# Tuples are immutable
my_tuple = (1, 2, 3)
print("Original tuple:", my_tuple)

# Trying to change a value will raise an error
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)