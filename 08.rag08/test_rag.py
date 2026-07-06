import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from starlette.middleware.cors import CORSMiddleware
from langchain_community.embeddings import DashScopeEmbeddings
import pickle
#初始化Dashscope Embeddings
embeddings =DashScopeEmbeddings(
    model="text-embedding-v1",
    dashscope_api_key="sk-6790bcf8821e466bb015d5d297c413d4",
)
 
llm = ChatOpenAI(
    model="qwen2.5-32b-instruct",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)

# 加载文档,可换成PDF、txt、doc等其他格式文档
loader = TextLoader('金庸-天龙八部.txt', encoding='utf-8')
documents = loader.load()
 
text_splitter = RecursiveCharacterTextSplitter.from_language(language="markdown", chunk_size=200, chunk_overlap=0)
texts = text_splitter.create_documents(
    [documents[0].page_content]
)
 
# 选择向量模型，并灌库
# db = FAISS.from_documents(texts, embeddings)
# with open("my_db","wb") as f:
#     pickle.dump(db,f)
with open("my_db","rb") as f:
    db=pickle.load(f)
# 获取检索器，选择 top-2 相关的检索结果
retriever = db.as_retriever(search_kwargs={"k": 2})

# 创建带有 system 消息的模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """你是一个对接问题排查机器人。
               你的任务是根据下述给定的已知信息回答用户问题。
               确保你的回复完全依据下述已知信息。不要编造答案。
               请用中文回答用户问题。

               已知信息:
               {context} """),
    ("user", "{question}")
])

# 自定义的提示词参数
chain_type_kwargs = {
    "prompt": prompt_template,
}

# 定义RetrievalQA链
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # 使用stuff模式将上下文拼接到提示词中
    chain_type_kwargs=chain_type_kwargs,
    retriever=retriever,
    return_source_documents=True
)
response=qa_chain({"query": "介绍下乔峰"})
print (response)
print(response["result"])

# 如果需要，可以查看源文档
print(response["source_documents"])