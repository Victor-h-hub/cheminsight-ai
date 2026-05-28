import streamlit as st
import pandas as pd
import plotly.express as px

from utils.insights import generate_basic_insights

st.title("AI Data Insights")

uploaded_file = st.file_uploader(
    "Envie um arquivo CSV",
    type=["csv"]
)

if uploaded_file is not None:

    # Leitura do CSV
    df = pd.read_csv(uploaded_file)

    # Mostrar tabela
    st.subheader("Prévia dos Dados")
    st.dataframe(df)

    # Métricas básicas
    st.subheader("Informações Gerais")

    st.write(f"Quantidade de linhas: {df.shape[0]}")
    st.write(f"Quantidade de colunas: {df.shape[1]}")

    # Tipos das colunas
    st.subheader("Tipos de Dados")
    st.write(df.dtypes)

    # Seleção de coluna para gráfico
    st.subheader("Visualização de Dados")

    column = st.selectbox(
        "Escolha uma coluna para visualizar",
        df.columns
    )

    # Contagem de valores
    value_counts = df[column].value_counts()

    # Criar gráfico
    fig = px.bar(
        x=value_counts.index,
        y=value_counts.values,
        labels={
            "x": column,
            "y": "Quantidade"
        },
        title=f"Distribuição da coluna {column}"
    )

    # Mostrar gráfico
    st.plotly_chart(fig)

    # Estatísticas numéricas
    st.subheader("Estatísticas Numéricas")

    numeric_columns = df.select_dtypes(include="number").columns

    if len(numeric_columns) > 0:

        selected_numeric = st.selectbox(
            "Escolha uma coluna numérica",
            numeric_columns
        )

        st.write(f"Média: {df[selected_numeric].mean():.2f}")
        st.write(f"Maior valor: {df[selected_numeric].max()}")
        st.write(f"Menor valor: {df[selected_numeric].min()}")
        st.write(f"Soma total: {df[selected_numeric].sum()}")

    # Insights automáticos
    st.subheader("Insights Automáticos")

    insights = generate_basic_insights(df)

    for insight in insights:
        st.write(insight)