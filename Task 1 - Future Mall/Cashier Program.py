products = ["T-Shirt", "Shoes", "Backpack", "Headphones", "Watch"]

prices = [250, 450, 300, 600, 800]

cart = []

print("=" * 35)
print("        FUTURE MALL")
print("          CASHIER")
print("=" * 35)

while True:
    print("\nProducts:")

    for number in range(len(products)):
        print(f"{number + 1}. {products[number]} - {prices[number]} EGP")

    print("6. Checkout")

    choice = input("\nChoose a product: ")

    if choice == "6":
        break

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(products):
        print("Invalid choice. Please try again.")
        continue

    choice = int(choice)
    name = products[choice - 1]
    price = prices[choice - 1]

    quantity = input(f"Enter quantity of {name}: ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity.")
        continue

    quantity = int(quantity)
    total = price * quantity

    cart.append((name, price, quantity, total))

    print(f"{quantity} x {name} added to cart.")
    print(f"Item total: {total} EGP")

print("\n" + "=" * 35)
print("          FINAL RECEIPT")
print("           FUTURE MALL")
print("=" * 35)

if len(cart) == 0:
    print("No products purchased.")
else:
    total_price = 0

    for name, price, quantity, total in cart:
        print(f"{name}")
        print(f"  {quantity} x {price} EGP = {total} EGP")
        total_price += total

    print("-" * 35)
    print(f"Total before discount: {total_price} EGP")

    if total_price > 500:
        discount = total_price * 0.10
        final_price = total_price - discount

        print("Congratulations!")
        print("You received a 10% discount.")
        print(f"Discount: {discount:.2f} EGP")
        print(f"Your current price: {final_price:.2f} EGP")
    else:
        final_price = total_price
        print(f"Your current price: {final_price:.2f} EGP")

    print("=" * 35)
    print("       Thank you for shopping!")
    print("=" * 35)
