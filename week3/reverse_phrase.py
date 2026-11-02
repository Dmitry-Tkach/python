# For 5 - Reverse phrase: print a phrase backwards one character at a time.
print("What phrase do you want to see in reverse?")
phrase = input()

print("Reversing...")
print("The phrase is: ", end="")
# start at the last index, stop after index 0, move backwards
for pos in range(len(phrase) - 1, -1, -1):
    print(phrase[pos], end="")

# finish the line
print()
