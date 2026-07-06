from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage

#建立远程访问的大模型
llm = ChatOpenAI(
    model="qwen2.5",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
#SystemMessage：大模型的人设，通过提示词的方式实现
#HumanMessage ：用户的问题
# messages1 = [
#     SystemMessage(content="请你作为我的物理课助教，用通俗易懂且间接的语言帮我解释物理概念。"),
#     HumanMessage(content="什么是波粒二象性？"),
# ]
messages2 = [
    {"role": "system", "content": "请你作为我的物理课助教，用通俗易懂且间接的语言帮我解释物理概念。"},
    {"role": "user", "content": "什么是波粒二象性？"}
]
 
response = llm.invoke(messages2,temperature=0.5,max_tokens=200)
print (type(response))
print (response)

# temperature=0.5,  # 调整温度参数,温度越高，模型输出的多样性越强
# max_tokens=200    # 限制最大生成长度
