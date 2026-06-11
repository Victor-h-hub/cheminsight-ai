import numpy as np
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

def create_histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        nbins=20,
        title=f"Distribuição de {column}"
    )

    fig.update_layout(
        showlegend=False
    )

    return fig

def create_scatter_plot(df, x_column, y_column):

    valid_data = df[
        [x_column, y_column]
    ].dropna().copy()

    fig = px.scatter(
        valid_data,
        x=x_column,
        y=y_column,
        title=f"{y_column} em função de {x_column}"
    )

    regression_results = None

    enough_points = len(valid_data) >= 2
    x_has_variation = valid_data[x_column].nunique() >= 2
    y_has_variation = valid_data[y_column].nunique() >= 2

    if enough_points and x_has_variation and y_has_variation:

        x_values = valid_data[x_column].to_numpy(
            dtype=float
        )

        y_values = valid_data[y_column].to_numpy(
            dtype=float
        )

        slope, intercept = np.polyfit(
            x_values,
            y_values,
            1
        )

        predicted_values = (
            slope * x_values
            + intercept
        )

        residual_sum_squares = np.sum(
            (y_values - predicted_values) ** 2
        )

        total_sum_squares = np.sum(
            (y_values - np.mean(y_values)) ** 2
        )

        r_squared = (
            1 - residual_sum_squares / total_sum_squares
        )

        ordered_x = np.sort(x_values)

        trend_y = (
            slope * ordered_x
            + intercept
        )

        fig.add_scatter(
            x=ordered_x,
            y=trend_y,
            mode="lines",
            name="Tendência linear"
        )

        regression_results = {
            "slope": slope,
            "intercept": intercept,
            "r_squared": r_squared,
            "valid_points": len(valid_data)
        }

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title=x_column,
        yaxis_title=y_column
    )

    return fig, regression_results