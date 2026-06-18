name = input("What is your name? ")
age = int(input("What is your age? "))
age_in_5_years = age + 5
message = f"{name} is {age} years old and will be {age_in_5_years} years old in 5 years."
print(message)


product_a_price = (input("Enter the price of Product A: "))
product_b_price = (input("Enter the price of Product B: "))
product_a_price_f = float(product_a_price)
product_b_price_f = float(product_b_price)
print(f"Product A costs {product_a_price_f} and Product B costs {product_b_price_f}.")
is_a_cheaper_b = product_a_price_f < product_b_price_f
print(f"Is Product A cheaper than Product B? {is_a_cheaper_b}")