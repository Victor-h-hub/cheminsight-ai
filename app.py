# ===================================================
## IMPORTAÇÕES
# ===================================================

import streamlit as st
import pandas as pd


from utils.charts import (
    create_distribution_chart,
    create_histogram,
    create_scatter_plot
)
from utils.insights import generate_chemical_insights
from utils.ai_insights import generate_chemical_ai_insights
from utils.chemical_analysis import (
    analyze_mode_compatibility,
    suggest_scatter_axes
)

# ===================================================
## CONFIGURAÇÃO DA PÁGINA
# ===================================================

st.set_page_config(
    page_title="ChemInsights AI",
    page_icon="⚗️",
    layout="wide"
)

if "ai_response" not in st.session_state:
    st.session_state.ai_response = None

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

if "last_analysis_mode" not in st.session_state:
    st.session_state.last_analysis_mode = None


# ===================================================
## TÍTULO E DESCRIÇÃO PRINCIPAL
# ===================================================

st.title("⚗️ ChemInsights AI")

st.markdown("""
Plataforma inteligente para análise exploratória de dados químicos e laboratoriais.

Faça upload de um arquivo CSV para:

- visualizar e validar dados experimentais;
- gerar estatísticas descritivas;
- analisar relações entre variáveis;
- criar gráficos interativos;
- receber insights automáticos;
- obter interpretações químicas assistidas por IA.
""")


# ===================================================
## SIDEBAR
# ===================================================

st.sidebar.title("⚗️ Painel do ChemInsights")

st.sidebar.markdown("""
**Tecnologias utilizadas**

- Python
- Streamlit
- Pandas
- Plotly
- Gemini AI

**Contextos disponíveis**

- Química Analítica
- Cinética Química
- Controle de Qualidade
- Monitoramento Ambiental
""")


# ===================================================
## UPLOAD DO CSV
# ===================================================

uploaded_file = st.sidebar.file_uploader(
    "Envie um arquivo CSV com dados químicos ou laboratoriais.",
    type=["csv"]
)


# ===================================================
# VALIDAÇÃO DO UPLOAD
# ===================================================

if uploaded_file is None:
    st.session_state.ai_response = None
    st.session_state.uploaded_file_name = None
    st.session_state.last_analysis_mode = None

    st.info("Envie um arquivo CSV para iniciar a análise.")
    st.stop()

if uploaded_file.name != st.session_state.uploaded_file_name:
    st.session_state.ai_response = None
    st.session_state.uploaded_file_name = uploaded_file.name


# ===================================================
# LEITURA DO CSV
# ===================================================

def read_csv_file(file):
    attempts = [
        {"sep": ",", "encoding": "utf-8"},
        {"sep": ";", "encoding": "utf-8"},
        {"sep": ",", "encoding": "latin1"},
        {"sep": ";", "encoding": "latin1"},
    ]

    best_df = None
    best_score = -1
    last_error = None

    for options in attempts:
        try:
            file.seek(0)

            current_df = pd.read_csv(
                file,
                **options
            )

            score = current_df.shape[1]

            if score > best_score:
                best_df = current_df
                best_score = score

        except Exception as error:
            last_error = error

    if best_df is not None:
        return best_df

    if last_error is not None:
        raise last_error

    raise ValueError("Não foi possível interpretar o arquivo CSV.")


try:
    df = read_csv_file(uploaded_file)

except Exception as error:
    st.error(
        f"Não foi possível ler o arquivo CSV: {error}"
    )
    st.stop()


# ===================================================
# VALIDAÇÃO DO DATAFRAME
# ===================================================

if df.empty:
    st.warning(
        "O arquivo CSV foi carregado, mas está vazio."
    )
    st.stop()

st.success("Arquivo carregado com sucesso!")

# ===================================================
## PRÉVIA DOS DADOS
# ===================================================

st.subheader("📄 Prévia dos Dados")

st.dataframe(
    df,
    width="stretch"
)

st.divider()


# ===================================================
## INFORMAÇÕES GERAIS
# ===================================================

st.subheader("📌 Informações Gerais")

col1, col2 = st.columns(2)

with col1:
    st.metric("Quantidade de Linhas", df.shape[0])

with col2:
    st.metric("Quantidade de Colunas", df.shape[1])

st.divider()


# ===================================================
## TIPOS DE DADOS
# ===================================================

