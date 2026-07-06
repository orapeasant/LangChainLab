from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)


template = """You are a chatbot having a conversation with a human. Please answer as briefly as possible.

{chat_history}
Human: {human_input}
Chatbot:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"], template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    memory=memory,
)
while True: 
    query = input("请输入问题: ")
    result=llm_chain.predict(human_input=query )
    print (result)
