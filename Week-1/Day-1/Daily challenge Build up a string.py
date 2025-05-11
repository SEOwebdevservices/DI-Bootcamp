#1. Ask for User Input:
#user_input = input("Add a Name exactly 10 characters long" )
#2. Check the Length of the String:
#print(len(user_input))
#if len(user_input) < 10:
    #print("String not long enough.")
#elif len(user_input) > 10:
    #print("String too long.")
#else:
    #print("Perfect string")
#3. Print the First and Last Characters:
name = "mommyfreed"
print("first character:", name[0])
print("last character:", name[9])

#4. Build the String Character by Character:
text = "mommyfreed"
for i in range(1, len(text) + 1):
    print(text[:i])

#5. Bonus: Jumble the String (Optional)