import random
num_dice = int(input("Enter number of dice: "))
num_rolls = int(input("Enter number of rolls: "))
if num_dice <= 0 or num_rolls <= 0:
    print("Please enter positive numbers!")
else:
    frequency = {i: 0 for i in range(1, 7)}
    for roll in range(num_rolls):
        results = []
        for _ in range(num_dice):
            value = random.randint(1, 6); results.append(value); frequency[value] += 1
        print("Roll", roll + 1, ":", results)
    print("\nFrequency of Outcomes:")
    for number, count in frequency.items(): print(number, "appeared", count, "times")
    print("Total outcomes:", sum(frequency.values()))
