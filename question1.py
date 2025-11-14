# Store items and prices in a dictionary
item_prices = {
    "Bread": 25,
    "Milk": 18,
    "Eggs": 2.5,
    "Sugar": 20
}

# Dictionary to store quantities the user will input
item_quantities = {}

print("Please enter the quantity for each item: ")

# Using a for loop to ask user for quantities
for item, price in item_prices.items():
    quantity = int(input(f"How many {item} do you want to buy? "))
    item_quantities[item] = quantity

# calculate subtotal
subtotal = 0
for item, quantity in item_quantities.items():
    cost = item_prices[item] * quantity
    subtotal += cost


# calculate the discount
discount = 0
if subtotal > 100:
    discount = subtotal * 0.10

# calculate total
total = subtotal - discount


# Print receipt
print("\n----- RECEIPT -----")
for item, quantity in item_quantities.items():
    cost = item_prices[item] * quantity
    print(f"{item} (x{quantity}): GHS {cost:.2f}")
print("-------------------")
print(f"Subtotal: GHS {subtotal:.2f}")
print(f"Discount: GHS {discount:.2f}")
print(f"Total: GHS {total:.2f}")