def mean(value):
    if isinstance(value, dict):
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


print(
    mean([1, 4, 5])
)

print(
    mean({"Marry": 9.1, "Sim": 8.8, "John": 7.5})
)
