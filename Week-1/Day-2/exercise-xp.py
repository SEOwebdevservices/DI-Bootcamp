#Exercise 1: Favorite Numbers
#Create a set called my_fav_numbers and populate it with your favorite numbers. 
#my_fav_numbers = {"5","13","438","666"}
#Add two new numbers to the set. 
#my_fav_numbers.add("1971")
#my_fav_numbers.add("53")
#print(my_fav_numbers)

#Remove the last number you added to the set. 

#my_fav_numbers.discard("53")
#print(my_fav_numbers)

#Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers
#friend_fav_numbers = {"2", "6", "12", "21"}
#Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
    # Note: Sets are unordered collections, so ensure no duplicate numbers are added.
#our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
#print(our_fav_numbers) 

#Exercise 2: Tuple
#mytuple = ('12', '1971', '13', '21', '5', '2', '6', '666', '438')
#print(mytuple)
#Given a tuple of integers, try to add more integers to the tuple.

#y = list(mytuple)
#y.append("1948")
#mytuple = tuple(y)
#print(mytuple)

#Exercise 3: List Manipulation
#basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove "Banana" from the list. 
#basket.remove("Banana")
#basket.remove("Blueberries")
#print(basket)
#Add "Kiwi" to the end of the list
#basket.append("Kiwi")
#basket.insert(0, "Apples")
#print(basket)
#Count how many times "Apples" appear in the list. 
#print(basket.count("Apples"))
#basket.clear()
#print(basket)

#Exercise 4: Floats
#hat is a float?
#A flots is a number that can be pos or neg that may or may not contain one or more decimals
#What’s the difference between a float and an integer? 
#an int is a whole number and a float can be a whole number or can contains a decimal
#Create a list containing the following sequence of mixed floats and integers:
#1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5. 

#loops: for and while Loops
#fruits = ["apple", "banana", "Kiwi", "pear"]
#for each_fruite in fruits:
    #print(f"I love {each_fruite}")

#for i in range(1, 11):
    #print(i)
#seq=[]
#i = 1
#while i < 5: 
   # i +=0.5
    #if int(i) == i:
        #seq.append (int(i))
    #else: 
        #seq.append (i)
    
#print(seq)    
#Exercise 5: For Loop
#Write a for loop to print all numbers from 1 to 20, inclusive. 
##for number in range(1, 21):
    #print(number)

#Write another for loop that prints every number from 1 to 20 where the index is even
#for number in range(1, 21):
    #if number % 2 == 0:
        #print(number)
# Write a while loop that keeps asking the user to enter their name.
 #Stop the loop if the user’s input is your name.
#while True:
    #name = input("what is your name?")
    #if name.lower() == "steve":
        #break

#Exercise 7: Favorite Fruits
#favorite_fruits = input("Enter your favorite fruits (Seperated by spaces):").split()
#fruit = input("Enter the name of a fruit: ")
#if fruit in favorite_fruits:
    #print("You chose one of your favorite fruits! Enjoy!")
#else:
    #print("You chose a new fruit. I hope you enjoy it!")

#Exercise 8: Pizza Toppings
#toppings = []
#base_price = 10
#topping_price = 2.5

#while True:
    #topping = input('Enter a Pizza Topping (type "quit" to finish): ')
    #if topping.lower() == "quit":
        #break
    #toppings.append(topping)
    #print(f"Adding {topping} to your pizza.")

    #total_cost = base_price + topping_price* len(toppings)
    #print("\nToppings added:")
    #for t in toppings:
        #print(f"- {t}")

#print(f"Total cost of the pizza: ${total_cost:.2f}")        

#Exercise 9: Cinemax Tickets
#Ask for the age of each person in a family who wants to buy a movie ticket. 
#Calculate the total cost based on the following rules:
 #Free for people under 3.
    #$10 for people aged 3 to 12.
    #$15 for anyone over 12.

    #Print the total ticket cost. 
total_cost = 0
num_people = int(input("How many people are you buying tickets for? "))

for i in range(num_people):
    age = int(input(f"Enter the age of person #{i+1}: "))
    if age < 3:
        print("Free")
    elif age <= 12:
        print("Ticket is $10.")
        total_cost += 10
    else:
        print("Ticket is $15.")
        total_cost += 15

print(f"Total cost for all tickets: ${total_cost}")
   
#Exercise 10: Sandwich Orders

sandwich_orders = ["tuna", "pastrami", "avocado", "pastrami", "egg", "chicken", "pastrami"]
finished_sandwiches = []

# Remove all "pastrami" from the list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Prepare each sandwich
for sandwich in sandwich_orders:
    print(f"Your {sandwich} sandwich is ready.")
    finished_sandwiches.append(sandwich)

# Print final list of finished sandwiches
print("Finished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"{sandwich.capitalize()}")
