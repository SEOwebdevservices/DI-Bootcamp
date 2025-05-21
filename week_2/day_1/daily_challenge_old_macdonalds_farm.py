# Step 1: Create the Farm class
class Farm:
    # Step 2: __init__ method
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    # Step 3: add_animal method
    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    # Step 4: get_info method
    def get_info(self):
        result = f"{self.name}'s farm\n\n"

        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"

        result += "\n    E-I-E-I-0!"
        return result

# Step 5: Test the code
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())