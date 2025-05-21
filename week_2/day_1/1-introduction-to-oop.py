#what is an object
#what is a class

#how to create a class
class Dog:
     #print("creating object")
    def __init__(self, name, color, breed, age):
        print('creating object')
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    def bark(self):
        print(f'{self.name} is barking')

    def walk(self, meters):
        print(f"{self.name} walked {meters} meeters today") 

    def rename(self, new_name):
        self.name = new_name


#an instance (or object) of class Dog is created
#shelter_dog = Dog()

#shelter_dog.color = "Black"
#print(shelter_dog.color)

#creating instances of dog after creating rhe __init
shelter_dog = Dog("rex", "black", "shelter", 5)
print(shelter_dog.__dict__)
shelter_dog.bark()
shelter_dog.walk(200)
shelter_dog.rename("paul")  # <-- added


huskey_dog = Dog("boby", "grey", "huskey", 9)
print(huskey_dog.name, huskey_dog.color, huskey_dog.age)
huskey_dog.bark()
huskey_dog.walk(300)


my_dogs = [shelter_dog, huskey_dog]
print(my_dogs)

for dog in my_dogs:
    print(dog.name)
print(type(huskey_dog))
# print(help(str))  
my_dogs_objects = [obj for obj in globals().values() if isinstance(obj, Dog)]  



#    Analyse the code below. What will be the output ?
  #  Explain the goal of the methods
 #   Create a method that modifies the name of the person


class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print(f"Hello my name is {self.name}, & I am {self.age}, years old")

  def rename(self, new_name):
        self.name = new_name  

first_person = Person("John", 36)
first_person.show_details()

first_person.rename("Dave")  

first_person.show_details() 