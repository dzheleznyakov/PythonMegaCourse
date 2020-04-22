import time

# sys.builtin_module_names

while True:
    with open('files/vegetables.txt') as file:
        print(file.read().strip())
    time.sleep(10)
