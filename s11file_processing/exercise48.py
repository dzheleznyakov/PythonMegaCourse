with open('bear.txt') as bear_file:
    content = bear_file.read()

with open('first.txt', mode='w') as first_file:
    first_file.write(content[:90])
