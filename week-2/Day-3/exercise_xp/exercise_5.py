# Exercise 5: Amount of time left until January 1st
import datetime

# Step 2 to Step 5: Function to show time left until January 1st
def time_until_january():
    # Step 2: Get current date and time
    now = datetime.datetime.now()

    # Step 3: Create a datetime for January 1st of the next year
    next_year = now.year + 1
    jan_first = datetime.datetime(year=next_year, month=1, day=1)

    # Step 4: Calculate the difference
    time_left = jan_first - now

    # Step 5: Display the difference
    print("Time left until January 1st:", time_left)

# Call the function
time_until_january()