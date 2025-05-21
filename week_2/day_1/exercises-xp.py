#Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

    def find_oldest_cat(self, cat2, cat3):
            oldest_age = max(self.age,  cat2.age, cat3.age)
            for cat in [self, cat2, cat3]:
                 if cat.age == oldest_age: 
                    return cat
         
    


cat_1 = Cat('Lili', 3)
cat_2 = Cat('taffy', 15)
cat_3 = Cat('Caramelo', 7)
print(cat_2.__dict__)
oldest=cat_1.find_oldest_cat (cat_2, cat_3)
print(f"The oldest cat is {oldest.name}, and is {oldest.age} years old.")

#Exercise 2 : Dogs
class Dog:
     def __init__(self, dog_name, dog_height):
         self.name = dog_name
         self.height = dog_height 
     def bark(self):
        print(f'{self.name} goes woof')

     def jump(self):
        print(f"jumps {self.height * 2} cm high")

     def find_big_dog(self, dog2):
            big_height = max(self.height, dog2.height)
            for dog in [self, dog2]:
                 if dog.height == big_height:
                      return dog   

davids_dog = Dog("KC", 20)
sarahs_dog = Dog("Penny", 31)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.height
davids_dog.bark ()
davids_dog.jump()
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark ()
sarahs_dog.jump()
big_dog = davids_dog.find_big_dog(sarahs_dog)
print(f"The bigger dog is {big_dog.name}, with a height of {big_dog.height} cm")

#Exercise 3 : Who’s the song producer?
# Step 1: Create the Song class
class Song:
    # Constructor method that takes a list of lyrics
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # Method to print the song lyrics line by line
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Example: Create a Song object and call the method
crazy_train = Song([
    "Crazy, but that's how it goes"
    "Millions of people living as foes"
    "Maybe. It's not too late"
    "To learn how to love, and forget how to hate"
])

# Call the method to print the lyrics
crazy_train.sing_me_a_song()

#Exercise 4 : Afternoon at the Zoo
## Step 1: Define the Zoo class
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo.")
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        if not self.animals:
            print("No animals in the zoo.")
        else:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(animal)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        self.animals.sort()  # Sort animals alphabetically
        self.grouped_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in self.grouped_animals:
                self.grouped_animals[first_letter] = []
            self.grouped_animals[first_letter].append(animal)

        return self.grouped_animals

    def get_groups(self):
        grouped = self.sort_animals()
        print("Grouped Animals:")
        for letter, group in grouped.items():
            print(f"{letter}: {group}")

# Step 2: Create a Zoo instance
ramat_gan_safari = Zoo("Ramat Gan Safari")

# Step 3: Use the Zoo methods
ramat_gan_safari.add_animal("Giraffe")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Bear")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()