from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage
from transformers import AutoTokenizer  


m1=HumanMessage(content="as a physics ta, please use simple language to explain physics concept")

m2=HumanMessage(content="what is eletronicmagnet")
print(m1.pretty_repr()) 

