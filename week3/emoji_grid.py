# Nested 1 - Emoji grid: print a grid of emojis with the given rows and columns.
rows = int(input("How many rows should I have?\n"))
cols = int(input("How many columns should I have?\n"))

print("Here I go:")
# outer loop builds each row
for row in range(rows):
    # inner loop prints one emoji per column on the same line
    for col in range(cols):
        print("😁", end=" ")
    # move to the next line after a row is finished
    print()

print("Done!")
