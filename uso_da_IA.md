# 🤖 Uso da Inteligência Artificial no Desenvolvimento

## Objetivo deste documento

Este documento apresenta, de forma transparente, como ferramentas de Inteligência Artificial foram utilizadas durante o desenvolvimento do **ChemInsights AI**, projeto criado para a segunda fase de um processo seletivo de Engenharia de Soluções Júnior/Trainee.

O objetivo é registrar:

* quais atividades receberam apoio de IA;
* quais decisões permaneceram sob responsabilidade do desenvolvedor;
* como as sugestões foram testadas e revisadas;
* quais erros e limitações foram identificados;
* como a IA contribuiu para acelerar o aprendizado;
* por que a solução não depende exclusivamente de IA generativa.

A IA foi utilizada como ferramenta de aprendizado, orientação técnica, revisão e aceleração do desenvolvimento, e não como substituta da responsabilidade humana sobre o projeto.

---

# Contexto do desenvolvimento

O projeto foi desenvolvido por um estudante de Química que estava iniciando seus estudos práticos em Python, desenvolvimento de aplicações web e análise de dados.

O primeiro MVP, chamado **AI Data Insights**, permitia:

* carregar arquivos CSV;
* visualizar dados;
* calcular estatísticas;
* gerar gráficos;
* produzir insights automáticos;
* solicitar interpretações à API Gemini.

Após a primeira avaliação, foi recebido o feedback de que o projeto estava genérico e deveria aplicar conceitos mais avançados de química.

A partir disso, o sistema foi transformado no:

# ⚗️ ChemInsights AI

Uma plataforma de análise exploratória de dados químicos e laboratoriais, com:

* cálculos determinísticos em Python;
* regras químicas explícitas;
* regressão linear;
* explicações didáticas;
* validação do contexto;
* interpretação complementar com IA.

A decisão de reaproveitar a arquitetura existente, em vez de reconstruir tudo, foi conduzida pelo desenvolvedor.

---

# Ferramentas de IA utilizadas

Durante o desenvolvimento foram utilizadas:

* ChatGPT;
* Claude;
* Google Gemini.

As ferramentas tiveram funções diferentes ao longo do processo.

## ChatGPT

Utilizado principalmente como:

* orientador técnico;
* professor de programação;
* apoio à arquitetura;
* auxílio na depuração;
* explicação de conceitos;
* revisão de decisões;
* apoio à documentação;
* parceiro para desenvolvimento incremental.

## Claude

Utilizado principalmente para:

* obter uma segunda opinião sobre o código;
* revisar possíveis inconsistências;
* comparar abordagens;
* avaliar problemas de importação e ambiente;
* revisar estruturas e prompts.

## Google Gemini

Utilizado em dois papéis diferentes:

1. como modelo integrado ao ChemInsights AI para interpretar os datasets;
2. como ferramenta de comparação e apoio pontual durante o desenvolvimento.

---

# Como a IA foi utilizada

## 1. Aprendizado de programação

A IA foi utilizada para explicar conceitos que ainda eram novos para o desenvolvedor, incluindo:

* variáveis;
* funções;
* parâmetros;
* condicionais;
* laços;
* tratamento de exceções;
* imports;
* módulos;
* ambientes virtuais;
* bibliotecas;
* APIs;
* variáveis de ambiente;
* cache;
* estado de sessão;
* leitura de mensagens de erro.

As respostas não foram usadas apenas como código pronto.

Foi solicitado que os conceitos fossem explicados passo a passo, incluindo:

* por que a alteração era necessária;
* qual arquivo seria afetado;
* quais riscos existiam;
* como testar;
* como reconhecer se a mudança funcionou.

---

## 2. Estruturação do projeto

A IA ajudou a sugerir uma arquitetura modular para separar responsabilidades.

A estrutura evoluiu para:

```text
app.py
utils/
├── ai_insights.py
├── charts.py
├── chemical_analysis.py
└── insights.py
```

As responsabilidades ficaram distribuídas da seguinte forma:

