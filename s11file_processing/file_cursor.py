my_file = open('fruits.txt')
print(my_file.read())
print('--------')
print(my_file.read())
print('++++++++')

my_file = open('fruits.txt')
content = my_file.read()
my_file.close()
print(content)
print('--------')
print(content)

