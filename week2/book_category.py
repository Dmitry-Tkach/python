def book_category():
    print("What type of book is this?")

    input_val = input()

    if not input_val:
        return book_category()

    if input_val == "adventure":
        print("I like adventure book")

    elif input_val == "mystery":
        print("I like mystery book")

    else: print("I do not like unknow book")

    print("Finished reading book")


book_category()
