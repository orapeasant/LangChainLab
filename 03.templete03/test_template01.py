from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="qwen3",
    base_url='https://llm.adirontechs.com/v1',
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1"
)
# 模板定义
#构建模板的两种方法
prompt_template = PromptTemplate.from_template("{{你好}},今天是星期{day}，后天是星期几?")
 
#prompt_template=PromptTemplate(input_variables=['day'], template='今天是星期{day}，后天是星期几')
#模板变成字符串
print (prompt_template)
prompt_string=prompt_template.invoke({"day": "三"})
print (prompt_string)
#模板本身不输入大模型，是通过模板invoke的字符串，输入给大模型
result=llm.invoke(prompt_string)
print (result)