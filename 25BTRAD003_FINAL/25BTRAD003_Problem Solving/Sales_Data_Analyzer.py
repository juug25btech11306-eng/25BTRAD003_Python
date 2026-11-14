sales_data = {
    "Laptop": {"quantity": 10, "price": 45000},
    "Mobile": {"quantity": 20, "price": 15000},
    "Headphones": {"quantity": 30, "price": 2000},
    "Keyboard": {"quantity": 15, "price": 1000}
}

def add_or_update_product():
    name = input("Enter product name: ").title()
    try:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter product price: "))
    except ValueError:
        print("Enter valid numeric values.")
        return

    if name in sales_data:
        sales_data[name]["quantity"] += quantity
        sales_data[name]["price"] = price
        print("Product record updated successfully!")
    else:
        sales_data[name] = {"quantity": quantity, "price": price}
        print("New product added successfully!")

def calculate_total_sales():
    total = sum(details["quantity"] * details["price"] for details in sales_data.values())
    print("\nTotal Sales Revenue: Rs.", total)

def display_sales():
    print("\n---------- PRODUCT SALES REPORT ----------")
    print("{:<15} {:<12} {:<12} {:<12}".format("Product", "Quantity", "Price", "Revenue"))
    for product, details in sales_data.items():
        revenue = details["quantity"] * details["price"]
        print("{:<15} {:<12} {:<12} {:<12}".format(
            product, details["quantity"], details["price"], revenue
        ))

def highest_selling_product():
    if not sales_data:
        print("No product data available.")
        return
    highest = max(sales_data, key=lambda product: sales_data[product]["quantity"])
    print("\nHighest Selling Product:", highest)
    print("Quantity Sold:", sales_data[highest]["quantity"])

def compare_performance():
    print("\n---------- SALES PERFORMANCE ----------")
    sorted_products = sorted(
        sales_data.items(), key=lambda item: item[1]["quantity"], reverse=True
    )
    for product, details in sorted_products:
        revenue = details["quantity"] * details["price"]
        print(product, "- Quantity:", details["quantity"], "| Revenue: Rs.", revenue)

def main():
    while True:
        print("\n====== SALES DATA ANALYZER ======")
        print("1. Add or Update Product")
        print("2. Calculate Total Sales")
        print("3. Display Product-wise Sales")
        print("4. Find Highest-selling Product")
        print("5. Compare Product Performance")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_or_update_product()
        elif choice == "2":
            calculate_total_sales()
        elif choice == "3":
            display_sales()
        elif choice == "4":
            highest_selling_product()
        elif choice == "5":
            compare_performance()
        elif choice == "6":
            print("Thank you for using Sales Data Analyzer!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
