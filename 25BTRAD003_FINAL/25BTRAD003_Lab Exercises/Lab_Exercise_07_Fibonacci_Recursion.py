def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
terms = int(input("Number of terms: "))
if terms < 0: print("Enter a non-negative number.")
else:
    for i in range(terms): print(fibonacci(i), end=" ")
    print()
