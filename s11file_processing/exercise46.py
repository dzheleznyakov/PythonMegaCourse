def count_occurrences(char, file_path):
    file = open(file_path)
    content = file.read()
    file.close()
    return content.count(char)


res = count_occurrences('a', 'bear.txt')
print(res)
