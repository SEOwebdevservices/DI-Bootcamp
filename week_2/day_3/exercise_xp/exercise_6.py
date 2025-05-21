#Exercise 6: Birthday and minutes
import datetime


def minutes_lived(birthdate_str):
    
    birthdate = datetime.datetime.strptime(birthdate_str, "%Y-%m-%d")


    now = datetime.datetime.now()


    time_lived = now - birthdate


    minutes = time_lived.total_seconds() / 60


    print("You have lived for about", int(minutes), "minutes.")


minutes_lived("2000-01-01")