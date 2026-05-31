import plotly.express as px


def create_distribution_chart(df, column):

    value_counts = df[column].value_counts()

    fig = px.bar(
        x=value_counts.index,
        y=value_counts.values,
        labels={
            "x": column,
            "y": "Quantidade"
        },
        title=f"Distribuição da coluna {column}"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title=column,
        yaxis_title="Quantidade",
        title_x=0.1
    )

    return fig