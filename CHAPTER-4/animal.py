class Animal:
    def __init__(self, name):

        # Initialize the Animal with a name
        self.name = name  # Store name as instance attribute

    def speak(self):
        # Method to be overridden by child classes
        # Currently does nothing (placeholder)
        pass

# Create an Animal instance named "Rex"
dog = Animal("Rex")


# Access and print the name attribute
print(dog.name)  # Prints: Rex

# Example child class showing inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Example cat class showing inheritance
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of child classes
dog = Dog("Rex")
cat = Cat("Whiskers")





