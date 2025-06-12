from animal import Animal  # Assuming Animal is defined in animal.py

class Dog(Animal):  # Inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!