| Arquivo                | Responsabilidade                             |
| ---------------------- | -------------------------------------------- |
| `app.py`               | Interface e fluxo principal                  |
| `charts.py`            | Gráficos, regressão e indicadores            |
| `insights.py`          | Insights determinísticos                     |
| `chemical_analysis.py` | Reconhecimento de colunas e compatibilidade  |
| `ai_insights.py`       | Integração com Gemini e engenharia de prompt |

A sugestão de modularização contou com apoio da IA, mas a decisão de manter uma arquitetura simples, compatível com um MVP, foi do desenvolvedor.

---

## 3. Construção de funcionalidades

A IA auxiliou na implementação de:

* upload de CSV;
* leitura com diferentes separadores;
* validação de arquivos;
* prévia do DataFrame;
* identificação dos tipos de dados;
* estatísticas descritivas;
* gráficos com Plotly;
* histogramas;
* gráfico de dispersão;
* regressão linear;
* cálculo de inclinação;
* cálculo de intercepto;
* cálculo do (R^2);
* regras químicas determinísticas;
* reconhecimento dos nomes das colunas;
* validação do contexto selecionado;
* sugestão automática dos eixos;
* integração com a API Gemini;
* fallback entre modelos;
* tratamento de erros;
* mensagens explicativas para o usuário.

O código sugerido não foi aceito automaticamente.

Cada alteração passou por testes no aplicativo e, quando necessário, foi corrigida ou descartada.

---

# Uso da IA generativa dentro do produto

O Gemini foi integrado ao ChemInsights AI como uma camada complementar de interpretação.

Ele recebe:

* nomes das colunas;
* dimensão do dataset;
* tipos dos dados;
* resumo estatístico;
* amostra das primeiras linhas;
* contexto químico selecionado.

A resposta é estruturada em:

1. diagnóstico principal;
2. evidências observadas;
3. possíveis anomalias;
4. interpretação química;
5. próximos passos recomendados;
6. limitações.

A IA não executa os principais cálculos numéricos do sistema.

Os cálculos são realizados em Python antes da chamada ao modelo.

---

# Separação entre cálculo e interpretação

Uma decisão central do projeto foi não entregar toda a análise ao Gemini.

O fluxo foi organizado assim:

```text
Python
→ cálculos verificáveis

Regras químicas determinísticas
→ interpretação inicial baseada em critérios explícitos

Gemini
→ contextualização, hipóteses e recomendações
```

## Cálculos feitos em Python

* média;
* mínimo;
* máximo;
* desvio padrão;
* correlação;
* regressão linear;
* inclinação;
* intercepto;
* (R^2).

## Regras químicas explícitas

* reconhecimento de tempo e concentração;
* reconhecimento de concentração e absorbância;
* validação básica do intervalo convencional de pH;
* identificação de tendências;
* verificação de compatibilidade;
* sugestão de eixos;
* avisos sobre limites científicos.

## Papel do Gemini

* organizar a interpretação;
* contextualizar os resultados;
* levantar hipóteses;
* sugerir próximos passos;
* indicar limitações;
* traduzir resultados para linguagem técnica acessível.

Essa separação reduz o risco de o modelo inventar números ou substituir cálculos reproduzíveis.

---

# Engenharia de prompt

O prompt do Gemini foi refinado ao longo dos testes.

Foram criadas instruções específicas para quatro contextos.

## Química Analítica

O modelo foi orientado a considerar:

* concentração;
* absorbância;
* curvas de calibração;
* espectrofotometria;
* Lei de Beer-Lambert;
* validação de métodos.

Também recebeu a regra de que um (R^2) alto não valida sozinho um método analítico.

## Cinética Química

O modelo foi orientado a considerar:

* tempo;
* concentração;
* consumo de reagentes;
* formação de produtos;
* temperatura;
* tendências cinéticas.

Também recebeu a regra de não determinar ordem ou mecanismo da reação sem evidências suficientes.

## Controle de Qualidade

O modelo foi orientado a considerar:

* lotes;
* pH;
* condutividade;
* rendimento;
* estabilidade;
* possíveis desvios.

Também recebeu a regra de não declarar conformidade sem limites de especificação.

## Monitoramento Ambiental

