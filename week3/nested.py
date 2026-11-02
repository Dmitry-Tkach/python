# Nested loops: print the numbers 0-9 three times on one line.
# outer loop repeats the whole row 3 times
for count in range(0, 3, 1):
    # inner loop prints the numbers 0 to 9
    for number in range(0, 10, 1):
        print(f"{number} |", end="")
