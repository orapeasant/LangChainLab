import os
from http import HTTPStatus
from openai import OpenAI

client=OpenAI(
    api_key="adfasf",
    base_url="https://llm.adirontechs.com/v1"
)

messages=[
    {"role":"system","content":"as a physics TA, please use simple language to explain physics concept"},
    {"role":"user","content":"what is eletronicmagnet"}
]


completion=client.chat.completions.create(
    model="qwen3",
    messages=messages
)

print(completion.model_dump_json())