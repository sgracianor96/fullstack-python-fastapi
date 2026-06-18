"""
Week 1 Exercise 1: Variables and Types
Learning: Basic variables, types, and operations
Author: Sebastian
"""

# TODO: Write your code here
# Create a variable called 'name' and assign your name
# Create a variable called 'age' and assign your age
# Create a variable called 'is_learning_python' and assign True or False
# Print all three variables using print()

name = "Sebastian"
age = 30
is_learning_python = True

message = f"{name} is {age} years old and is learning Python: {is_learning_python}"

print(name)
print(age)
print(is_learning_python)
print(message)
print(f"My age is {age} and {age}")

price_a = 25.99
price_b = 30.50
is_a_cheaper_b = price_a < price_b
print(f"Product A costs {price_a} and Product B costs {price_b}. Product A is cheaper: {is_a_cheaper_b}")

# Ask user for their name
name = input("What is your name? ")
print(f"Hello, {name}")

