# For 1 - ASCII mountains: draw a mountain as many times as the user asks.
print("How many mountains should I display?")
mountains = int(input())

print("Displaying...")
# range(mountains) repeats the body once per mountain
for count in range(mountains):
    print('    __')
    print('   /  \\_')
    print('  /^    \\')
    print(' /  ^     \\')
    print('/_^_^____^_\\')

print("Done!")
