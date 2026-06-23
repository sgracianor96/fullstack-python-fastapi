products = [
    {"id": 1, "name": "Laptop", "price": 999, "rating": 4.5, "in_stock": True},
    {"id": 2, "name": "Phone", "price": 799, "rating": 4.8, "in_stock": True},
    {"id": 3, "name": "Headphones", "price": 199, "rating": 4.2, "in_stock": False},
    {"id": 4, "name": "Monitor", "price": 399, "rating": 4.6, "in_stock": True},
    {"id": 5, "name": "Keyboard", "price": 99, "rating": 4.1, "in_stock": True}
]
count = 0
budget = int(input("Enter your budget: "))
min_rating = float(input("Enter minimum rating: "))
stock_status = input("Show only in-stock items? (yes/no): ").lower()
while budget < 0 or min_rating < 0 or min_rating > 5:
    print("Invalid budget or rating. Please enter a non-negative budget and a rating between 0-5.")
    budget = int(input("Enter your budget: "))
    min_rating = float(input("Enter minimum rating: "))
print(f"Products that match your criteria:")
for product in products:
    if product["price"] <= budget and product["rating"] >= min_rating:
        if stock_status == "yes" and not product["in_stock"]:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - NO (out of stock)")
        else:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - YES")
            count = count + 1
    else:
        if product["price"] > budget and product["rating"] < min_rating:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - NO (too expensive and rating too low)")
        elif product["price"] > budget:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - NO (too expensive)")
        elif product["rating"] < min_rating:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - NO (rating too low)")
print(f"Found {count} product(s) that match your criteria.")