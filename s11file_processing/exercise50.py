with open('data.txt', mode='a+') as my_file:
    my_file.seek(0)
    content = my_file.read()
    my_file.seek(0)
    my_file.write(content)
    my_file.write(content)
