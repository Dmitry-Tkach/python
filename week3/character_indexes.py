# For 4 - Character indexes: show each character of a word with its index.
print("What word do you see?")
word = input()

print("Displaying index positions...")
# valid indexes run from 0 to len(word) - 1
for pos in range(0, len(word), 1):
    print(f"index {pos}: {word[pos]}")

print("Done!")