O modelo foi orientado a considerar:

* pH;
* condutividade;
* salinidade;
* nitrato;
* fosfato;
* pontos de coleta;
* possíveis alterações ambientais.

Também recebeu a regra de não declarar contaminação ou risco definitivo sem referências técnicas ou legais.

---

# Exemplos de revisão crítica das respostas

As respostas da IA não foram aceitas apenas porque pareciam tecnicamente convincentes.

Durante os testes, algumas respostas foram corrigidas.

## Classificação de resultado como aceitável

Em uma análise de controle de qualidade, a IA classificou uma faixa de rendimento como aceitável mesmo sem possuir limites de especificação.

O prompt foi alterado para proibir classificações como:

* aceitável;
* conforme;
* adequado.

Esses termos só podem ser usados quando houver valores de referência.

## Interpretação da condutividade

A IA tratou inicialmente a condutividade como diretamente proporcional à concentração total de íons.

A regra foi refinada para considerar também:

* identidade dos íons;
* carga;
* mobilidade;
* temperatura;
* composição da solução.

## Uso do (R^2)

O modelo poderia interpretar um (R^2) próximo de 1 como prova suficiente de qualidade.

Foram acrescentadas ressalvas para explicar que um (R^2) alto:

* não prova causalidade;
* não valida sozinho um método;
* não determina mecanismo;
* não define automaticamente a ordem da reação.

---

# Erros das IAs durante o desenvolvimento

A IA também produziu sugestões incorretas ou inadequadas.

## Problemas de código

Foram observados:

* funções com assinaturas incompatíveis;
* código com indentação incorreta;
* duplicidade de widgets;
* uso inadequado de `st.session_state`;
* alterações sugeridas no local errado do arquivo;
* trechos que utilizavam variáveis antes de sua criação;
* sugestões de cache que dificultaram a depuração.

## Problemas com modelos Gemini

Algumas sugestões utilizaram:

```text
gemini-1.5-flash
```

Esse modelo não estava disponível no endpoint utilizado.

Foi necessário:

* listar os modelos realmente disponíveis para a chave;
* identificar modelos válidos;
* atualizar a integração;
* testar individualmente as chamadas.

## Sugestões excessivamente complexas

Em diferentes momentos, as IAs sugeriram funcionalidades como:

* banco de dados;
* autenticação;
* exportação;
* novos provedores;
* machine learning;
* arquitetura mais complexa.

Essas sugestões foram descartadas por não serem necessárias para o MVP e por aumentarem o risco dentro do prazo.

---

# Depuração e validação

A IA auxiliou na interpretação de erros, mas a validação ocorreu por meio da execução real do sistema.

Foram investigados erros como:

* `NameError`;
* `AttributeError`;
* `ImportError`;
* `StreamlitDuplicateElementId`;
* argumento inesperado em função;
* cache de módulos;
* arquivos importados incorretamente;
* modelo não encontrado;
* erro 404;
* erro 429;
* erro 503;
* resposta vazia;
* falha de estado da aplicação.

Em alguns casos, hipóteses iniciais da IA estavam incorretas.

A causa real só foi identificada após:

* inspeção do código;
* leitura do traceback;
* testes no terminal;
* verificação do caminho dos módulos;
* remoção de cache;
* renomeação de funções;
* consulta aos modelos disponíveis;
* comparação entre o comportamento esperado e o observado.

---

# Resiliência da API

Durante os testes, o Gemini apresentou:

* alta demanda;
* indisponibilidade temporária;
* limite de cota;
* modelo não encontrado.

Para reduzir o impacto desses problemas, foi implementado fallback entre modelos.

A aplicação tenta diferentes modelos compatíveis.

Caso nenhum responda, o sistema apresenta uma mensagem amigável.

Os detalhes técnicos ficam no terminal e não são exibidos ao usuário final.

Mesmo sem resposta da IA, continuam funcionando:

* upload;
* tabela;
* estatísticas;
* gráficos;
* regressão;
* compatibilidade;
* sugestão de eixos;
* insights determinísticos.

---

# Decisões conduzidas pelo desenvolvedor

## Definição do problema

