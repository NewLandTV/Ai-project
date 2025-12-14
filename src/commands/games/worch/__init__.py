import ollama
import os
import time

prompt = "너는 한국어 끝말잇기를 잘하는 인공지능이야. 가장 중요한 점은 상대가 입력한 단어의 마지막 글자로 시작해야 해. 또한 두 글자 이상의 단어로 공백없이 붙여 써야만 해. 마지막으로 불필요한 부가 설명을 일절 하지 마."
messages = [{ "role": "system", "content": prompt }]

directory = os.path.dirname(__file__)
program_path = os.path.join(directory, "worch.exe")
word_path = os.path.join(directory, "word.out")

def run():
    print("v0.1.0 WORCH 모듈입니다!")
    
    while True:
        word = input("단어를 입력하세요 : ")
        
        with open(word_path, "w", encoding="utf-8") as file:
            file.write(word)

        # TEST: Python to C
        # TODO: 성능 개선을 위해서 AI가 사전에 있는 단어 중 아무거나 골라 쓰도록 구현하는 것.
        # os.system(f"{program_path} \"{word}\" \"{word_path}\"")
        # if not os.path.exists(word_path):
        #     print("다시 입력해 주세요.")
        #     continue

        time.sleep(1)

        messages.append({ "role": "user", "content": f"{prompt} 단어 : {word}" })
        response = ollama.chat(model="exaone3.5", messages=messages)
        word = response.message.content
        messages.append({ "role": "assistant", "content": word })
        print(f"AI가 입력한 단어 : {word}")

        with open(word_path, "w", encoding="utf-8") as file:
            file.write(word)