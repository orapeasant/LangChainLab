from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer
llm = ChatOpenAI(
    model="llama3.1",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
#默认会把"你好"转为 
#HumanMessage(content="你好"),
response_list = llm.stream("你好",stream_usage=True)
for response in response_list:
    print (response)