st.subheader("🧩 Tipos de Dados")

data_types_df = df.dtypes.reset_index()
data_types_df.columns = ["Coluna", "Tipo"]

st.dataframe(
    data_types_df,
    width="stretch",
    hide_index=True
)

st.divider()



# ===================================================
# CONTEXTO QUÍMICO DA ANÁLISE
# ===================================================

st.subheader("🧪 Contexto Químico")

analysis_mode = st.selectbox(
    "Selecione o contexto da análise",
    [
        "Química Analítica",
        "Cinética Química",
        "Controle de Qualidade",
        "Monitoramento Ambiental"
    ],
    key="analysis_mode"
)

analysis_mode_descriptions = {
    "Química Analítica": (
        "Analisa relações entre concentração, absorbância, "
        "curvas de calibração e resultados de métodos analíticos."
    ),
    "Cinética Química": (
        "Analisa como reagentes ou produtos variam ao longo do tempo "
        "e identifica tendências experimentais."
    ),
    "Controle de Qualidade": (
        "Avalia consistência entre amostras ou lotes, variações, "
        "desvios e possíveis não conformidades."
    ),
    "Monitoramento Ambiental": (
        "Analisa parâmetros físico-químicos relacionados à qualidade "
        "da água, contaminação e salinização."
    )
}

st.info(analysis_mode_descriptions[analysis_mode])

compatibility_result = analyze_mode_compatibility(
    columns=list(df.columns),
    analysis_mode=analysis_mode
)

if compatibility_result["compatible"]:
    st.success(
        "O arquivo possui variáveis compatíveis com "
        "o contexto selecionado."
    )
else:
    missing_variables = compatibility_result["missing_variables"]
    missing_text = ", ".join(missing_variables)

    st.warning(
        "O arquivo pode não conter todas as variáveis "
        f"esperadas para este contexto. Ausências identificadas: "
        f"{missing_text}. A análise ainda pode ser executada, "
        "mas suas conclusões poderão ser limitadas."
    )

identified_columns = compatibility_result["identified_columns"]

st.divider()


# ===================================================
## VISUALIZAÇÃO GRÁFICA
# ===================================================

st.subheader("📊 Visualização dos Dados Experimentais")
chart_type = st.radio(
    "Tipo de gráfico",
    ["Barras", "Histograma", "Dispersão"],
    horizontal=True,
    key="chart_type"
)

numeric_columns_chart = df.select_dtypes(include="number").columns

suggested_x, suggested_y = suggest_scatter_axes(
    numeric_columns=numeric_columns_chart,
    analysis_mode=analysis_mode,
    identified_columns=identified_columns
)

