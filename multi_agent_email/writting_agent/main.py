import os
import openai
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

llm_model = "gpt-4o-mini"

client = openai.OpenAI()

styles = ["formal and technical", "casual and friendly", "enthusiastic and persuasive", "concise and to the point", "storytelling and engaging"]
tones = ["confident", "empathetic", "urgent", "optimistic", "serious"]

customer_email = """
Crie um email para um cliente corporativo apresentando nossa solução
de visão computacional para inspeção industrial. O estilo deve ser
formal e técnico, com tom confiante e persuasivo. Inclua um CTA para
agendar uma demonstração.
"""

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

def get_today_str() -> str:
    """Get current date in a human-readable format."""
    dt = datetime.now()
    return f"{dt.strftime('%a %b')} {dt.day}, {dt.year}"


def writting_main(reflection: str):
    prompt_formatted = reflection.format(customer_email=customer_email, style=styles[0], tone=tones[0], date=get_today_str())
    print(get_completion(prompt_formatted))
    return prompt_formatted