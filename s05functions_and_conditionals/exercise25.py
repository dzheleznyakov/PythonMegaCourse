def fun(param):
    if isinstance(param, str):
        if len(param) < 8:
            return False
        else:
            return True;


print(fun("mypass"))
print(fun("mylongpassword"))
