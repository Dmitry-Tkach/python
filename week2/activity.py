def activity():
    print("Please enter the activity to be performed.")

    input_value = input()

    if not input_value:
        return activity()

    if input_value == "calculate":
        print("Performing calculations...")
    elif input_value == "activity" :
        print("Performing activity...")
    else: print("Incorrect input value")

    print("Activity completed!")


activity()
