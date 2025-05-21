print("hello world\n" *4)

name = "Steve"
print(name)
age = 53
shoe_size = 11
info = f"My name is {name}, I am {age} years old and my shoe size is {shoe_size} inches. I like Harley Davidson Motorcycles"
print(info)

# Exercise 9 : Tall enough to ride a roller coaster
#Instructions

    #Write code that will ask the user for their height in centimeters.
    #If they are over 145 cm, print a message that states they are tall enough to ride.
    #If they are not tall enough, print a message that says they need to grow some more to ride.

height = int(input( "What is your Height: "))
if height >= 145:
    print(f"You are tall enought to ride")
else:
    print(f"You are not tall enough. Come back when you are taller.")

my_list = []
for i in range (0, 21, 2):
    
    print(i)
    my_list.append(i) 
print(my_list)    