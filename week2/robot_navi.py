def navi():
    print("Please enter a whole number.")

    input_val = input()

    if not input_val:
        return navi()
    if input_val == ("up"):
        print(f"I am moving in {input_val} direction")
    elif input_val == ("down"):
        print(f"I am moving in {input_val} direction")
    elif input_val == ("left"):
        print(f"I am moving in {input_val} direction")
    elif input_val == ("right"):
        print(f"I am moving in {input_val} direction")
    else:
        print("Unknown direction")


navi()
