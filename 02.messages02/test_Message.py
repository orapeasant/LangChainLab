from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer
 

m1=HumanMessage(content="请你作为我的物理课助教，用通俗易懂且间接的语言帮我解释物理概念。")
m2=HumanMessage(content="什么是波粒二象性？")
print (m1.pretty_repr())
 