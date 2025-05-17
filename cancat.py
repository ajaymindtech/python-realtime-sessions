x = 10
y = "20"
print("x is " + str(x) + " and y is " + y)  # Concatenation
print("x is {} and y is {}".format(x, y))  # str.format()
print("x is %d and y is %s" % (x, y))  # Old-style formatting
print("x is %d and y is %s" % (x, y))  # New-style formatting

print(x + int(y))  # Output: 30
print(str(x) + y)  # Output: 1020