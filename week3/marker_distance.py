# Nested 2 - Marker distance: count the characters between two markers.
sequence = input("Please enter a sequence\n")
marker = input("Please enter the character for the marker\n")

first = -1      # -1 means the first marker has not been found yet
distance = 0

for position in range(len(sequence)):
    if sequence[position] == marker:
        if first == -1:
            # found the first marker
            first = position
        else:
            # found the second marker: characters in between
            distance = position - first - 1
            break

print(f"The distance between the markers is {distance}.")
