 
 

import os
#这个包就是阿里云的
import dashscope

messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': '你是谁？'}
    ]
response = dashscope.Generation.call(
    api_key="sk-0baadaecdc344279af4efb46d9ff0ba1",
    model="qwen2.5-32b-instruct",  
    messages=messages,
    result_format='message'
    )
print(response)