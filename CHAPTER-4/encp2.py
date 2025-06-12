class Person:
    def __init__(self, name, age, salary):
        self.name = name            # Public
        self._age = age             # Protected
        self.__salary = salary      # Private

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Salary: {self.__salary}")  # Accessible inside the class

# Inheritance to test protected and private access
class Employee(Person):
    def show_details(self):
        print(f"Accessing from subclass:")
        print(f"Name: {self.name}")     # ✅ Public - Accessible
        print(f"Age: {self._age}")      # ✅ Protected - Accessible in subclass
        # print(f"Salary: {self.__salary}")  # ❌ Private - Not accessible
        # Accessing private via name mangling (not recommended)
        print(f"Salary (via name mangling): {self._Person__salary}")

# Object creation
emp = Employee("Ajay", 30, 70000)

# Accessing public member
print("Public:", emp.name)        # ✅

# Accessing protected member
print("Protected:", emp._age)     # ⚠️ Allowed, but by convention should not be accessed directly

# Accessing private member
# print("Private:", emp.__salary)  # ❌ Will raise AttributeError

# Accessing private member via name mangling
print("Private (mangled):", emp._Person__salary)  # ⚠️ Not recommended

# Display info using method
emp.display_info()
emp.show_details()
