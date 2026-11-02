# While 6 - Sum user numbers: add up as many numbers as the user chooses.
print("How many numbers should I sum up?")
amount = int(input())
total = 0
count = 0

while count < amount:
    # ask for each number, showing its position
    value = int(input(f"Please enter number {count + 1} of {amount}:\n"))
    total += value
    count += 1

print(f"The answer is {total}.")
