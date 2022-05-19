

#new_temps= [temp/10 for temp in temps]         #List comprehension, much shorter 

#for temp in temps:                             Long way
  #  new_temps.append(temp / 10)


temps = [221, 234, 340, -9999, 230]

new_temps = [temp/10  if temp!=-9999 else 0 for temp in temps]

print(new_temps)