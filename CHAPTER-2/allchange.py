my_tuple = (1111, 2, 3)
temp_list = list(my_tuple)   # Convert to list

# Change all elements
temp_list[0] = 10
temp_list[1] = 20
temp_list[2] = 30

my_tuple = tuple(temp_list)  # Convert back to tuple
print("Modified tuple:", my_tuple)