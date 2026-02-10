import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage

# Import shared OpenAI helper. Support running as script or as package.
try:
    from multi_agent_email.openai_agent import get_completion, styles, tones, get_today_str, llm_model
except Exception:
    import sys, os
    pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if pkg_root not in sys.path:
        sys.path.insert(0, pkg_root)
    from openai_agent import get_completion, styles, tones, get_today_str, llm_model

customer_input = """\
Olá, gostaria de receber informações sobre as cotações atuais das criptomoedas, especialmente Bitcoin e Ethereum.
Além disso, estou interessado em entender melhor as oportunidades e riscos de investimento nesse mercado. Agradeço desde já pela ajuda!
"""

@tool
def fetch_crypto_prices(coins: list[str]):
    """Busca cotações atuais de criptomoedas como bitcoin e ethereum."""
    
    #Substituir pela chamada da API real, por exemplo CoinGecko ou CoinMarketCap
    mock_data = {
        "bitcoin": {"usd": 70423.25},
        "ethereum": {"usd": 3850.45}
    }
    return {coin.lower(): mock_data.get(coin.lower(), "N/A") for coin in coins}

def writing_main(prompt_task: str):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    llm_with_tools = llm.bind_tools([fetch_crypto_prices])
    
    messages = [
        SystemMessage(content=prompt_task),
        HumanMessage(content=customer_input)
    ]
    
    ai_msg = llm_with_tools.invoke(messages)
    
    if ai_msg.tool_calls:
        messages.append(ai_msg)
        for tool_call in ai_msg.tool_calls:
            
            tool_output = fetch_crypto_prices.invoke(tool_call["args"])
            
            messages.append({
                "role": "tool",
                "content": str(tool_output),
                "tool_call_id": tool_call["id"]
            })
        
        final_response = llm_with_tools.invoke(messages)
        return final_response.content

    return ai_msg.content