import os
from http import HTTPStatus
#from dashscope import Application
from openai import OpenAI
###
#OpenAI标准接口访问-
###
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",-*
    api_key="sk-6790bcf8821e466bb015d5d297c413d4", 
    base_url="https://llm.adirontechs.com/v1",
)

# role 字段用来定义消息的发送者角色，具体包括三种选择：system、user、和 assistant。

# system（系统）:通常用于设置聊天的上下文或者提供系统级别的指示和配置信息。
# user（用户）:代表实际的用户输入，即用户向聊天系统提出的问题或者发起的对话内容。
# assistant（助手）:代表智能助手的回复或者动作，是模型根据用户输入给出的响应。
messages=[
        {'role': 'system', 'content': '请你作为我的物理课助教，用通俗易懂且间接的语言帮我解释物理概念。'},
        {'role': 'user', 'content': '什么是波粒二象性？'}]
 
# frequency_penalty-介于 -2.0 和 2.0 之间的数字。到目前为止，正值会根据新标记在文本中的现有频率来惩罚新标记，从而降低模型逐字重复同一行的可能性。
# temperature-用于控制随机性和多样性的程度,介于 0 和 2 之间。较高的值（如 0.8）将使输出更加随机，而较低的值（如 0.2）将使其更具集中性和确定性。
 
completion = client.chat.completions.create(
    #model="qwen2.5",  
    model="llama3.1",  
    messages=messages
    )
print(completion.model_dump_json())

 