import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

llm_model = "gpt-4o-mini"

client = openai.OpenAI()

styles = ["formal and technical", "casual and friendly", "enthusiastic and persuasive", "concise and to the point", "storytelling and engaging"]
tones = ["confident", "empathetic", "urgent", "optimistic", "serious"]

def get_completion(prompt, model=llm_model):
    messages = [
        {
        "role": "user",
        "content": prompt
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )

    return response.choices[0].message.content


def appraisal_agent(email: str) -> str:
    prompt = f"""
    Avalie o seguinte email:
    {email}
    
    Forneça uma avaliação técnica e construtiva sobre o conteúdo, estilo e tom do email.
    Também de uma nota de 1 a 10 sobre a clareza, profissionalismo e adequação ao público-alvo.
    """
    appraisal = get_completion(prompt)
    return appraisal