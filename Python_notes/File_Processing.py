#myfile = open("fruits.txt") #file object is created
#cursor starts at the beginning, but after read goes to the end of the file (can't do print file twice)

#content = myfile.read()        can either save the content as a variable 

#or do seek(0)
#print(myfile.read()) 
#myfile.seek(0)
#print(myfile.read())

#myfile.close() #deletes the file from memory   
                # can put the file in a variable like contents and recall that even when file has been closed

#with open("files/fruits.txt") as myfile:
#    content = myfile.read()      #file wll be closed once the "with" block ends
#print(content)

with open("files/vegetables.txt", "a+") as myfile:    #can but 'r' instead of w for reading. just helps with readibility 
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic\n")                           # if you write in an existing file it will rewrite the file 