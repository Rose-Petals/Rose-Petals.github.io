monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "JOhn": 7.5}

#dir(___) gives you the attributes/things you can do with that object
#some methods like print() and mean() won't show up in dir() because they are methods and don't need the () at the end
#use dir(__builtins__) to find all built in functions

mySum = sum(student_grades.values())
length = len(student_grades)
mean = mySum/length
print(mean)

#use help(___) to find out what the command does eg. help(len) tells the number of items in a container
#a list is also a "container"


#Things needed to know python- syntax, proper data struture, algorithm 