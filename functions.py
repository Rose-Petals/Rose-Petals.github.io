
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)

    return the_mean


student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(student_grades)) 


#You have to return and not print in a function
#None is a return type
