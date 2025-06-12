# 1. Storing coordinates (latitude, longitude)
location = (17.3850, 78.4867)
print("Location coordinates:", location)

# 2. Returning multiple values from a function
def get_min_max(numbers):
    return (min(numbers), max(numbers))

result = get_min_max([10, 20, 5, 40])
print("Min and Max:", result)

# 3. Unpacking tuple values
person = ("Ajay", 30, "Hyderabad")
name, age, city = person
print(f"Name: {name}, Age: {age}, City: {city}")

# 4. Using tuples as dictionary keys
employee_salaries = {
    ("Ajay", "IT"): 120000,
    ("Sita", "HR"): 95000
}
print("Ajay's IT Salary:", employee_salaries[("Ajay", "IT")])