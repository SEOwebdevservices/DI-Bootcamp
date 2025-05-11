human_years = int(input("How many human years ago did you get your cat and dog? "))

# Make sure the input is at least 1
if human_years < 1:
    print("Human years must be 1 or greater.")
else:
    # Calculate cat years
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculate dog years
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    # Print the results
    print(f"\nHuman Years: {human_years}")
    print(f"Cat Years: {cat_years}")
    print(f"Dog Years: {dog_years}")

Example Output (if user enters 3):
