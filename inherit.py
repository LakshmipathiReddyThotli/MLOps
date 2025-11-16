# # Inheritance Demonstration 
# # what is inherited? - constructor, non private members ( variables and methods) 
# class Animal:

#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes sound")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Animal.name = name
#         super().__init__(name)
#         self.breed = breed

#     def speak(self):
#         print(f"{self.name} is of {self.breed} type")


# # animal = Animal("Generic")
# # animal.speak()

# dog = Dog("Ninja", "Labrodor")
# dog.speak()

# # 1. single inheritance 
# # 2 Multilevel inheritance
# # 3. Multiple Inheritance <Diamond Problem>
# # 4. Hybrid inheritance


class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes sound")

class Mammal(Animal):

    def feed(self):
        print(f"{self.name} is feeding milk")

class Bird(Animal):

    def fly(self):
        print(f"{self.name} is flying")

class  Bat(Mammal, Bird):
    def __init__(self, name):
            Mammal.__init__(self,name)

    def nocturnal(self):
        print(f"{self.name} is nocturnal")


bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.nocturnal()