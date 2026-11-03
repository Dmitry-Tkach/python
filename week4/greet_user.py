# Define and call a function: a reusable greeting.

# def creates the function; the indented lines are its body
def greet_user():
    print("Please enter your name")
    name = input()
    print("Hello", name)


# calling the function by name runs its body
greet_user()
