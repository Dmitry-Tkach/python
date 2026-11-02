# While 1 - Apple robot: remove as many apples as the user asks for.
print("how many apples do you want to remove?")
input_val = int(input())
removed = 0

# repeat until the requested number of apples has been removed
while(removed < input_val):
    print("Apple removerd")
    # increase the counter so the loop eventually stops
    removed += 1

print(f"Removed {removed}" )
