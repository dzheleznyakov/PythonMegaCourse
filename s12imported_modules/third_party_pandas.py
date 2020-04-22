import time
import os
import pandas

# sys.builtin_module_names

while True:
    if os.path.exists("files/temps_today.csv"):
        with open('files/temps_today.csv') as file:
            data = pandas.read_csv('files/temps_today.csv')
            print(data.mean())
            print(dir(type(data)))
    else:
        print("File does not exists.")
    time.sleep(10)
