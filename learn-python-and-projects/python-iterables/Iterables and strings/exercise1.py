#exercise1
#text = "Python is Fun!"
#1. Convert the entire string to uppercase
text = "Python is Fun!"
upper_text = text.upper()
print(upper_text) 
#why in the materials does it show the code as this:
#opnion = "this Is nIce"
#opnion.upper() 
#print(opnion)
# 'THIS IS NICE'

opnion = "this Is nIce"
opnion.upper() 
print(opnion)
# 'THIS IS NICE'

#2Make the first letter upper case

text = "python is fun!"
capital_text = text.capitalize()
print(capital_text) 

#3. Make the first letter of each word upper case
text = "python is fun!"
title_text = text.title()
print(title_text) 

#4. Find the index of "F". What happens if you use lower case in the method?
text = "Python Is Fun!"
index = text.index("F")
print(index)
#if you use the lower case you will get ValueError: substring not found
# 5. Find a substring 

