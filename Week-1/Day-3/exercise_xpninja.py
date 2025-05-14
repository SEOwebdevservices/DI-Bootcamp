#Exercise 1 : Cars
#Instructions

#1Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
#C2onvert it into a list using Python (don’t do it by hand!).
#3Print out a message saying how many manufacturers/companies are in the list.
#4Print the list of manufacturers in reverse/descending order (Z-A).
#5Using loops or list comprehension:
    #1Find out how many manufacturers’ names have the letter ‘o’ in them.
    #2Find out how many manufacturers’ names do not have the letter ‘i’ in them.

    #Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
       # Remove these programmatically. (Hint: you can use set to help you).
       # Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

       

car_brands = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

# Use the split() method to turn the string into a list
car_list = car_brands.split(", ")
count = len(car_list)
print("There are", count, "manufacturers in the list.")
print(car_list)
car_list.sort(reverse = True)
print(car_list)