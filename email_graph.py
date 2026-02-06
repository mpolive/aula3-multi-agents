from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

class EmailState(TypedDict):
    tema: str
    tom: str
    plano: str
    email: str
    avaliacao: str
    aprovado: bool
    historico: list


def agente_reflexao(state: EmailState):

    prompt = f"""
Analise o pedido e crie um plano para o email:

TEMA: {state['tema']}
TOM: {state['tom']}

Retorne:
- objetivo
- público
- tom e estilo
- pontos obrigatórios
"""
    r = llm.invoke([HumanMessage(content=prompt)])

    state["historico"].append(("Reflexão", r.content))
    return {"plano": r.content}


def agente_escrita(state: EmailState):

    prompt = f"""
Com base neste plano:

{state['plano']}

Escreva o email seguindo o tom: {state['tom']}
"""
    r = llm.invoke([HumanMessage(content=prompt)])

    state["historico"].append(("Escrita", r.content))
    return {"email": r.content}


def agente_avaliacao(state: EmailState):

    prompt = f"""
Avalie este email:

{state['email']}

Responda:

APROVADO: sim ou nao
JUSTIFICATIVA:
VERSAO_SUGERIDA:
"""
    r = llm.invoke([HumanMessage(content=prompt)])

    aprovado = "aprovado: sim" in r.content.lower()

    state["historico"].append(("Avaliação", r.content))

    return {
        "avaliacao": r.content,
        "aprovado": aprovado
    }


def precisa_reescrever(state):
    return "escrita" if not state["aprovado"] else "fim"


def criar_app():

    workflow = StateGraph(EmailState)

    workflow.add_node("reflexao", agente_reflexao)
    workflow.add_node("escrita", agente_escrita)
    workflow.add_node("avaliacao", agente_avaliacao)

    workflow.set_entry_point("reflexao")

    workflow.add_edge("reflexao", "escrita")
    workflow.add_edge("escrita", "avaliacao")

    workflow.add_conditional_edges(
        "avaliacao",
        precisa_reescrever,
        {"escrita": "escrita", "fim": "__end__"}
    )

    return workflow.compile()