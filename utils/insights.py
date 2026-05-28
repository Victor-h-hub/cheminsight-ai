def generate_basic_insights(df):

    insights = []

    insights.append(
        f"O dataset possui {df.shape[0]} linhas e {df.shape[1]} colunas."
    )

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        insights.append(
            f"A coluna '{column}' possui média de {df[column].mean():.2f}."
        )

        insights.append(
            f"O maior valor em '{column}' é {df[column].max()}."
        )

    return insights