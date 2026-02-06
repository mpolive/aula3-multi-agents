from langchain.chat_models import ChatOpenAI
from langchain.chains import SequentialChain


from config.settings import MODEL_NAME, TEMPERATURE
from agents.reflection import build_reflection_agent
from agents.writing import build_writing_agent
from agents.evaluation import build_evaluation_agent




def main():
llm = ChatOpenAI(
model=MODEL_NAME,
temperature=TEMPERATURE
)


reflection_chain = build_reflection_agent(llm)
writing_chain = build_writing_agent(llm)
evaluation_chain = build_evaluation_agent(llm)


pipeline = SequentialChain(
chains=[
reflection_chain,
writing_chain,
evaluation_chain
],
input_variables=["input"],
output_variables=["final_output"],
verbose=True
)


user_input = "Escreva um e-mail para um cliente informando atraso na entrega de um projeto."


result = pipeline.run({"input": user_input})
print("\n📧 Resultado Final:\n")
print(result)




if __name__ == "__main__":
main()