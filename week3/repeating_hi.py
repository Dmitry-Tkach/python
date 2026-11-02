# While 4 - Repeating Hi: print "Hi" once for every character in the phrase.
print("Please enter a phrase:")
phrase = input()
count = 0

# len() counts every character, including spaces
while count < len(phrase):
    print("Hi", end=" ")
    count += 1

# finish the line
print()
