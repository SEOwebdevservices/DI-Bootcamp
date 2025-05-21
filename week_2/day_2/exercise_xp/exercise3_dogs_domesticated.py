from exercises_XP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False  

    def train(self):
        print(self.bark())
        self.trained = True  

    def play(self, *args):
        dogs_names = ', '.join([dog.name for dog in args])
        print(f"{self.name} plays with {dogs_names}.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}")


dog1 = PetDog("Buddy", 3, 20)
dog2 = PetDog("Max", 4, 25)
dog3 = PetDog("Bella", 2, 18)


dog1.train()  


dog1.play(dog2, dog3)  


dog1.do_a_trick()  
dog2.do_a_trick()  


