# For 6 - Direct character iteration: print each character on its own line.
print("What phrase do you want to print?")
phrase = input()

print("outputting...")
print("The phrase is:")
# "for ... in" visits each character directly, no index needed
for char in phrase:
    print(char)
