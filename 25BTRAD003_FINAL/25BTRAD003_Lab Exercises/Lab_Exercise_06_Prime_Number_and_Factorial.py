n = int(input("Enter a number to check prime: "))
prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0: prime = False; break
print(n, "is prime" if prime else "is not prime")
x = int(input("Enter a number for factorial: "))
if x < 0: print("Factorial is not defined for negative numbers.")
else:
    fact = 1
    for i in range(1, x + 1): fact *= i
    print("Factorial:", fact)
