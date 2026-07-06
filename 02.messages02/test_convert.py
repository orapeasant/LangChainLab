from langchain_openai import ChatOpenAI
from langchain.schema.messages import HumanMessage, SystemMessage,AIMessage,ToolMessage
from transformers import AutoTokenizer
from langchain_core.messages.utils import convert_to_openai_messages
messages = [
                SystemMessage([{"type": "text", "text": "foo"}]),
                {"role": "user", "content": [{"type": "text", "text": "whats in this"}, {"type": "image_url", "image_url": {"url": "data:image/png;base64,'/9j/4AAQSk'"}}]},
                AIMessage("", tool_calls=[{"name": "analyze", "args": {"baz": "buz"}, "id": "1", "type": "tool_call"}]),
                ToolMessage("foobar", tool_call_id="1", name="bar"),
                {"role": "assistant", "content": "thats nice"},
            ]
oai_messages = convert_to_openai_messages(messages)
print (oai_messages)