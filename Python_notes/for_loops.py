#rounding
monday_temperatures = [9.1, 8.8, 7.6]

#without for loop
#print(round(monday_temperatures[0]))
#print(round(monday_temperatures[1]))
#print(round(monday_temperatures[2]))


#temperature is a variable name for whatever values are in the array/list
for temperature in monday_temperatures:
    print(round(temperature))
    print("Done")

#similar method can work for other values
for letter in 'hello':
    print(letter.title())

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.values(): #values give you the number, key give you the names, and items gives you both
    print (grades) # print (f) is like toString in Java