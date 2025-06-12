from animal import Animal ,Dog,Cat # Assuming Animal is defined in animal.py

def make_animal_speak(animal):
    print(animal.speak())
    
# Create instances of child classes
dog = Dog("Rex")
cat = Cat("Whiskers")

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!