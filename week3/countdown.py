# For 2 - Countdown: count down from the given number of steps to 1.
print("How far are we from the target?")
steps = int(input())

# start at steps, stop before 0, move backwards by 1
for remaining in range(steps, 0, -1):
    print(f"{remaining} steps remaining")

print("Target achieved!")
