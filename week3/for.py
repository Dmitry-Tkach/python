# Draws an ASCII face 10 times using range() with one argument.
def forDwawing():
    # range(10) gives 0 to 9, so the face is drawn 10 times
    for count in range(10):
        print("#########")
        print("# #")
        print("# O O #")
        print("| V |")
        print("| --- |")
        print("|_______|")

forDwawing()

# Draws the same face 10 times using range(start, stop, step).
def forWithParam():
    # start at 0, stop before 10, step by 1
    for count in range(0, 10, 1):
        print("#########")
        print("# #")
        print("# O O #")
        print("| V |")
        print("| --- |")
        print("|_______|")


forWithParam()
