data = [99, 'no data', 95, 94, 'no data']


def clean(d):
    return [value for value in d if type(value) == int or type(value) == float]


print(clean(data))
