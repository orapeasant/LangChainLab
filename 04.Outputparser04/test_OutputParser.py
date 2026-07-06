from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain.output_parsers import OutputFixingParser
class Book(BaseModel):
    name: str = Field(description="书籍名称")
    year: int = Field(description="出版年份")

llm = ChatOpenAI(
    model="qwen3-0.6b",
    base_url='https://dashscope.aliyuncs.com/compatible-mode/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
parser = JsonOutputParser(pydantic_object=Book)
 
fix_parser = OutputFixingParser.from_llm(parser=parser, llm=llm)

prompt = PromptTemplate(
    template="请帮我从出版列表中解析图书的信息。\n{format_instructions}\n出版列表：{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
#prompt=prompt.invoke({"query":"水浒传出版于1929年。三国演义出版于2002年"})
prompt=prompt.invoke({"query":"你好"})
response=llm.invoke(prompt)
print (response.content)
print ("-"*50)
result=fix_parser.parse(response.content)
print (result)
#转json失败的原因
#1.输出的信息本身和json不相关
#2.模型不够强，转不成