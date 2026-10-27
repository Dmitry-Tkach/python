def even_odd():
    print( "Please enter a whole number.")

    input_val = input()

    if not input_val:
        return even_odd()

    input_val = int(input_val)

    if input_val % 2 == 0:
        print(f"{input_val} it is even")
    else:
       print(f"{input_val} it is odd")


even_odd()
