from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
)

prompt = input("Informe sua pergunta: ")

resposta = llm.invoke(prompt)
print(resposta.content)
