import os
from textwrap import dedent

from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# ---------------------------------------------------
# GERAÇÃO DE INSIGHTS COM IA
# ---------------------------------------------------

def generate_chemical_ai_insights(
    summary: str,
    columns: list,
    shape: tuple,
    analysis_mode: str
) -> str:

    if not api_key:
        return (
            "Erro: a chave da API Gemini não foi configurada. "
            "Verifique o arquivo .env."
        )

    if analysis_mode == "Química Analítica":
        domain_instructions = """
        Priorize:
        - concentração e absorbância;
        - curvas analíticas e calibração;
        - possível comportamento linear;
        - Lei de Beer-Lambert;
        - limitações e validação do método.

        Não considere um R² alto como validação completa do método.
        """

    elif analysis_mode == "Cinética Química":
        domain_instructions = """
        Priorize:
        - variação das espécies ao longo do tempo;
        - consumo de reagentes ou formação de produtos;
        - influência de temperatura, catalisador e condições;
        - tendências cinéticas observáveis.

        Não determine ordem ou mecanismo de reação sem evidências
        experimentais e comparação entre modelos cinéticos.
        """

    elif analysis_mode == "Controle de Qualidade":
        domain_instructions = """
        Priorize:
        - consistência entre amostras ou lotes;
        - dispersão e estabilidade dos resultados;
        - possíveis desvios e não conformidades;
        - parâmetros que merecem investigação;
        - necessidade de limites de especificação.

        Não declare conformidade sem que os limites aceitáveis
        estejam presentes no dataset ou no contexto.
        """

    elif analysis_mode == "Monitoramento Ambiental":
        domain_instructions = """
        Priorize:
        - parâmetros físico-químicos;
        - qualidade da água;
        - salinidade e condutividade;
        - nutrientes e possíveis fontes de contaminação;
        - diferenças entre pontos de coleta.

        Não declare contaminação ou risco ambiental definitivo
        sem valores de referência, legislação ou contexto amostral.
        """

    else:
        domain_instructions = """
        Faça uma análise geral, priorizando interpretações químicas
        somente quando forem sustentadas pelas variáveis disponíveis.
        """

    prompt = dedent(f"""
        Você é um químico e cientista de dados especializado na
        interpretação de dados químicos e laboratoriais.

        CONTEXTO SELECIONADO:
        {analysis_mode}

        DIRETRIZES DO CONTEXTO:
        {domain_instructions}

        INFORMAÇÕES DO DATASET:
        - Dimensão: {shape}
        - Colunas: {columns}

        RESUMO ESTATÍSTICO E AMOSTRA:
        {summary}

        Produza uma análise técnica, objetiva e acessível para químicos,
        incluindo graduandos com pouca experiência em ciência de dados.

        Use exatamente esta estrutura:

        ## 1. Diagnóstico principal
        Resuma em até 3 frases o comportamento mais importante dos dados.

        ## 2. Evidências observadas
        Apresente no máximo 4 tópicos, citando valores ou tendências
        realmente presentes no dataset.

        ## 3. Possíveis anomalias ou pontos de atenção
        Apresente no máximo 3 tópicos. Caso não haja evidência suficiente,
        informe isso claramente.

        ## 4. Interpretação química
        Explique, em linguagem técnica acessível, o significado químico
        dos principais padrões observados.

        ## 5. Próximos passos recomendados
        Sugira no máximo 4 verificações, experimentos ou análises adicionais.

        ## 6. Limitações
        Explique brevemente o que não pode ser concluído apenas com
        os dados fornecidos.

        REGRAS OBRIGATÓRIAS:

        - Use no máximo aproximadamente 600 palavras.
        - Não escreva saudações ou introduções como "Prezado químico".
        - Não repita a descrição do papel que você recebeu.
        - Não invente valores, variáveis, limites ou resultados.
        - Diferencie observação, interpretação e hipótese.
        - Não afirme causalidade apenas com base em correlação.
        - Não determine mecanismo ou ordem de reação sem evidência.
        - Não considere um método validado apenas por apresentar R² alto.
        - Não declare conformidade sem limites de especificação.
        - Quando faltarem dados, diga exatamente quais informações
          adicionais seriam necessárias.
        - Utilize português brasileiro e linguagem clara.
        - Nunca classifique um resultado como aceitável, conforme ou
          adequado quando o dataset não fornecer limites de especificação
          ou valores de referência.
        - Ao interpretar condutividade, considere que ela depende não
          apenas da quantidade de íons, mas também da identidade, carga,
          mobilidade, temperatura e composição da solução.
        - Evite afirmar proporcionalidade direta universal entre
          condutividade e concentração total de íons.
    """).strip()

    try:
        client = genai.Client(api_key=api_key)

        models_to_try = [
            "gemini-2.5-flash-lite",
            "gemini-2.0-flash-lite",
            "gemini-2.0-flash",
            "gemini-2.5-flash"
        ]

        errors = []

        for model_name in models_to_try:
            try:
                print(f"TENTANDO MODELO: {model_name}")

                response = client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                if response.text:
                    print(f"MODELO UTILIZADO: {model_name}")
                    return response.text.strip()

                print(
                    f"RESPOSTA VAZIA DO MODELO: {model_name}"
                )

                errors.append("EMPTY_RESPONSE")

            except Exception as model_error:
                error_message = str(model_error)

                # O erro completo permanece somente no terminal.
                print(
                    f"FALHA NO MODELO {model_name}: "
                    f"{error_message}"
                )

                if (
                    "429" in error_message
                    or "RESOURCE_EXHAUSTED" in error_message
                ):
                    errors.append("QUOTA")

                elif (
                    "503" in error_message
                    or "UNAVAILABLE" in error_message
                ):
                    errors.append("UNAVAILABLE")

                elif (
                    "401" in error_message
                    or "403" in error_message
                    or "API_KEY_INVALID" in error_message
                ):
                    errors.append("AUTHENTICATION")

                else:
                    errors.append("GENERAL")

        if "AUTHENTICATION" in errors:
            return (
                "Erro: não foi possível autenticar a integração com a IA. "
                "Verifique a configuração da chave da API."
            )

        if "QUOTA" in errors:
            return (
                "Erro: o limite temporário de uso dos modelos de IA "
                "foi atingido. Tente novamente mais tarde. "
                "Os gráficos, as estatísticas e os insights automáticos "
                "continuam disponíveis."
            )

        if "UNAVAILABLE" in errors:
            return (
                "Erro: os modelos de IA estão temporariamente "
                "indisponíveis devido à alta demanda. "
                "Aguarde alguns instantes e tente novamente."
            )

        return (
            "Erro: não foi possível gerar a análise com IA neste momento. "
            "As demais funcionalidades do ChemInsights AI continuam disponíveis."
        )

    except Exception as error:
        # Informação completa apenas para depuração no terminal.
        print(
            "ERRO AO CONFIGURAR A INTEGRAÇÃO COM IA: "
            f"{error}"
        )

        return (
            "Erro: ocorreu uma falha ao iniciar a integração com IA. "
            "Verifique a configuração e tente novamente."
        )
