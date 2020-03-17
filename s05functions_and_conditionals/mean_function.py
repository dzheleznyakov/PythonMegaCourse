def mean(my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean


print(
    mean([1, 4, 5])
)

print(type(mean), type(sum))
