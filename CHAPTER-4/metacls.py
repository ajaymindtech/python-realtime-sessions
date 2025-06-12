# Import statements (none needed)

# Define metaclass that customizes class creation
class Meta(type):
    # Method called when creating a new class
    # cls: The metaclass itself (Meta)
    # name: Name of the class being created
    # bases: Parent classes being inherited from
    # dct: Dictionary of class attributes and methods
    def __new__(cls, name, bases, dct):
        # Add new attribute to the class dictionary
        dct["new_attribute"] = "Added by metaclass"
        # Call parent (type) __new__ to create and return the class
        return super().__new__(cls, name, bases, dct)

# Define class that uses Meta as its metaclass
# MyClass will have new_attribute added automatically
class MyClass(metaclass=Meta):
    pass

# Print the attribute that was added by the metaclass
# Shows the attribute exists and contains expected value
print(MyClass.new_attribute)  # Output: Added by metaclass