try:
    if chart_type == "Barras":
        column = st.selectbox(
            "Selecione uma variável para analisar graficamente",
            df.columns,
            key="bar_column"
        )

        fig = create_distribution_chart(df, column)

        st.plotly_chart(
            fig,
            width="stretch",
            config={"displayModeBar": False}
        )

        st.caption("Exibindo até os 20 valores mais frequentes.")

    elif chart_type == "Histograma":
        if len(numeric_columns_chart) == 0:
            st.warning("Nenhuma coluna numérica disponível para histograma.")
        else:
            column = st.selectbox(
                "Selecione uma variável numérica",
                numeric_columns_chart,
                key="histogram_column"
            )

            fig = create_histogram(df, column)

            st.plotly_chart(
                fig,
                width="stretch",
                config={"displayModeBar": False}
            )

    elif chart_type == "Dispersão":
        if len(numeric_columns_chart) < 2:
            st.warning("São necessárias pelo menos duas colunas numéricas.")
        else:
            numeric_columns_list = list(numeric_columns_chart)

            x_default_index = 0
            y_default_index = 1

            if suggested_x in numeric_columns_list:
                x_default_index = numeric_columns_list.index(suggested_x)

            if suggested_y in numeric_columns_list:
                y_default_index = numeric_columns_list.index(suggested_y)

            if suggested_x and suggested_y:
                st.info(
                    f"Sugestão para este contexto: "
                    f"X = {suggested_x} e Y = {suggested_y}."
                )

            x_column = st.selectbox(
                "Variável do eixo X",
                numeric_columns_list,
                index=x_default_index,
                key=f"scatter_x_column_{analysis_mode}",
            )

            y_column = st.selectbox(
                "Variável do eixo Y",
                numeric_columns_list,
                index=y_default_index,
                key=f"scatter_y_column_{analysis_mode}",
            )

            fig, regression_results = create_scatter_plot(
                df,
                x_column,
                y_column
            )

            st.plotly_chart(
                fig,
                width="stretch",
                config={"displayModeBar": False}
            )        
            if regression_results:

                slope = regression_results["slope"]
                intercept = regression_results["intercept"]
                r_squared = regression_results["r_squared"]

                st.markdown("#### 📐 Ajuste linear")

                metric_col1, metric_col2, metric_col3 = st.columns(3)

                with metric_col1:
                    st.metric(
                        "Inclinação",
                        f"{slope:.4f}"
                    )

                with metric_col2:
                    st.metric(
                        "Intercepto",
                        f"{intercept:.4f}"
                    )

                with metric_col3:
                    st.metric(
                        "R²",
                        f"{r_squared:.4f}"
                    )

                st.write(
                    f"**Equação estimada:** "
                    f"y = {slope:.4f}x {intercept:+.4f}"
                )

                st.write(
                    f"**Coeficiente de determinação:** "
                    f"R² = {r_squared:.4f}"
                )
                
                st.markdown("#### 🔎 Interpretação do ajuste")

                if slope > 0:
                    trend_interpretation = (
                        f"À medida que **{x_column}** aumenta, "
                        f"**{y_column}** apresenta tendência de aumento."
                    )

                elif slope < 0:
                    trend_interpretation = (
                        f"À medida que **{x_column}** aumenta, "
                        f"**{y_column}** apresenta tendência de diminuição."
                    )

                else:
                    trend_interpretation = (
                        f"O ajuste indica pouca ou nenhuma variação média "
                        f"de **{y_column}** em relação a **{x_column}**."
                    )

                st.write(trend_interpretation)

                if r_squared >= 0.90:
                    st.success(
                        "O ajuste linear representa muito bem a variação "
                        "observada nos dados."
                    )

                elif r_squared >= 0.70:
                    st.info(
                        "O ajuste linear representa de forma moderada "
                        "a variação observada nos dados."
                    )

                else:
                    st.warning(
                        "O ajuste linear representa pouco da variação "
                        "observada. Outros modelos ou variáveis podem ser "
                        "necessários."
                    )

                st.caption(
                    "Um R² alto não prova causalidade, não determina "
                    "sozinho a ordem de uma reação e não valida "
                    "isoladamente um método analítico."
                )
            else:

                st.info(
                    "Não foi possível calcular o ajuste linear. "
                    "São necessários pelo menos dois pontos válidos "
                    "e variação nos valores dos eixos X e Y."
                )

            with st.expander(
    "📘 Como interpretar a linha, a equação e o R²?"
):
                st.markdown("""
### Linha de tendência

É uma reta que resume o comportamento geral dos pontos.

Ela não significa que todos os dados seguem perfeitamente uma relação linear. Ela representa o ajuste linear que melhor aproxima os valores observados.

### Equação da reta

A equação tem o formato:

**y = ax + b**

- **a — inclinação:** indica quanto Y tende a variar quando X aumenta uma unidade;
- **b — intercepto:** valor estimado de Y quando X é igual a zero.

Uma inclinação positiva indica tendência de aumento.

Uma inclinação negativa indica tendência de diminuição.

### Coeficiente de determinação — R²

O R² varia, em geral, de 0 a 1.

- próximo de **1:** o modelo linear representa bem a variação observada;
- próximo de **0:** a reta explica pouco da variação dos dados.

Um R² alto não prova causalidade, não valida sozinho um método analítico e não determina o mecanismo de uma reação.

### Cuidado na interpretação química

Em espectrofotometria, um R² alto pode indicar boa linearidade entre concentração e absorbância, mas a validação de uma curva analítica exige outras avaliações.

Em cinética química, a linearidade entre concentração e tempo não é suficiente para definir a ordem da reação. Para isso, devem ser comparadas diferentes formas integradas e consideradas as condições experimentais.
""")
except Exception as error:
    st.error(f"Não foi possível gerar o gráfico: {error}")

st.divider()


# ===================================================
## ESTATÍSTICAS NUMÉRICAS
# ===================================================

st.subheader("📈 Estatísticas Numéricas")

