def greet(person):
    if isinstance(person, str):
        if len(person) > 0:
            first = person[0].upper()
        else:
            first = ""
        if len(person) > 1:
            name = first + person[1:]
        else:
            name = first
        return "Hi %s" % name


print(greet("mary"))
