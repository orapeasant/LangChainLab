from datetime import datetime
from langchain_core.prompts import PromptTemplate
def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

# 直接定义模板.
prompt_template = PromptTemplate(template="今天的日期是 {date}，天气是 {wheather}",partial_variables={"date": _get_datetime})
result=prompt_template.invoke({"wheather": "小雨"})
print (result)
