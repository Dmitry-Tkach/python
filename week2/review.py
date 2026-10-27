def castle_adventure():
    print("Which door should I open (red, blue or green)?")
    door = input().strip().lower()

    if door == "red" or door == "blue":
        print("Do I have a key (yes or no)?")
        key = input().strip().lower()
        print("Is there a guard (yes or no)?")
        guard = input().strip().lower()

        if key == "yes" and not guard == "yes":
            print("I unlocked the treasure room!")
        elif key == "yes" and guard == "yes":
            print("The guard caught me before I could use the key!")
        else:
            print("The door is locked. I need a key.")
    elif door == "green":
        print("The green door leads back outside. Adventure over!")
    else:
        print("There is no such door. I will stay where I am.")


castle_adventure()
