from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

llm=ChatOpenAI(
    model="qwen3",
    base_url="https://llm.adirontechs.com/v1",
    api_key="sf"
)
message1=[
    {"role":"system","content":"as a physics ta, please use simple langauge to explain physics concept"},
    {"role":"user","content":"what is tesla"} 
]
message2=[
    {"role":"system","content":"as a physics ta, please use simple langauge to explain physics concept"},
    {"role":"user","content":"what is eletronicmagnet"} 
]

#response=llm.invoke(message2,temperature=0.5, max_tokens=200)
response = llm.batch([message1,message2])
print(type(response))
print(response)

