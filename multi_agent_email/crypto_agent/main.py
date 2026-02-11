from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from langchain_core.tools import tool
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

class CryptoAgent:
    def __init__(self, model, tools, system=""):
        self.system = system
        graph = StateGraph(AgentState)
        
        graph.add_node("analyst", self.call_openai)
        graph.add_node("action", self.take_action)
        
        graph.add_conditional_edges(
            "analyst",
            self.exists_action,
            {True: "action", False: END}
        )
        graph.add_edge("action", "analyst")
        graph.set_entry_point("analyst")
        
        self.graph = graph.compile()
        self.tools = {t.name: t for t in tools}
        self.model = model.bind_tools(tools)

    def exists_action(self, state: AgentState):
        result = state['messages'][-1]
        return len(result.tool_calls) > 0

    def call_openai(self, state: AgentState):
        messages = state['messages']
        if self.system:
            messages = [SystemMessage(content=self.system)] + messages
        message = self.model.invoke(messages)
        return {'messages': [message]}

    def take_action(self, state: AgentState):
        tool_calls = state['messages'][-1].tool_calls
        results = []
        for t in tool_calls:
            print(f"--- Executando Tool: {t['name']} ---")
            result = self.tools[t['name']].invoke(t['args'])
            results.append(ToolMessage(tool_call_id=t['id'], name=t['name'], content=str(result)))
        return {'messages': results}
    
@tool
def fetch_crypto_prices(coins: list[str]):
    """Busca cotações atuais de criptomoedas como bitcoin e ethereum."""
    
    #Substituir pela chamada da API real, por exemplo CoinGecko ou CoinMarketCap
    mock_data = {
        "bitcoin": {"usd": 70423.30},
        "ethereum": {"usd": 3850.45}
    }
    return {coin.lower(): mock_data.get(coin.lower(), "N/A") for coin in coins}

@tool
def search_crypto_news(query: str):
    """Busca as últimas notícias e tendências do mercado de criptomoedas."""
    # Mock de base de dados de notícias
    mock_news = {
        "bitcoin": "Adoção institucional do Bitcoin cresce com novos ETFs na Ásia. Analistas preveem baixa volatilidade no curto prazo.",
        "ethereum": "Atualização na rede Ethereum reduz taxas de transação significativamente. O ecossistema DeFi mostra sinais de recuperação.",
        "geral": "O mercado cripto aguarda decisões do FED sobre taxas de juros, o que pode impactar ativos de risco."
    }
    
    query_lower = query.lower()
    for key in mock_news:
        if key in query_lower:
            return mock_news[key]
            
    return mock_news["geral"]

def writing_main_langgraph(prompt_system, user_input):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    tools = [fetch_crypto_prices, search_crypto_news] 
    
    bot = CryptoAgent(llm, tools, system=prompt_system)
    
    messages = [HumanMessage(content=user_input)]
    result = bot.graph.invoke({"messages": messages})
    
    return result['messages'][-1].content