import os

directory = os.path.dirname(__file__)
program_path = os.path.join(directory, "worch.exe")

def run():
    print("v0.1.0 WORCH 모듈입니다!")

    word = input("단어를 입력하세요. ")
    
    os.system(f"{program_path} {word}")