#Exercise 1: What Are You Learning?
#Step 1: Define a Function
#def learning(display_message):
   # '''prints a phrase on the console'''
    #Step 2: Print a Message
    #print(f"I am learning about {display_message}in Python")
#Call the Function
#learning(display_message = "functions ")
#
#Exercise 2: What’s Your Favorite Book?
#Step 1: Define a Function with a Parameter
#def favorite_book(title):
#    '''prints a phrase on the console'''
#    #Step 2: Print a Message with the Title
#    print(f"{title}has to be one of my favorite books")
#favorite_book(title = "Thieves World ")  

#
#Exercise 3: Some Geography
#def describe_city(city, country="Unknown"):
  #Step 2: Print a Message
    #print(f"{city} is in {country}")
#describe_city("Reykjavik", "Iceland")  # This will print: Reykjavik is in Iceland
#describe_city("Paris")  # This will print: Paris is in Unknown
#
#Exercise 4: Random
#Step 1: Import the random Module
#import random
#Step 2: Define a Function with a Parameter
#def compare_random_numbers(user_number):
    # Step 3: Generate a random number
    #random_number = random.randint(1, 100)
    
    # Step 4: Compare the numbers
    #if user_number == random_number:
        #print("Success! The numbers match.")
    #else:
        #print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Step 5: Call the function with a number between 1 and 100
#compare_random_numbers(50)  # You can replace 50 with any number between 1 and 100

#Exercise 5: Let’s Create Some Personalized Shirts! ok
#Step 1: Define a Function with Parameters
#def make_shirts(size, text):
    #Step 2: Print a Summary Message
    #print(f"This shirt is a size {size}, {text} ")
#Step 3: Call the Function
#make_shirts(size="large", text="I Love Python")
#make_shirts(size="Medium", text="I Love Python")
#make_shirts(size="small", text="I Dislike Python")


# Exercise 6: Magicians…

# Step 1: Create a List of Magician Names
#magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Step 2: Create a Function to Display Magicians
#def show_magicians(magicians):
    #for magician in magicians:
       #print(magician)

# Step 3: Create a Function to Modify the List
#def make_great(magicians):
    # Use list comprehension to add "the Great" to each magician's name
    #return [magician + ' the Great' for magician in magicians]

# Step 4: Call the Functions
#magician_names = make_great(magician_names)  # Modify the list
#show_magicians(magician_names)  # Display the modified list

#Exercise 7: Temperature Advice
# Step 1: Create the get_random_temp() Function
import random

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 23), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn":
        return round(random.uniform(5, 20), 1)
    else:
        return round(random.uniform(-10, 40), 1)

def main():
  
    month = int(input("Enter the month number (1–12): "))
    
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    else:
        season = "unknown"
    
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 17 <= temp <= 23:
        print("Nice weather.")
    elif 24 <= temp <= 32:
        print("A bit warm, stay hydrated.")
    elif 33 <= temp <= 40:
        print("It’s really hot! Stay cool.")

main()