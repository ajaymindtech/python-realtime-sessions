def animal(type, name):
    type = "dog"
    name = "Rex"
    print(type, name)

animal("dog", "Rex")


class Animal:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def speak(self):
        print(f"{self.name} says: Woof!")

dog = Animal("dog", "Rex")
dog.speak()
