import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("Chave carregada?", api_key is not None)
print("Tamanho da chave:", len(api_key) if api_key else 0)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explique em 3 linhas o que é análise de dados."
)

print(response.text)