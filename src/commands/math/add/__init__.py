import os
import subprocess

directory = os.path.dirname(__file__)
program_path = os.path.join(directory, "add.exe")

def run():
    print("v1.0.0 This is math.add(a, b) = result module!")
    subprocess.run([program_path])