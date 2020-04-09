temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
print(new_temps)

new_temps2 = [temp / 10 for temp in temps]
print(new_temps2)
