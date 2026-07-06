from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的助手，能准确回答各种问题。"),
    ("human", "{question}")
])
def extract_answer(response):
    return response.content
#构建大模型
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
#prompt.invoke({"question":"你好，你是谁"})->大模型
#方法1
#如果是管道格式 X|Y
#默认Y会调用invoke函数
#invoke是个特殊的函数
#大模型，提示词模板 都有
chain={"question": lambda x: x}| prompt|llm|extract_answer 
result=chain.invoke("你好，你是谁")
print (result)

# #方法2
#output_key 输出对应的字段名
# chain = LLMChain(llm=llm, prompt=prompt, output_key="回答")
# result=chain.invoke("你好，你是谁")
# print (result)
