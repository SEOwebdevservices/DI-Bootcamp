#Exercise 1 : Hello World
for i in range(4):
  print("Hello World")

  #exercise2: SOme Math
  print((99 ** 3) * 8)

 #Exercise 3 : What is the output ?
#SyntaxError: invalid SyntaxError

#Exercise 4 : Your computer brand
computer_brand = "Asus"
print(f"I have a {computer_brand} computer")

#Exercise 5 : Your information
name = "Steve"
age = "53"
shoe_size = "11"
info = (f"My name is {name}, i'm {age}, years old and my shoe size is {shoe_size} inches")
print(info)

#Exercise 6 : A & B
a = 3
b = 2
if a > b:
  print("Hello World")

  #Exercise 7 : Odd or Even
#number = int(input("Enter a number: "))
#if (number % 2) == 0:
   #print("{0} is Even".format(number))
#else:
   #print("{0} is Odd".format(number))

#Exercise 8 : What’s your name ?
#my_name = "Steve"
#user_name = input("what is your name? ")
#if user_name == my_name:
    #print ("Cool Name")
#else:
    #print (f"oh well {user_name} too bad your name is not as cool as mine.")

    #Exercise 9 : Tall enough to ride a roller coaster
user_height = input("what is your Heightin CM?")
if user_height > 145:
  print ("You are tall enough to ride")
else:
  print ("oh well, you will need to grow some more to ride")
