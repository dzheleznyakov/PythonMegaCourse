file = open('bear.txt')
content = file.read()
file.close()
print(content[:90])
