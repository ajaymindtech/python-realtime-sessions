# Initialize descriptor class to enforce non-negative values
class NonNegative:
    # Store descriptor name when class is created
    def __set_name__(self, owner, name):
        self.name = name

    # Get value from instance dict, default to 0 if not set
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, 0)

    # Validate and set value in instance dict
    def __set__(self, instance, value):
        # Check if value is negative
        if value < 0:
            raise ValueError("Value cannot be negative")
        # Store valid value in instance dict
        instance.__dict__[self.name] = value

# Product class using NonNegative descriptor
class Product:
    # Define price attribute with NonNegative descriptor
    price = NonNegative()

# Create product instance
product = Product()

# Set valid positive price
product.price = 10

# Print current price value
print(product.price)  # Output: 10

# Try to set invalid negative price - will raise error
product.price = -5  # Raises ValueError