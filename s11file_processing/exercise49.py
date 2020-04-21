with open('bear1.txt') as bear1_file:
    bear1_content = bear1_file.read()

with open('bear2.txt', mode='a') as bear2_file:
    bear2_file.write(' ' + bear1_content)
