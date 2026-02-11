from .reflection_agent.main import reflection_main
from .crypto_agent.main import writing_main_langgraph
from .appraisal_agent.main import appraisal_agent


customer_input = """\
Olá, gostaria de receber informações sobre as cotações atuais das criptomoedas, somente do bitcoin.
Além disso, estou interessado em entender melhor as oportunidades e riscos de investimento nesse mercado. Agradeço desde já pela ajuda!
Também gostaria de saber novidades sobre o bitcoin, poderia criar uma sessão de News?
"""

def main():
    # Engenharia de Contexto
    reflection_prompt = reflection_main() 
    
    print("--- Iniciando Agente de Escrita (LangGraph) ---")
    
    # 2. Chamando Agent Reativo de Escrita (LangGraph)
    email = writing_main_langgraph(reflection_prompt, customer_input)
    
    print("\n--- E-mail Gerado ---")
    print(email)
    
    # 3. Avaliação final
    print("\n--- Iniciando Avaliação ---")
    appraisal = appraisal_agent(email)
    print(appraisal)