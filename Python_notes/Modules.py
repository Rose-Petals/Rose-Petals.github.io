import time  #can see what to import by using import sys --> sys.builtin_module_names ---> then use dir(fill in the blank) to see what it can do etc  
import os
import pandas #3rd party libraby, have to install using pip3 install pandas

while True:
    print (os.getcwd())  #use print(os.getcwd()) to get which folder or location you are working in
    if os.path.exists("files/vegetables.txt"):   
        with open("files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)  #slows down the reading on the file