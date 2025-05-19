#Exercise 4: Family and Person Classes
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age)
        new_person.last_name = self.last_name
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print("Person not found.")

    def family_presentation(self):
        print(f"Family name: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name}, {person.age} years old")


# === Test Code (must be outside the class definitions) ===
my_family = Family("Smith")

# Add members
my_family.born("Alice", 17)
my_family.born("Bob", 20)

# Check if someone is allowed to go out
my_family.check_majority("Alice")  # should print "not allowed"
my_family.check_majority("Bob")    # should print "allowed"

# Show the family
my_family.family_presentation()      