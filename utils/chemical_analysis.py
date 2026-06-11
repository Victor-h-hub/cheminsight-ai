import unicodedata


def normalize_column_name(column_name):
    """
    Padroniza o nome de uma coluna para facilitar
    a identificação de variáveis químicas.
    """

    normalized_name = unicodedata.normalize(
        "NFKD",
        str(column_name)
    )

    normalized_name = "".join(
        character
        for character in normalized_name
        if not unicodedata.combining(character)
    )

    return normalized_name.lower().replace(" ", "_")


def find_column(columns, keywords):
    """
    Procura a primeira coluna cujo nome contenha
    uma das palavras-chave informadas.
    """

    for column in columns:
        normalized_column = normalize_column_name(column)

        if any(
            keyword in normalized_column
            for keyword in keywords
        ):
            return column

    return None


def analyze_mode_compatibility(columns, analysis_mode):
    """
    Verifica se o dataset possui variáveis relevantes
    para o contexto químico selecionado.
    """

    identified_columns = {
        "tempo": find_column(
            columns,
            ["tempo", "time"]
        ),
        "concentracao": find_column(
            columns,
            ["concentracao", "concentration"]
        ),
        "absorbancia": find_column(
            columns,
            ["absorbancia", "absorbance"]
        ),
        "ph": find_column(
            columns,
            ["ph"]
        ),
        "condutividade": find_column(
            columns,
            ["condutividade", "conductivity"]
        ),
        "rendimento": find_column(
            columns,
            ["rendimento", "yield"]
        ),
        "lote": find_column(
            columns,
            ["lote", "batch"]
        ),
        "salinidade": find_column(
            columns,
            ["salinidade", "salinity"]
        ),
        "nitrato": find_column(
            columns,
            ["nitrato", "nitrate"]
        ),
        "fosfato": find_column(
            columns,
            ["fosfato", "phosphate"]
        ),
        "temperatura": find_column(
            columns,
            ["temperatura", "temperature"]
        )
    }

    if analysis_mode == "Química Analítica":
        required_variables = [
            "concentracao",
            "absorbancia"
        ]

    elif analysis_mode == "Cinética Química":
        required_variables = [
            "tempo",
            "concentracao"
        ]

    elif analysis_mode == "Controle de Qualidade":
        required_variables = [
            "lote",
            "ph",
            "condutividade",
            "rendimento"
        ]

    elif analysis_mode == "Monitoramento Ambiental":
        required_variables = [
            "ph",
            "condutividade",
            "salinidade",
            "nitrato",
            "fosfato"
        ]

    else:
        required_variables = []

    found_variables = [
        variable
        for variable in required_variables
        if identified_columns.get(variable) is not None
    ]

    missing_variables = [
        variable
        for variable in required_variables
        if identified_columns.get(variable) is None
    ]

    if analysis_mode in [
        "Química Analítica",
        "Cinética Química"
    ]:
        compatible = len(missing_variables) == 0

    else:
        compatible = len(found_variables) >= 2

    return {
        "compatible": compatible,
        "identified_columns": identified_columns,
        "found_variables": found_variables,
        "missing_variables": missing_variables
    }


def suggest_scatter_axes(
    numeric_columns,
    analysis_mode,
    identified_columns
):
    """
    Sugere eixos para o gráfico de dispersão.
    Retorna None quando não existe uma recomendação
    quimicamente clara.
    """

    numeric_columns = list(numeric_columns)

    if analysis_mode == "Cinética Química":
        suggested_x = identified_columns.get("tempo")
        suggested_y = identified_columns.get("concentracao")

    elif analysis_mode == "Química Analítica":
        suggested_x = identified_columns.get("concentracao")
        suggested_y = identified_columns.get("absorbancia")

    else:
        return None, None

    if (
        suggested_x in numeric_columns
        and suggested_y in numeric_columns
        and suggested_x != suggested_y
    ):
        return suggested_x, suggested_y

    return None, None