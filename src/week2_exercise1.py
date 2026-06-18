age = int(input("What is your age? "))

if age < 0:
    print("Age cannot be negative.")
elif age > 120:
    print("Age seems unrealistic. Please enter a valid age.")
elif age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")