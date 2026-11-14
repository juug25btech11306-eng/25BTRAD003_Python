while True:
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        km = float(input("Enter distance in kilometers: "))
        miles = km * 0.621371
        print("Distance in Miles =", round(miles, 2))
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print("Temperature in Fahrenheit =", round(fahrenheit, 2))
    elif choice == "3":
        kg = float(input("Enter weight in kilograms: "))
        pounds = kg * 2.20462
        print("Weight in Pounds =", round(pounds, 2))
    elif choice == "4":
        print("Exiting Unit Converter.")
        break
    else:
        print("Invalid Choice!")
