from dotenv import load_dotenv
import os
from openai import OpenAI, api_key

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
org_id = os.getenv("OPENAI_ORG_ID")
project_id = os.getenv("OPENAI_PROJECT_ID")
    
def openia_simple_request():
    if api_key:
        client = OpenAI(api_key=api_key, organization=org_id, project=project_id)
        print("\n🚀 Enviando requisição de teste...")
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Diga 'Olá Mundo', Xurusbaga XurusBago!"}],
        )
        print("Resposta da API:", completion.choices[0].message.content)
    else:
        print("\n❌ Falha: variável OPENAI_API_KEY não encontrada no .env")


if __name__ == "__main__":
    openia_simple_request()