# While 5 - Sum 1 to 100: add every number from 1 to 100.
print("Calculating the sum of the first 100 numbers...")
total = 0
number = 1

# <= makes sure 100 itself is included
while number <= 100:
    total += number
    number += 1

print(f"...Done! The answer is {total}.")
