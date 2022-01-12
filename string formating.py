name = input("Enter your name: ")
surname = input("Enter your surname:")
message = "Hello %s %s!" % (name, surname) # the value after %s will replace it 
message2 = f"Hello {name} {surname}!" #implemented in in method 3.6m
print(message)
print(message2)



# %s is a special string in python that allows the program to put in variables