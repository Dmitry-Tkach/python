# Validate a character: show the ASCII code of exactly one character.
letter = input("Please enter a letter: ")

# len checks that exactly one character was entered
if len(letter) == 1:
    # ord returns the numeric code of the character
    print(f"ASCII: {ord(letter)}")
else:
    # handles empty input or more than one character
    print("Enter one character.")
