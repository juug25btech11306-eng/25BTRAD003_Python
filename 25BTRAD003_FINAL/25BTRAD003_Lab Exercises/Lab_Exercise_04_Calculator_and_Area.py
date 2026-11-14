while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Square 6.Rectangle 7.Circle 0.Exit")
    c = input("Choice: ")
    if c == "0":
        break
    if c in ("1", "2", "3", "4"):
        a, b = float(input("First number: ")), float(input("Second number: "))
        if c == "1": print("Result:", a + b)
        elif c == "2": print("Result:", a - b)
        elif c == "3": print("Result:", a * b)
        elif b == 0: print("Cannot divide by zero.")
        else: print("Result:", a / b)
    elif c == "5":
        s = float(input("Side: ")); print("Area:", s * s)
    elif c == "6":
        l, w = float(input("Length: ")), float(input("Breadth: "))
        print("Area:", l * w)
    elif c == "7":
        r = float(input("Radius: ")); print("Area:", 3.14159 * r * r)
    else: print("Invalid choice")