numeric_columns = df.select_dtypes(
    include="number"
).columns

if len(numeric_columns) == 0:
    st.info("Nenhuma coluna numérica encontrada no arquivo.")

else:
    selected_numeric = st.selectbox(
        "Escolha uma coluna numérica",
        numeric_columns,
        key="numeric_stats_column"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Média",
            f"{df[selected_numeric].mean():.2f}"
        )

        st.metric(
            "Maior Valor",
            f"{df[selected_numeric].max():.2f}"
        )

    with col2:
        st.metric(
            "Menor Valor",
            f"{df[selected_numeric].min():.2f}"
        )

        st.metric(
            "Desvio Padrão",
            f"{df[selected_numeric].std():.2f}"
        )

    with st.expander(
        "📘 Como interpretar estas estatísticas?"
    ):
        st.markdown("""
### Média

Representa o valor central obtido pela soma dos resultados dividida pela quantidade de observações.

Pode ser influenciada por valores muito altos ou muito baixos.

### Menor e maior valor

Indicam os extremos observados no conjunto de dados.

São úteis para identificar a faixa experimental e possíveis valores atípicos.

### Desvio padrão

Indica o quanto os valores se afastam, em média, da média do conjunto.

- desvio padrão pequeno: resultados mais próximos entre si;
- desvio padrão alto: maior dispersão dos resultados.

O significado de um desvio padrão ser "alto" ou "baixo" depende da unidade, da escala e do contexto experimental.

### Atenção

Essas estatísticas descrevem os dados disponíveis, mas não comprovam sozinhas:

- qualidade do método;
- precisão experimental;
- presença de erro sistemático;
- causalidade entre variáveis.
""")

st.divider()


# ===================================================
## INSIGHTS AUTOMÁTICOS
# ===================================================

st.subheader("🧠 Insights Automáticos")

try:
    insights = generate_chemical_insights(df)

    if insights:
        for insight in insights:
            st.write(insight)
    else:
        st.info("Nenhum insight automático foi gerado.")

except Exception as error:
    st.error(f"Não foi possível gerar os insights automáticos: {error}")

st.divider()


# ===================================================
## PREPARAÇÃO DOS DADOS PARA IA
# ===================================================

numeric_summary = (
    df.describe().to_string()
    if len(numeric_columns) > 0
    else "Nenhuma coluna numérica disponível."
)

sample_data = df.head(5).to_string()
data_types = df.dtypes.to_string()

summary = f"""
TIPOS DE DADOS:
{data_types}

ESTATÍSTICAS NUMÉRICAS:
{numeric_summary}

AMOSTRA DOS DADOS:
{sample_data}
"""


# ===================================================
## INSIGHTS ESTRATÉGICOS COM IA
# ===================================================

st.subheader("🤖 Insights Estratégicos com IA")

st.info(analysis_mode_descriptions[analysis_mode])

if compatibility_result["compatible"]:
    st.success(
        "O arquivo possui variáveis compatíveis com "
        "o contexto selecionado."
    )
else:
    missing_variables = compatibility_result["missing_variables"]
    missing_text = ", ".join(missing_variables)

    st.warning(
        "O arquivo pode não conter todas as variáveis "
        f"esperadas para este contexto. Ausências identificadas: "
        f"{missing_text}. A análise ainda pode ser executada, "
        "mas suas conclusões poderão ser limitadas."
    )

if analysis_mode != st.session_state.last_analysis_mode:
    st.session_state.ai_response = None
    st.session_state.last_analysis_mode = analysis_mode

if st.button("🚀 Gerar Insights com IA"):
    st.session_state.ai_response = None

    try:
        with st.spinner("Gerando insights com IA..."):
            st.session_state.ai_response = generate_chemical_ai_insights(
                summary=summary,
                columns=list(df.columns),
                shape=df.shape,
                analysis_mode=analysis_mode
            )
            

    except Exception as error:
        st.error(f"Não foi possível gerar os insights com IA: {error}")


# ===================================================
## EXIBIÇÃO DOS INSIGHTS DA IA
# ===================================================

if st.session_state.ai_response:
    if st.session_state.ai_response.startswith("Erro"):
        st.warning(st.session_state.ai_response)
    else:
        st.write(st.session_state.ai_response)
else:
    st.info("Clique no botão acima para gerar insights estratégicos com IA.")