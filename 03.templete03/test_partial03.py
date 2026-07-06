from datetime import datetime
from langchain.prompts import PromptTemplate
def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}", 
    #input_variables=["adjective", "date"]
)
partial_prompt = prompt.partial(date="三")
print(partial_prompt.format(adjective="funny"))