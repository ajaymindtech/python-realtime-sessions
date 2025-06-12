my_tuple = (1, 2, 3)
temp_list = list(my_tuple)   # Convert to list
temp_list[0] = 10            # Modify the list
my_tuple = tuple(temp_list)  # Convert back to tuple
print("Modified tuple:", my_tuple)