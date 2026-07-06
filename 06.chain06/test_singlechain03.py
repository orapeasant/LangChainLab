from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)



human_message_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template="给一个 {product} 取一个好听的公司名字?",
        input_variables=["product"],
    )
)

chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
 
chain =chat_prompt_template|llm
print(chain.invoke("人工智能教育公司"))



 