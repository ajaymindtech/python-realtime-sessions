char_to_ascii = {char: ord(char) for char in 'abc'}
print(char_to_ascii)  # Output: {'a': 97, 'b': 98, 'c': 99}

char_to_ascii = {}
for char in 'abc':
    char_to_ascii[char]= ord(char)
print(char_to_ascii)  # Output: {'a': 97, 'b': 98, 'c': 99}