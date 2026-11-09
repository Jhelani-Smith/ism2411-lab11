# ISM2411 Lab 11
# Reflection 1:
# I would use .get() when I don't have a dictionary key. I would use
# bracket notation when I know I have a dictionary 
#my rule of thumb is deciding based on if I have a dictionry key

# Reflection 2:
# Building a summary dictionary reminds me of using a Pivot
# Table in ExcelPython is more useful for large datasets because it can 
# automate the process and involve less human interaction






# Exercise 1: One Customer

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)

# Exercise 2: Update and Add

# Add a phone number
customer["phone"] = "555-123-4567"
print(customer)

# Update the customer's tier
customer["tier"] = "platinum"
print(customer)

# Delete the email field
del customer["email"]
print(customer)

# Exercise 3: Safe Lookup

# Use .get() to look up the deleted email
print(customer.get("email", "no email on file"))

# Use bracket notation and catch the KeyError
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# Exercise 4: Iterate

# Print every key:value pair
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), Python loops through keys only
for key in customer:
    # This loop returns keys, not key:value pairs
    print(key)

# Exercise 5: Lookup Table

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", tier)
print("Discount rate:", discount * 100, "%")
print("Final price: $", round(final_price, 2))

# Exercise 6: List of Dicts

dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [dict1, dict2, dict3]

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"Name: {person['name']} | "
        f"Tier: {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )

    # Exercise 7: Nested Catalog

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} "
            f"- Only {details['stock']} remaining!"
        )

        # Exercise 8: Sales by Region

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")