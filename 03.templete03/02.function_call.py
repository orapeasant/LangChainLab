from datetime import datetime
from langchain_core.prompts import PromptTemplate

def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")


prompt_template=PromptTemplate(template="today is {date}, weather is {weather}",partial_variables={"date":_get_datetime})

result=prompt_template.invoke({"weather":"rainy"})

print(result)