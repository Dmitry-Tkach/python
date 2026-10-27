def nested_book():
    print("What type of cover does the book have?")

    input_val = input()

    if not input_val:
        return nested_book()

    if input_val != "soft" and input_val != "hard":
        print("Please enter only soft or hard")
        return nested_book()

    if input_val == "soft":
        print("Is the book perfect-bound?")
        
        perfect = input()

        if perfect == "yes":
            print("Soft cover, perfect bound books are very popular!")
        else:
            print("Soft covers with coils or stitches are great for short books")
    elif input_val == "hard":
        print("Books with hard covers can be more expensive!")

nested_book()
