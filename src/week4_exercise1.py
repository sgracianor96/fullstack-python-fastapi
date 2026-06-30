products = [
    {"id": 1, "name": "Laptop", "price": 999, "rating": 4.5, "in_stock": True},
    {"id": 2, "name": "Smartphone", "price": 699, "rating": 4.7, "in_stock": False},
    {"id": 3, "name": "Tablet", "price": 499, "rating": 4.2, "in_stock": True}
]

def validate_inputs(budget, min_rating):
    """Validate user inputs"""
    if budget < 0:
        return False
    if min_rating < 0 or min_rating > 5:
        return False
    return True

def is_product_match(product, budget, min_rating, in_stock_only):
    """Check if product matches all criteria"""
    # Check price and rating
    if product["price"] <= budget and product["rating"] >= min_rating:
        # If we need in-stock only, check that too
        if in_stock_only and not product["in_stock"]:
            return False
        return True
    return False

def filter_products(products, budget, min_rating, in_stock_only):
    """Filter products that match criteria"""
    matching_products = []
    for product in products:
        if is_product_match(product, budget, min_rating, in_stock_only):
            matching_products.append(product)
    return matching_products

def print_results(products, filtered_products):
    """Print all products with YES/NO status"""
    count = 0
    print(f"\nProducts matching your criteria:")
    for product in products:
        if product in filtered_products:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - YES")
            count += 1
        else:
            print(f"- {product['name']}: ${product['price']} (Rating: {product['rating']}) - NO")
    print(f"\nFound {count} product(s) that match your criteria.")

# ===== MAIN FLOW (this was missing!) =====
budget = int(input("Enter your budget: "))
min_rating = float(input("Enter minimum rating: "))
stock_status = input("Show only in-stock items? (yes/no): ").lower()

# Validate inputs
if not validate_inputs(budget, min_rating):
    print("Invalid input. Please enter valid budget and rating values.")
else:
    # Filter products
    in_stock_only = stock_status == "yes"
    filtered = filter_products(products, budget, min_rating, in_stock_only)
    
    # Print results
    print_results(products, filtered)