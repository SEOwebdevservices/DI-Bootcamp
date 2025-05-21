import re

# Step 1: The original matrix string
MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 2: Convert the matrix string into a 2D list (matrix)
# - Remove leading/trailing whitespace
# - Split into lines
# - Convert each line to a list of characters
lines = MATRIX_STR.strip().split('\n')
matrix = [list(line) for line in lines]

# Optional: Print the matrix to visualize it
print("Matrix:")
for row in matrix:
    print(row)

# Step 3: Read the matrix column by column
rows = len(matrix)
cols = len(matrix[0])
decoded_raw = ""

for col in range(cols):
    for row in range(rows):
        decoded_raw += matrix[row][col]

print("\nRaw Decoded String (before cleanup):")
print(decoded_raw)

# Step 4: Replace symbols (non-alphabet characters) between letters with spaces
# - Use regular expression to replace any group of non-letters between letters with a space
cleaned_message = re.sub(r'(?<=\w)([^a-zA-Z]+)(?=\w)', ' ', decoded_raw)

# Step 5: Print the final decoded message
print("\n Decoded Message:")
print(cleaned_message)