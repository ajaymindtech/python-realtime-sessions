def my_decorator(func):  # Takes a function as argument
    def wrapper():  # Inner function that wraps the original
        print("Something is happening before the function is called.")  # Runs before
        func()  # Calls the original function
        print("Something is happening after the function is called.")  # Runs after
    return wrapper  # Returns the wrapper function

@my_decorator  # Applies decorator to say_hello
def say_hello():  # Function being decorated
    print("Hello!")  # Original function code

say_hello()  # Calls decorated function
@my_decorator  # Applies decorator to say1_hello
def say1_hello():  # Function being decorated
    print("Hello second!")  # Original function code

say1_hello()  # Calls decorated function
