def generate_chemical_insights(df):    
    insights = []

    insights.append(
        f"O dataset possui {df.shape[0]} linhas e "
        f"{df.shape[1]} colunas."
    )

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_columns) == 0:
        insights.append(
            "Nenhuma variável numérica foi identificada "
            "para análise estatística."
        )
        return insights

    # ------------------------------------------------
    # RESUMO ESTATÍSTICO
    # ------------------------------------------------

    for column in numeric_columns:

        mean_value = df[column].mean()
        min_value = df[column].min()
        max_value = df[column].max()

        insights.append(
            f"'{column}': média = {mean_value:.2f}, "
            f"mínimo = {min_value:.2f} e "
            f"máximo = {max_value:.2f}."
        )

    # ------------------------------------------------
    # IDENTIFICAÇÃO DE COLUNAS QUÍMICAS
    # ------------------------------------------------

    normalized_columns = {
        column: column.lower()
        for column in numeric_columns
    }

    def find_column(keywords):
        for original_name, normalized_name in normalized_columns.items():
            if any(
                keyword in normalized_name
                for keyword in keywords
            ):
                return original_name

        return None

    time_column = find_column(
        ["tempo", "time"]
    )

    concentration_column = find_column(
        ["concentracao", "concentração", "concentration"]
    )

    absorbance_column = find_column(
        ["absorbancia", "absorbância", "absorbance"]
    )

    ph_column = find_column(
        ["ph"]
    )

    # ------------------------------------------------
    # REGRA DE CINÉTICA QUÍMICA
    # ------------------------------------------------

    if time_column and concentration_column:

        valid_data = df[
            [time_column, concentration_column]
        ].dropna().sort_values(time_column)

        if len(valid_data) >= 2:

            initial_concentration = (
                valid_data[concentration_column].iloc[0]
            )

            final_concentration = (
                valid_data[concentration_column].iloc[-1]
            )

            correlation = valid_data[
                [time_column, concentration_column]
            ].corr().iloc[0, 1]

            if final_concentration < initial_concentration:
                insights.append(
                    "A concentração diminui ao longo do tempo, "
                    "indicando consumo progressivo da espécie "
                    "monitorada durante o experimento."
                )

            elif final_concentration > initial_concentration:
                insights.append(
                    "A concentração aumenta ao longo do tempo, "
                    "o que pode ser compatível com a formação "
                    "progressiva de uma espécie química."
                )

            insights.append(
                f"A correlação entre '{time_column}' e "
                f"'{concentration_column}' é {correlation:.3f}. "
                "Esse valor descreve a associação entre as variáveis, "
                "mas não determina sozinho a ordem ou o mecanismo "
                "da reação."
            )

    # ------------------------------------------------
    # REGRA DE QUÍMICA ANALÍTICA
    # ------------------------------------------------

    if concentration_column and absorbance_column:

        valid_data = df[
            [concentration_column, absorbance_column]
        ].dropna()

        if len(valid_data) >= 2:

            correlation = valid_data[
                [concentration_column, absorbance_column]
            ].corr().iloc[0, 1]

            insights.append(
                f"A correlação entre concentração e absorbância "
                f"é {correlation:.3f}."
            )

            if correlation >= 0.95:
                insights.append(
                    "Os dados apresentam forte associação linear "
                    "positiva entre concentração e absorbância, "
                    "compatível com a construção de uma curva "
                    "analítica. A confirmação da Lei de Beer-Lambert "
                    "exige regressão, avaliação dos resíduos e "
                    "informações experimentais adicionais."
                )

    # ------------------------------------------------
    # VALIDAÇÃO BÁSICA DE pH
    # ------------------------------------------------

    if ph_column:

        invalid_ph = df[
            (df[ph_column] < 0)
            | (df[ph_column] > 14)
        ]

        if len(invalid_ph) > 0:
            insights.append(
                f"Foram encontrados {len(invalid_ph)} valores de pH "
                "fora do intervalo convencional de 0 a 14. "
                "Verifique unidade, calibração ou registro dos dados."
            )
        else:
            insights.append(
                "Todos os valores de pH estão dentro do intervalo "
                "convencional de 0 a 14."
            )

    return insights