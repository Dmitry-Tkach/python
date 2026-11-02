# While 3 - Battery ASCII: show the battery charging one bar at a time.
print("How many bars should be charged?")
bars = int(input())
charged = 0

while charged < bars:
    # add a bar first, then draw the current charge level
    charged += 1
    print("Charging:", " ".join(["█"] * charged))

print("The battery is fully charged.")
