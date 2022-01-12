def weather_condition(temp):
    if temp > 25:
        return "Hot"
    elif 15 <= temp <= 25:
        return "Warm"
    else:
        return "cold"

user_input = float(input("Enter temperature:"))

print(weather_condition(user_input), user_input)

#elif instead of else if

#python converts user input to a string, so you have to convert it into the data type that you want

#it's better to use "isinstance(num, int)" instead of type(num) == int
