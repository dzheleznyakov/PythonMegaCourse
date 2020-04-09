def process(*args):
    l = [s.upper() for s in list(args)]
    return sorted(l)


print(process('snow', 'glacier', 'iceberg'))
