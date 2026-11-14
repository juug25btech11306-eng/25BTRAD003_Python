items = []
total = 0.0

print("=" * 40)
print("       BILL GENERATOR")
print("=" * 40)

while True:
    item = input("\nEnter Item Name: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Item: Rs."))

    amount = quantity * price
    total += amount
    items.append([item, quantity, price, amount])

    choice = input("\nDo you want to add another item? (yes/no): ").lower()
    if choice != "yes":
        break

gst = total * 0.18
grand_total = total + gst

print("\n" + "=" * 55)
print("{:<20} {:<10} {:<10} {:<10}".format("Item", "Qty", "Price", "Amount"))
print("=" * 55)

for item_name, quantity, price, amount in items:
    print("{:<20} {:<10} Rs.{:<7.2f} Rs.{:<7.2f}".format(
        item_name, quantity, price, amount
    ))

print("=" * 55)
print(f"Subtotal       : Rs.{total:.2f}")
print(f"GST (18%)      : Rs.{gst:.2f}")
print(f"Grand Total    : Rs.{grand_total:.2f}")
print("=" * 55)

paid = float(input("Amount Paid: Rs."))
if paid >= grand_total:
    print(f"Balance Returned: Rs.{paid - grand_total:.2f}")
else:
    print(f"Amount Due: Rs.{grand_total - paid:.2f}")

print("\nThank you for shopping!")
