# Prints "iteration 0" to "iteration 9" and then "Completed iteration 10"

count = 0
# keep looping while count is below 10
while(count < 10):
    print("iteration %d" %(count))
    # increase count so the loop eventually stops
    count += 1

print("Completed iteration %d" %(count))
