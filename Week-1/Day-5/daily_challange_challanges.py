#Challenge 1: Sorting
# Step 1: Get Input
#words = input("Enter words separated by commas: ")

# Step 2: Split the String
#word_list = words.split(",")

# Step 3: Sort the List
#word_list.sort()

# Step 4: Join the Sorted List
#sorted_words = ",".join(word_list)

# Step 5: Print the Result
#print(sorted_words)

#Challenge 2: Longest Word

# Step 1: Define the function
def longest_word(sentence):
    # Step 2: Split the sentence into words
    words = sentence.split()
    
    # Step 3: Initialize variables
    longest = ""
    
    # Step 4: Iterate through the words
    for word in words:
        # Step 5: Compare word lengths
        if len(word) > len(longest):
            longest = word  # update longest word
    
    # Step 6: Return the longest word
    return longest

# Test examples:
print(longest_word("Margaret's toy is a pretty doll."))  # Margaret's
print(longest_word("A thing of beauty is a joy forever."))  # forever.
print(longest_word("Forgetfulness is by all means powerless!"))  # Forgetfulness