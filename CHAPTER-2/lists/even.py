en = {}
odd = {}
for x in range(1, 10):    
    if x % 2 == 0:
        en[x] = x
        print("Even number:", en)
    elif x % 2 != 0:
        odd[x] = x
        print("Odd number:", odd)
    else:
        print("Error: Invalid number:", x)
        
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

even = {}
odd = {}
prime = {}

for x in range(1, 10):
    if x % 2 == 0:
        even[x] = x
    else:
        odd[x] = x
    if is_prime(x):
        prime[x] = x

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Prime numbers:", prime)
    