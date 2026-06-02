# ===================================================
## IMPORTAÇÕES
# ===================================================
import streamlit as st
import pandas as pd
from utils.charts import (
    create_distribution_chart,
    create_histogram
)
from utils.insights import generate_basic_insights
from utils.ai_insights import generate_ai_insights


# ===================================================
## CONFIGURAÇÃO DA PÁGINA
# ===================================================

st.set_page_config(
    page_title="AI Data Insights",
    page_icon="📊",
    layout="wide"
)


# ===================================================
## TÍTULO E DESCRIÇÃO PRINCIPAL
# ===================================================

st.title("📊 AI Data Insights")

st.markdown("""
Sistema simples de análise de dados com IA.

Faça upload de um arquivo CSV para:
- visualizar dados;
- gerar gráficos;
- obter estatísticas;
- receber insights automáticos com IA.
""")


# ===================================================
## SIDEBAR
# ===================================================

st.sidebar.title("⚙️ Painel do Sistema")

st.sidebar.markdown("""
Este projeto utiliza:
- Python
- Streamlit
- Pandas
- Plotly
- Gemini AI
""")


# ===================================================
## UPLOAD DO CSV
# ===================================================

uploaded_file = st.sidebar.file_uploader(
    "Faça upload de um arquivo CSV para começar a análise dos dados.",
    type=["csv"]
)


# ===================================================
## VALIDAÇÃO DO UPLOAD
# ===================================================

if uploaded_file is None:
    st.info("Envie um arquivo CSV para iniciar a análise.")
    st.stop()


# ===================================================
## LEITURA DO CSV
# ===================================================

def read_csv_file(file):
    attempts = [
        {"sep": ",", "encoding": "utf-8"},
        {"sep": ";", "encoding": "utf-8"},
        {"sep": ",", "encoding": "latin1"},
        {"sep": ";", "encoding": "latin1"},
    ]

    last_error = None

    for options in attempts:
        try:
            file.seek(0)
            return pd.read_csv(file, **options)
        except Exception as error:
            last_error = error

    raise last_error


try:
    df = read_csv_file(uploaded_file)

except Exception as error:
    st.error(f"Não foi possível ler o arquivo CSV: {error}")
    st.stop()


# ===================================================
## VALIDAÇÃO DO DATAFRAME
# ===================================================

if df.empty:
    st.warning("O arquivo CSV foi carregado, mas está vazio.")
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
    st.metric(
        "Quantidade de Linhas",
        df.shape[0]
    )

with col2:
    st.metric(
        "Quantidade de Colunas",
        df.shape[1]
    )

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
## VISUALIZAÇÃO GRÁFICA
# ===================================================

st.subheader("📊 Distribuição dos Dados")

chart_type = st.radio(
    "Tipo de gráfico",
    ["Barras", "Histograma"],
    horizontal=True
)

column = st.selectbox(
    "Selecione uma variável para analisar graficamente",
    df.columns
)

if chart_type == "Barras":

    fig = create_distribution_chart(
        df,
        column
    )

    st.plotly_chart(
        fig,
        width="stretch",
        config={"displayModeBar": False}
    )

else:

    if pd.api.types.is_numeric_dtype(df[column]):

        fig = create_histogram(
            df,
            column
        )

        st.plotly_chart(
            fig,
            width="stretch",
            config={"displayModeBar": False}
        )

    else:

        st.warning(
            "Histograma só pode ser gerado para colunas numéricas."
        )

st.caption(
    "Exibindo até os 20 valores mais frequentes."
)

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
        numeric_columns
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
            "Soma Total",
            f"{df[selected_numeric].sum():.2f}"
        )

st.divider()


# ===================================================
## INSIGHTS AUTOMÁTICOS
# ===================================================

st.subheader("🧠 Insights Automáticos")

try:
    insights = generate_basic_insights(df)

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

if st.button("🚀 Gerar Insights com IA"):

    try:
        with st.spinner("Gerando insights com IA..."):

            ai_response = generate_ai_insights(
                summary=summary,
                columns=list(df.columns),
                shape=df.shape
            )

            st.write(ai_response)

    except Exception as error:
        st.error(
            f"Não foi possível gerar os insights com IA: {error}"
        )
