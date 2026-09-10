#shopping cart
item = input("What item would you like to purchase?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like to buy?:"))

total = price * quantity
print(f"You have bought {quantity} * {item}/s ")
print(f"That makes you total ${total}")
