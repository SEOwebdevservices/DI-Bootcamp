#Exercise 1: Converting Lists into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
data = {k:v for k,v in zip(keys,values)}
print(data)


print(" ")#this code is just to make a space between my code
#Exercise 2: Cinemax #2
# Create a dictionary of family members and their ages
family_ages = {
    "Steve": 53,
    "James": 43,
    "Shelly": 5,
    "Orit": 2
}

total_cost = 0

# Loop through the dictionary
for name, age in family_ages.items():
    # Check age and apply ticket price
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    print(f"{name} (age {age}): ${price}")
    total_cost += price

print(f"Total cost for the family: ${total_cost}")


print(" ")#this code is just to make a space between my code
#Exercise 3: Zara
# Create the dictionary
brand = {
    "name": "zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Change number of stores to 2
brand["number_stores"] = 2

#Print a sentence about Zara’s clients
print("Zara’s clients are:", ", ".join(brand["type_of_clothes"]))

#Add new key: country_creation
brand["country_creation"] = "Spain"

#Check if "international_competitors" exists, then add "Desigual"
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#Delete the "creation_date" key
del brand["creation_date"]

#Print the last item in international_competitors
print("Last international competitor:", brand["international_competitors"][-1])

#Print major colors in the US
print("Major colors in the US:", ", ".join(brand["major_color"]["US"]))

#Print the number of keys in the dictionary
print("Number of keys in the brand dictionary:", len(brand))

#Print all keys of the dictionary
print("Keys in the brand dictionary:", list(brand.keys()))

print(" ")#this code is just to make a space between my code


#Exercise 4: Disney Characters
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Create a dictionary that maps characters to their indices:
users_dict = {}

for index in range(len(users)):
    users_dict[users[index]] = index

print(users_dict)
#Create a dictionary that maps indices to characters:
index_to_user = {}

for index in range(len(users)):
    index_to_user[index] = users[index]

print(index_to_user)
#Create a dictionary where characters are sorted alphabetically and mapped to their indices:
users.sort()
print(users)
sorted_users = sorted(users)
sorted_dict = {}
for index in range(len(sorted_users)):
    sorted_dict[sorted_users[index]] = index
    print(sorted_dict)