Foi definida a transformação do projeto genérico em uma solução voltada para química e laboratório.

## Público-alvo

Foram considerados:

* graduandos;
* químicos;
* pesquisadores;
* analistas;
* profissionais laboratoriais.

## Escopo

Foi decidido manter um MVP simples e funcional.

Funcionalidades maiores foram registradas como melhorias futuras.

## Reaproveitamento da arquitetura

Foi decidido não criar um projeto completamente novo após o feedback.

A base existente foi adaptada, reduzindo risco e retrabalho.

## Escolha dos contextos

Foram selecionados:

* Química Analítica;
* Cinética Química;
* Controle de Qualidade;
* Monitoramento Ambiental.

## Experiência do usuário

Foi decidido que o sistema deveria:

* usar conceitos avançados;
* explicar os indicadores;
* orientar a escolha dos eixos;
* avisar sobre incompatibilidades;
* não bloquear o usuário;
* manter linguagem acessível.

## Limites científicos

Foi definido que o sistema deveria comunicar o que não pode ser concluído a partir dos dados.

---

# O que foi ajustado manualmente

Durante o desenvolvimento, foram realizados ajustes manuais em:

* organização dos arquivos;
* imports;
* indentação;
* nomes das funções;
* estado da interface;
* mensagens do usuário;
* prompt químico;
* ordem dos modelos;
* tratamento de erros;
* textos didáticos;
* validação das respostas;
* estrutura da documentação;
* caminhos das imagens;
* proteção da chave da API.

---

# Como as sugestões foram avaliadas

Cada sugestão foi analisada considerando:

* impacto no case;
* tempo disponível;
* risco técnico;
* valor para o usuário;
* coerência química;
* facilidade de explicação;
* estabilidade da aplicação.

A prioridade foi dada a alterações com:

* alto valor;
* baixo ou médio risco;
* capacidade de demonstração;
* possibilidade de conclusão dentro do prazo.

---

# Limitações do uso de IA

A experiência confirmou que IAs generativas podem:

* produzir código que parece correto, mas não executa;
* sugerir bibliotecas ou modelos desatualizados;
* ignorar o estado atual do projeto;
* gerar soluções incompatíveis com a arquitetura;
* exagerar conclusões científicas;
* fornecer respostas diferentes para o mesmo problema;
* induzir a excesso de complexidade;
* esconder incertezas em textos convincentes.

Por isso, a IA exige:

* testes;
* leitura crítica;
* comparação;
* validação;
* compreensão mínima do código;
* responsabilidade humana.

---

# Aprendizados sobre uso responsável de IA

O principal aprendizado não foi apenas como pedir código.

Foi aprender a utilizar a IA como:

* professora;
* revisora;
* geradora de hipóteses;
* apoio de produtividade;
* ferramenta de comparação.

Também foi necessário aprender quando:

* não aceitar uma sugestão;
* pedir uma explicação;
* reduzir a complexidade;
* testar manualmente;
* consultar documentação;
* preservar uma versão funcional;
* interromper a adição de funcionalidades.

---

# Considerações finais

A Inteligência Artificial teve papel relevante no desenvolvimento do ChemInsights AI.

Ela permitiu:

* acelerar o aprendizado;
* explorar tecnologias novas;
* identificar erros;
* comparar soluções;
* estruturar prompts;
* melhorar a documentação;
* construir um MVP em prazo reduzido.

Entretanto, a IA também apresentou erros técnicos, sugestões inadequadas e interpretações químicas que precisaram ser corrigidas.

A responsabilidade final permaneceu humana.

Foram conduzidas pelo desenvolvedor:

* definição do problema;
* escolha do público;
* decisão de reaproveitar o projeto;
* seleção das funcionalidades;
* definição dos contextos químicos;
* testes;
* validação das respostas;
* controle de escopo;
* organização da experiência;
* aceitação ou rejeição das sugestões;
* decisão de encerrar o desenvolvimento funcional.

O uso da IA foi realizado de forma transparente, crítica e orientada ao aprendizado.

> A IA acelerou o processo, mas não eliminou a necessidade de compreender, testar, questionar e decidir.
