import time  #can see what to import by using import sys --> sys.builtin_module_names ---> then use dir(fill in the blank) to see what it can do etc  
import os
import pandas #3rd party libraby, have to install using pip3 install pandas, had to do python3 -m pip install pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")  #object called a data frame is created
        print(data.mean() ["st1"] )
    else:
        print("File does not exist.")
    time.sleep(10)