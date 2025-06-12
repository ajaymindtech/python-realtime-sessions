common_chars = set("apple") & set("banana")  # Intersection
print(common_chars)  # Output: {'a'}


set1 = set("apple")
print(set1)  # Output: {'a', 'p', 'e', 'l'}
set2 = set("banana")
print(set2)  # Output: {'a', 'n', 'b', 'a'}

# Union
union = set1 | set2  # Union
print(union)  # Output: {'a', 'p', 'e', 'l', 'n', 'b', 'a'}

# Difference
difference = set1 - set2  # Difference
print(difference)  # Output: {'p', 'l'} (apple and banana)