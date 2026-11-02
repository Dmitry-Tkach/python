# While 2 - Obstacle counter: avoid obstacles and report progress after each one.
print("How many obstacles must I avoid?")
obstacles = int(input())
count = 0

while count < obstacles:
    # print without a newline so the progress appears on the same line
    print("Avoiding...", end="")
    count += 1
    print(f"Done! {count} obstacles avoided.")

print("All obstacles have been avoided.")
