
def checkForInt(val):
    if not val.isdigit():
        return print("Please enter a number")


def counters():
    even = 0
    odd = 0
    
    def checkEvenOdd(val):
        nonlocal even, odd
        val = int(val)
        if val % 2 == 0:
            even += 1
        else: odd += 1

    for i in range(3):
        print((f"Please enter the {i+1} number."))
        firstVal = input()
        checkForInt(firstVal)
        checkEvenOdd(firstVal)


    print(f"There were {even} even and {odd} odd numbers.")


counters()
