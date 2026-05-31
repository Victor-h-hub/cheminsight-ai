import streamlit as st
import os

from dotenv import load_dotenv
from google import genai


# ---------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# ---------------------------------------------------
# GERAÇÃO DE INSIGHTS COM IA
# ---------------------------------------------------

@st.cache_data
def generate_ai_insights(summary: str, columns: list, shape: tuple) -> str:

    # Verifica se a chave existe
    if not api_key:

        return """
        Chave da API Gemini não configurada.

        Verifique o arquivo .env.
        """

    # Prompt enviado para IA
    prompt = f"""
    Você é um analista de dados especializado em análise exploratória.

    Analise o dataset abaixo e gere insights:

    - claros;
    - organizados;
    - objetivos;
    - profissionais;
    - em português.

    Informações do dataset:
    - Dimensão do dataset: {shape}
    - Colunas disponíveis: {columns}

    Estatísticas:
    {summary}

    Estruture sua resposta em tópicos:

    1. Visão geral dos dados
    2. Padrões identificados
    3. Tendências ou comportamentos relevantes
    4. Possíveis interpretações de negócio
    5. Observações importantes
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return """
        Não foi possível gerar insights com IA no momento.

        Possíveis causas:
        - limite da API gratuita atingido;
        - instabilidade temporária da API;
        - erro de conexão.
        """