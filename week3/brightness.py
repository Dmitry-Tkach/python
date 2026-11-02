# For 3 - Brightness: increase brightness in steps of 2 up to the chosen level.
print("What level of brightness is required?")
level = int(input())

print("Adjusting brightness...")
# start at 2, include the chosen level (level + 1), step by 2
for brightness in range(2, level + 1, 2):
    print("Brightness level:", "*" * brightness)

print("Complete!")
