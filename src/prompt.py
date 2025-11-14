import os

def get_prompt_info(name="prompt.txt"):
    if not os.path.exists(name):
        return None
    with open(name, "r", encoding="utf-8") as f:
        prompt = f.read()
    return prompt