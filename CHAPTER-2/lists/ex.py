for x in range(1,5):
    print("For loop iteration:", x**3)
    
sequence = [1, 2, 3, 4, 5]
for x in sequence:
    print("For loop iteration:", x**2)
    
    
# Squared numbers
squared = [x**2 for x in range(10)]
print(squared)  # Output: [0, 1, 4, 9, ..., 81]

for x in range(10):
    print(x**2)