from langchain_core.prompts import ChatPromptTemplate

prompt_template=ChatPromptTemplate([
    ("system","you are my private assistant"),
    ("user","today is {date}")
    ]
)   

print(prompt_template)

print("-"*20)

result=prompt_template.invoke({"date":"Wednesday"})
print(result)