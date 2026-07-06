from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer
llm = ChatOpenAI(
    model="qwen3",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
messages1 = [
    HumanMessage(content="什么是波粒二象性？"),
]
messages2 = [
    HumanMessage(content="你好，你是谁"),
]
 
response = llm.batch([messages1,messages2])
print (response)