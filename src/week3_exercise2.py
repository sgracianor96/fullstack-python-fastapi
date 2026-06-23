product = {
    "id": 1,
    "name": "Laptop",
    "price": 999,
    "rating": 4.5,
    "in_stock": True,
    "description": "High-performance laptop"
}
print(f"=== Product Inventory Manager ===")
print(f"Current product: {product}")
exit_program = False
while not exit_program:
    action = int(input(
    "\nChoose an action:\n"
    "  1. View product\n"
    "  2. Update price\n"
    "  3. Update rating\n"
    "  4. Add feature\n"
    "  5. Remove feature\n"
    "  6. Check if key exists\n"
    "  7. List all keys\n"
    "  8. Exit\n"
    "Enter choice: "
))
    if action == 1:
        print(f"Product details: {product}")
    elif action == 2:
        new_price = float(input("Enter new price: "))
        product["price"] = new_price
        print(f"Product updated: price is now {product['price']}")
    elif action == 3:
        new_rating = float(input("Enter new rating: "))
        product["rating"] = new_rating
        print(f"Product updated: rating is now {product['rating']}")
    elif action == 4:
        new_feature = input("Enter feature name: ")
        product[new_feature] = input(f"Enter value for {new_feature}: ")
        print(f"Added {new_feature}: {product[new_feature]}")
    elif action == 5:
        feature_to_remove = input("Enter feature to remove: ")
        if feature_to_remove in product:
            del product[feature_to_remove]
            print(f"Feature removed. New product details: {product}")
        else:
            print(f"Feature '{feature_to_remove}' does not exist.")
    elif action == 6:
        key_to_check = input("Enter key to check: ")
        if key_to_check in product:
            print(f"Key '{key_to_check}' exists in the product.")
        else:
            print(f"Key '{key_to_check}' does not exist in the product.")
    elif action == 7:
        print(f"All keys in the product: {list(product.keys())}")
    elif action == 8:
        exit_program = True     
print("Goodbye!")