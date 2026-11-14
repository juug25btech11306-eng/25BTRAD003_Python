import random
secret = random.randint(1, 100)
print("Guess a number between 1 and 100")
while True:
    try: guess = int(input("Your guess: "))
    except ValueError:
        print("Enter a whole number."); continue
    if guess < secret: print("Too low!")
    elif guess > secret: print("Too high!")
    else:
        print("Congratulations! Correct guess.")
        break
