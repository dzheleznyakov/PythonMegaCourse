def foo(param):
    if isinstance(param, int) or isinstance(param, float):
        if param > 25:
            return 'Hot'
        elif 15 <= param <= 25:
            return 'Warm'
        else:
            return 'Cold'


print(foo(10))
print(foo(15))
print(foo(16))
print(foo(25))
print(foo(26))
