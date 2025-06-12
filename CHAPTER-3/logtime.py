import time

# Decorator to measure and print execution time
def log_time(func):
    # Wrapper function that adds timing functionality
    def wrapper(*args, **kwargs):
        # Record start time
        start = time.time()

        # Call the original function
        result = func(*args, **kwargs)

        # Record end time
        end = time.time()

        # Print execution time
        print(f"{func.__name__} took {end - start:.2f} seconds")

        return result
    return wrapper

# Apply timing decorator to this function
@log_time
def slow_function():
    # Simulate slow operation
    time.sleep(2)

# Execute the decorated function
slow_function()