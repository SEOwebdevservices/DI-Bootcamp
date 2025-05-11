#1Declare a variable called first and assign it to the value "Hello World".
from re import T


first = "Hello World"
#2Write a comment that says "This is a comment."
# This is a comment

#3Log a message to the terminal that says "I AM A COMPUTER!"
print("I AM A COMPUTER!")

#4Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
if 1 < 2 and 4 > 2:
    print("Math is fun.")

#5Assign a variable called nope to an absence of value.
nope = None

#6Use the language’s “and” boolean operator to combine the language’s “true” value with its “false” value.
result = True and False
print(result)

#7Calculate the length of the string "What's my length?"
length = "what's my length?"
print(len(length))

#8Convert the string "i am shouting" to uppercase.
string = "i am shouting"
uppercase_string = string.upper()
print(uppercase_string)

#9Convert the string "1000"to the number 1000.
number_str = "1000"
number_int = int(number_str)
print(number_int)  

#10Combine the number 4 with the string "real" to produce "4real".
number = 4
string = "real"
combined = str(number) + string
print(combined)

#11Record the output of the expression 3 * "cool".
result = 3 * "cool"
print(result)

#12Record the output of the expression 1 / 0.
ZeroDivisionError: division by zero
#13Determine the type of [].
they are used to define "list literals," which are a way to create lists in Python.

#14Ask the user for their name, and store it in a variable called name.
name = input("What is your name? ")

#15Ask the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!.
number = float(input("Enter a number: "))
if number < 0:
    print("That number is less than 0!")
elif number > 0:
  print("That number is greater than 0!")
else:
  print("You picked 0!")

  #16Find the index of "l" in "apple".
  index = "apple".index("l")
  print(index)

  #17Check whether "y" is in "xylophone".
  result = "y" in "xylophone"
  print(result)
  
  #17Check whether a string called my_string is all in lowercase.
my_string = "hello world"
print(my_string.islower())