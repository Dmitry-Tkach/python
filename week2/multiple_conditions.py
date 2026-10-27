def mini_adventure():
    print("What type of adventure should I have?")

    adventure = input()

    if adventure == "scary" or adventure == "short":
        print("Entering the dark forest!")
    elif adventure == "safe" or adventure == "long":
        print("Taking the safe route!")
    else:
        print("Not sure which route to take.")


mini_adventure()


def dark_forest():
    print("What did I hear?")
    heard = input()

    print("What did I see?")
    saw = input()

    if heard == "grrr" and saw == "two red eyes":
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue!")


dark_forest()
