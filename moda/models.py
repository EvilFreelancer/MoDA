import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, GenerationConfig
from peft import PeftModel


def load_model(config):
    quantization_config = BitsAndBytesConfig(
        load_in_8bit=config['load_in_8bit'] if 'load_in_8bit' in config else False,
        load_in_4bit=config['load_in_4bit'] if 'load_in_4bit' in config else False,
        llm_int8_enable_fp32_cpu_offload=True
    )
    model = AutoModelForCausalLM.from_pretrained(config['name'], quantization_config=quantization_config)
    tokenizer = AutoTokenizer.from_pretrained(config['name'], use_fast=False)
    return model, tokenizer


def load_adapter(base_model, adapter_name):
    model = PeftModel.from_pretrained(base_model, adapter_name)
    tokenizer = AutoTokenizer.from_pretrained(adapter_name, use_fast=False)
    return model, tokenizer


def get_input_ids(tokenizer, messages):
    return tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True,
        return_tensors="pt"
    )


def get_adapter(name, adapters) -> str | bool:
    for adapter in adapters:
        if adapter["name"] == name:
            return adapter
    return False


def get_terminators(tokenizer):
    return [
        tokenizer.eos_token_id,
        # tokenizer.convert_tokens_to_ids("<|endoftext|>"),
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]


def get_prompt(messages):
    custom_messages = [
        f"{message['role'].upper()}:\n{message['content']}"
        for message in messages
    ]
    custom_messages = "\n\n".join(custom_messages)
    custom_messages += '\n\nASSISTANT:'
    return custom_messages


def trigger_model(input_ids, terminators, model, tokenizer):
    outputs = model.generate(
        input_ids,
        max_new_tokens=1024,
        eos_token_id=terminators,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.6,
        top_p=0.9,
        top_k=20,
    )
    response = outputs[0][input_ids.shape[-1]:]
    return tokenizer.decode(response, skip_special_tokens=True)


def trigger_pipeline(inputs, base_model, peft_model, tokenizer):
    pipeline = transformers.pipeline(
        "text-generation",
        model=base_model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )
    pipeline.model = peft_model
    sequences = pipeline(
        inputs,
        max_length=1024,
        do_sample=True,
        top_k=10,
        temperature=0.2,
        top_p=0.5,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )
    return sequences
