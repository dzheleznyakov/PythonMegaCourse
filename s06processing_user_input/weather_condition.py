def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


user_input = float(input("Enter temperature: "))
print(type(user_input), user_input)
print(weather_condition(user_input))
