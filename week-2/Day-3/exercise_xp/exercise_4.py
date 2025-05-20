import datetime

# Step 2 and 3: Create a function that gets and shows the current date
def show_date():
    today = datetime.date.today()
    print("Today's date is:", today)

# Call the function
show_date()