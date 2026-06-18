price = float(input("Enter the price of the product: "))
rating = float(input("Enter the rating of the product (1-5): "))
discount_percentage = int(input("Enter the discount percentage (0-100): "))

if (price < 50 and rating >= 4.0) or discount_percentage >= 20:
    print("This is good value!")
else:
    print("Not a good value.")