products = [
    {"id": 1, "name": "Laptop", "price": 999, "rating": 4.5},
    {"id": 2, "name": "Phone", "price": 699, "rating": 4.7},
    {"id": 3, "name": "Tablet", "price": 499, "rating": 4.2},
    {"id": 4, "name": "Headphones", "price": 199, "rating": 4.8},
    {"id": 5, "name": "Monitor", "price": 399, "rating": 4.6}
]

def display_products(products):
    """Display all products in a formatted manner"""
    print("\n=== Available Products ===")
    for product in products:
        print(f"ID {product['id']}: {product['name']} - ${product['price']} (Rating: {product['rating']})")

def add_to_cart(product_id, quantity, cart, products):
    """Add a product to the cart"""
    for product in products:
        if product["id"] == product_id:
            cart.append({"product": product, "quantity": quantity})
            return cart
    return cart

def calculate_subtotal(cart):
    """Calculate the subtotal of the cart"""
    subtotal = 0
    for item in cart:
        subtotal += item["product"]["price"] * item["quantity"]
    return subtotal

def calculate_total(subtotal, discount_percent, tax_percent):
    """Calculate the total after discount and tax"""
    discount_amount = subtotal * (1 - discount_percent / 100)
    apply_tax = discount_amount * (1 + tax_percent / 100)
    total = apply_tax
    return total

def display_cart(cart):
    """Display the contents of the cart"""
    print("\n=== Your Cart ===")
    total_items = 0
    subtotal = 0
    for item in cart:
        product = item["product"]
        quantity = item["quantity"]
        item_total = product["price"] * quantity
        print(f"- {product['name']} (x{quantity}): ${item_total:.2f}")
        total_items += quantity
        subtotal += item_total
    print(f"\nItems: {total_items} | Subtotal: ${subtotal:.2f}")

# Main program
cart = []
shopping = True

while shopping:
    print("\n=== Shopping Cart System ===")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        display_products(products)
    
    elif choice == "2":
        display_products(products)
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        cart = add_to_cart(product_id, quantity, cart, products)
        print("Added to cart!")
    
    elif choice == "3":
        if len(cart) == 0:
            print("Cart is empty!")
        else:
            display_cart(cart)
    
    elif choice == "4":
        if len(cart) == 0:
            print("Cart is empty! Add items before checkout.")
        else:
            subtotal = calculate_subtotal(cart)
            discount = float(input("Enter discount percentage (0-100): "))
            tax = float(input("Enter tax percentage (0-100): "))
            total = calculate_total(subtotal, discount, tax)
            
            print(f"\nSubtotal: ${subtotal:.2f}")
            print(f"Discount: ${subtotal * (discount/100):.2f}")
            print(f"Tax: ${(subtotal * (1 - discount/100)) * (tax/100):.2f}")
            print(f"Total: ${total:.2f}")
            print("Thank you for your purchase!")
            cart = []
            shopping = False
    
    elif choice == "5":
        shopping = False
    
    else:
        print("Invalid choice!")

print("Goodbye!")