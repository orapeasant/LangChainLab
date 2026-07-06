from datetime import datetime
from langchain.prompts import PromptTemplate


def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

prompt=PromptTemplate(
    template="tell me a {adjective} joke about the day {date}",
)
#partial_prompt=prompt.partial(date="Wedsnesday")
print(prompt.format(adjective="funny",date="Wedsnesday"))

print(prompt.partial())