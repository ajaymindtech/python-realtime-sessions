# Animal Factory class - creates different animal objects
class AnimalFactory:
    # Method to create animal objects based on type parameter
    def create_animal(self, animal_type):
        # If type is "dog", create and return Dog instance
        if animal_type == "dog":
            return Dog("Rex")
        # If type is "cat", create and return Cat instance
        elif animal_type == "cat":
            return Cat("Whiskers")

# Dog class definition
class Dog:
    # Initialize dog with name
    def __init__(self, name):
        self.name = name

    # Method to make dog speak
    def speak(self):
        return "Woof!"

# Cat class definition
class Cat:
    # Initialize cat with name
    def __init__(self, name):
        self.name = name

    # Method to make cat speak
    def speak(self):
        return "Meow!"

# Create factory instance
factory = AnimalFactory()

# Create dog using factory
dog = factory.create_animal("dog")

# Make dog speak and print result
print(dog.speak())  # Output: Woof!