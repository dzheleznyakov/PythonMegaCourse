data = ['1.2', '2.6', '3.3']


def convert(d):
    return sum([float(v) for v in d])


print(convert(data))
