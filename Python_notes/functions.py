def mean(**kargs): # (*) essentially makes it a list. You can put as many values in there as you want
    return kargs
                        #keyword arguments are like a=4, b=5 because you are telling the program which is what
print(mean(a= 1,b= 2,c=4))    #non keyword arguments aka. positional arguments are (4,5) because you are relying on the positioning of the variables to let the program know what goes where

#add another (*) to make mean(**kwargs) for keyword arguments