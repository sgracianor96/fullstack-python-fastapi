def validate_age(age):
    """
    Check if age is valid (between 0-120)
    
    Arguments:
        age: integer to validate
    
    Returns:
        True if valid, False if not
    """
    if age < 0 or age > 120:
        return False
    return True


# Use the function
user_age = int(input("Enter your age: "))

if validate_age(user_age):
    print(f"Age {user_age} is valid!")
else:
    print(f"Age {user_age} is invalid!")