# Singleton class that ensures only one instance is created
class Singleton:
    # Class variable to store the single instance
    _instance = None

    # __new__ is called when creating a new instance
    # cls is the class itself
    def __new__(cls):
        # Check if instance already exists
        if not cls._instance:
            # If no instance exists, create one using parent class __new__
            cls._instance = super().__new__(cls)
        # Return the single instance
        return cls._instance

# Create first instance
s1 = Singleton()

# Create second instance - will return same instance as s1
s2 = Singleton()

# Compare if s1 and s2 are the same object using 'is' operator
# True because they reference the same instance
print(s1 is s2)  # Output: True