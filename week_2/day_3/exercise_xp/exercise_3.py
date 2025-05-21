import string
import random


all_letters = string.ascii_letters  


random_string = ""

for i in range(5):
    random_char = random.choice(all_letters)  
    random_string = random_string + random_char  
print("Random string of 5 letters:", random_string)