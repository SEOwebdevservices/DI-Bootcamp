#Ask the user for two inputs:
#A number (integer).
#A length (integer).

#2. Create a program that generates a list of multiples of the given number.
#3. The list should stop when it reaches the length specified by the user.
# Ask the user for a length
#number = int(input("Enter a number: "))
#length = int(input("Enter a length in meeters: "))

# Make a list of multiples
#multiples = []
#for i in range(1, length + 1):
    #multiples.append(number * i)
    #print (multiples)

user_input = input("Type a string: ")
result = ""

for char in user_input:
    if result == "" or char != result[-1]:
        result += char


print("Without consecutive duplicates:", result)