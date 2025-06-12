from functools import lru_cache

# Cache decorator to store previously calculated values
@lru_cache(maxsize=None)
def fibonacci(n):
    # Base cases: fib(0) = 0, fib(1) = 1
    if n < 2:
        return n
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

# Calculate 10th Fibonacci number
print(fibonacci(10))  # Will print 55
