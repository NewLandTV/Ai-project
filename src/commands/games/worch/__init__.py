import os

directory = os.path.dirname(__file__)
program_path = os.path.join(directory, "worch.exe")
word_path = "word.txt"

def run():
    print("v0.1.0 WORCH 모듈입니다!")
    
    while True:
        word = input("단어를 입력하세요. ")
        
        os.system(f"{program_path} {word}")
        if not os.path.exists(word_path):
            print("다시 입력해 주세요.")
            continue

        with open(word_path, "r", encoding="utf-8") as file:
            word = file.read()

        print(f"AI가 입력한 단어 : {word}")