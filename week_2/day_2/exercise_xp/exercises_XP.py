class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
     def __init__(self, name, age, friendly, declawed):
         super().__init__(name, age)
         self.friendly = friendly
         self.declawed = declawed

bengal_cat = Bengal("Tiger", 3)
chartreux_cat = Chartreux("Misty", 4)
siamese_cat = Siamese("Luna", 2, friendly=True, declawed=False)
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

sara_pets = Pets(all_cats)
sara_pets.walk()


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        
    def bark(self):
        print(f'{self.name} is barking')
#mplement a run_speed() method that returns weight / age * 10.
    def run_speed(self):
        return self.weight / self.age * 10
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight :
            return f'the winner is {self.name}'
        else:
            return f'the winner is {other_dog.name}'

dog1 = Dog("KC", 15, 5)
print(dog1.__dict__)
dog1.name
dog1.age
dog1.weight 

dog2 = Dog("Wengie", 18, 2)
print(dog2.__dict__)
dog2.name
dog2.age
dog2.weight 




print(dog1.fight(dog2))
  

dog3 = Dog("Penny", 2, 6)
print(dog3.__dict__)
dog3.name
dog3.age
dog3.weight

