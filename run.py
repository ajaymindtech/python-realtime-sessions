import pdb
x=10
y=0
try:
    
    pdb.set_trace()
    
    print(x/y)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    print(f"{x} can not be devided by {y}".format(x=x, y=y))
finally:
    print("This block always executes.")    

