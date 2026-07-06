from langchain.memory import ChatMessageHistory 
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_openai import ChatOpenAI

from langchain.prompts import ChatPromptTemplate
from langchain.storage import InMemoryStore

llm=ChatOpenAI(
    model="llama3.1",
    base_url="https://llm.adirontechs.com/v1",
    api_key="asdfsa",
    max_tokens=12345
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("placeholder", "{chat_history}"),
    ("human", "{human_input}")
])

chain = prompt | llm

chat_chain = RunnableWithMessageHistory(
    chain,
    lambda session_id: ChatMessageHistory(store=InMemoryStore())    ,
    input_messages_key="human_input",
    history_message_key="chat_history"
)
session_id = "Alex Chat 001"


while True:
    query=input("question:")
    result = chat_chain.invoke({"human_input":query},config={"configurable":{"session_id":session_id}})
    print(result)