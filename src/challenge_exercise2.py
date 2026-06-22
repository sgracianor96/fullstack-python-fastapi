product_names = ["Laptop", "Phone", "Headphones", "Monitor", "Keyboard"]
product_prices = [999, 799, 199, 399, 99]
product_ratings = [4.5, 4.8, 4.2, 4.6, 4.1]
count = 0
budget = int(input("Enter your budget: "))
min_rating = float(input("Enter minimum rating: "))
while budget < 0 or min_rating < 0 or min_rating > 5:
    print("Invalid budget or rating. Please enter a non-negative budget and a rating between 0-5.")
    budget = int(input("Enter your budget: "))
    min_rating = float(input("Enter minimum rating: "))
print(f"Products that match your criteria:")
for i in range(len(product_prices)):
    if product_prices[i] <= budget and product_ratings[i] < min_rating:
        print(f"- {product_names[i]}: ${product_prices[i]} (Rating: {product_ratings[i]}) - NO (rating too low)")
    elif product_prices[i] > budget and product_ratings[i] >= min_rating:
        print(f"- {product_names[i]}: ${product_prices[i]} (Rating: {product_ratings[i]}) - NO (too expensive)")
    elif product_prices[i] > budget and product_ratings[i] < min_rating:
        print(f"- {product_names[i]}: ${product_prices[i]} (Rating: {product_ratings[i]}) - NO (too expensive and rating too low)")
    else: 
        print(f"- {product_names[i]}: ${product_prices[i]} (Rating: {product_ratings[i]}) - YES")
        count = count + 1
print(f"Found {count} product(s) that match your criteria.")