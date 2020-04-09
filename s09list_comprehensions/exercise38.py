data = [99, 'no data', 95, 94, 'no data']


def clean(d):
    return [value if type(value) == int or type(value) == float else 0 for value in d]


print(clean(data))
