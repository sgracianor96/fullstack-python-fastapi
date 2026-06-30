def calculate_discount(price, discount_percent):
    """
    Calculate the discount amount for a product
    
    Args:
        price: original price (float)
        discount_percent: discount percentage (0-100)
    
    Returns:
        discount amount (float)
    """

    calculate = price * (discount_percent / 100)
    return calculate
def calculate_final_price(price, discount_percent):
    """
    Calculate the final price after discount
    
    Args:
        price: original price (float)
        discount_percent: discount percentage (0-100)
    
    Returns:
        final price (float)
    """
    price_after_discount = price - calculate_discount(price, discount_percent)
    return price_after_discount
def calculate_with_tax(final_price, tax_percent):
    """
    Add tax to final price
    
    Args:
        final_price: price before tax (float)
        tax_percent: tax percentage (0-100)
    
    Returns:
        price with tax (float)
    """
    tax_amount = final_price * (tax_percent / 100)
    return final_price + tax_amount
# Get product info
price = float(input("Enter product price: "))
discount_percent = float(input("Enter discount percentage (0-100): "))
tax_percent = float(input("Enter tax percentage (0-100): "))

# Calculate
final_price = calculate_final_price(price, discount_percent)
total_with_tax = calculate_with_tax(final_price, tax_percent)

# Display
print(f"\nOriginal price: ${price:.2f}")
print(f"Discount ({discount_percent}%): ${calculate_discount(price, discount_percent):.2f}")
print(f"Price after discount: ${final_price:.2f}")
print(f"Tax ({tax_percent}%): ${total_with_tax - final_price:.2f}")
print(f"Final price: ${total_with_tax:.2f}")