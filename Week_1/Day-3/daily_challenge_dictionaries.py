#daily_challenge_dictionaries
#1. User Input:
#Ask the user to enter a word.
#Store the input word in a variable.
user_word = input("Enter a word: ")
#Iterate through each character of the input word using a loop.
#And check if the character is already a key in the dictionary.
#If it is, append the current index to the list associated with that key.
#If it is not, create a new key-value pair in the dictionary.
# Create an empty dictionary
char_positions = {}


for index in range(len(user_word)):
    char = user_word[index]  

 
    if char in char_positions:
        char_positions[char].append(index)
    else:
        char_positions[char] = [index]


print(char_positions)

print(" ")
#1. Store Data:

    #You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign).
    #You will also be given a string (wallet) representing the amount of money you have.

#2. Data Cleaning:

#3. Determining Affordable Items:

#4. Sorting and Output:

    #Sort the list of affordable items in alphabetical order.
    #If the list is empty (no items can be afforded), return the string “Nothing”.
    #Otherwise, return the sorted list.


items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
wallet_amount = int(wallet.replace("$", "").replace(",", ""))
affordable_items = []
for item in items_purchase:
    price_str = items_purchase[item]
    price = int(price_str.replace("$", "").replace(",", "")) 
    if price <= wallet_amount:
        affordable_items.append(item)
if len(affordable_items) == 0:
    print("Nothing")
else:
    print(sorted(affordable_items))