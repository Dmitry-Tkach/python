def checkForInt(val):
    if not val.isdigit():
        return print("Please enter a number")

def find_small():
    print("Please enter the first number.")

    firstVal = input()
    checkForInt(firstVal)

    print("Please enter the second number.")
    secondVal = input()
    checkForInt(secondVal)

    if firstVal < secondVal:
        print(f"{firstVal} is smaller")
    elif firstVal > secondVal:
        print(f"{secondVal} is smaller")
    else:
       print(f"{firstVal} and {secondVal} Both are equal!")


find_small()
