#strings: is a sequence of characters that represent text in Python


#string Methods
#"Hello Python".capitalize()
#print("Hello Python")
#print("hello python".upper())
#print("hello python".lower())
#print("Goodnight Moon".replace("Moon", "Honey"))

# 3 strings: sequence of chars: it allows us to use indexes (Positions)

#greetings= "Hello Python"
#print(greetings[6:12]) #slicing a string
#print(greetings[2])

description = "strings are..."
#make it all uper case
#print(description.upper())
#replace the word "are" to "is"
#print(description.replace("are", "is"))
##print(description[0:7])

#numbers: integers, float, complex

a = 5 #int
b = 2.7 #float
c = 5 + 3
print(c)

print(5*2)
print(5**2)

print(10/2)
print(11//2) #floor division
print(11%2) #modulus division
print(round(10/3,2))

#my_age = 35
#print("Hello, my name is Steve, I am" + str(my_age) +  "  years old")

#price + "150"
#result + int(price) + 5
#print(result)

#user_name = input("what is your name?")
#print(user_name)

##user_name = input("what is your age?")
#print(user_age + 50)

#user_age = int(input("what is your age?"))
#print(user_age + 50)

# Booleans: True or Fale values

#comparison operators
print(3 > 4)

#comparison key words
print( "js" is "Python")
print( "Python" is "Python")
print( "Python" is not "Python")

#1 = 350
#b = 350
#print(a == b) #true
#print(a is b) #

print(bool("1"))

#check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:
bank_balance = "3300"
#Phone_number = 532287514

print (int(bank_balance))
#print(str(phone_number))

#string formatting Fstring
print(f"your bank account ballance is {bank_balance}, therefore you can take a loan")

#before f-strings - IE before python 3 we used format():
name = "steve"
age = 53
message = "my name is" {}, I am {} years old" .format(name, age)
print(message)
