age = int(input("Enter your age? "))
while age < 0 or age > 120:
    print("Invalid age. Please enter a value between 0-120")
    age = int(input("What is your age? "))

print(f"Valid! Your age is {age}.")