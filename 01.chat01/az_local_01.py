from transformers import AutoModelForCausalLM, AutoTokenizer

model_name= "D:/aiml/llm/Qwen2.5-7B-Instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code = True
)

tokenizer= AutoTokenizer.from_pretrained(model_name)

messages = [
    {"role":"system", "content":"as a physics TA, please easy language to explain physics concept"},
    {"role":"user","content":"what is eletromagnet?"}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

model_inputs=tokenizer([text],return_tensors="pt").to(model.device)

generated_ids=model.generate(
    **model_inputs,
    max_new_tokens=23432
)
generated_ids=[
    output_ids[len(input_ids):] for input_ids,output_ids in zip(model_inputs.input_ids,generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print("output",response)