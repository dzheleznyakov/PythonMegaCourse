monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures)

monday_temperatures.append(8.1)
print(monday_temperatures)

monday_temperatures.clear()
print(monday_temperatures)


monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures)
print(monday_temperatures.index(8.8))
# print(monday_temperatures.index(8.8, 2))

print(monday_temperatures.__getitem__(1))
print(monday_temperatures[1])
