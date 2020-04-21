with open('vegetables.txt', mode='a+') as my_file:
    my_file.write('\nokra')
    my_file.seek(0)
    content = my_file.read()

print(content)
