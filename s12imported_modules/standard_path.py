import time
import os

# sys.builtin_module_names

while True:
    if os.path.exists("files/vegetables.txt"):
        with open('files/vegetables.txt') as file:
            print(file.read().strip())
    else:
        print("File does not exists.")
    time.sleep(10)
