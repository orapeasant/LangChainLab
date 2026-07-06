from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)

prompt1 = PromptTemplate(
    input_variables=["product"],
    template="给一个生产 {product} 取一个好听的公司名字?",
)
chain_1 = prompt1|llm 
#第一个大模型输出的是：  耐克  

prompt2 = PromptTemplate(
    input_variables=["product","product2"],
    template="给一个生产 {product} 取一个响亮的公司口号?",
)

chain_2 =prompt2|llm   

overall_chain =chain_1|chain_2
#等价于
#prompt1|llm|prompt2|llm       
catchphrase = overall_chain.invoke({"product":"花衬衣"})
print(catchphrase)