def foo(temp):
    if isinstance(temp, int) or isinstance(temp, float):
        if temp > 7:
            return "Warm"
        else:
            return "Cold"


print(foo(10))
print(foo(7))
print(foo(5))
