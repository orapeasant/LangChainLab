from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "D:/aiml/llm/Qwen2.5-7B-Instruct"
#加载模型
model = AutoModelForCausalLM.from_pretrained(
     model_name,
    torch_dtype="auto",
    device_map="auto", trust_remote_code=True
)
#加载分词器
tokenizer = AutoTokenizer.from_pretrained(model_name)
#用户输入
messages = [
    {"role": "system", "content": "请你作为我的物理课助教，用通俗易懂且间接的语言帮我解释物理概念。"},
    {"role": "user", "content": "什么是波粒二象性？"}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
 
#分词
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
print ("aa",model_inputs)
tokens_11 = tokenizer.decode([11])
tokens_332 = tokenizer.decode([332])

print("Token for ID 11:", tokens_11)  # Output: "token_for_id_11"
print("Token for ID 332:", tokens_332)  # Output: "token_for_id_332"
#大模型运行
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
#输入+输出
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
#大模型 id进，id出
#解码，id变成字符
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print("输出",response)
 