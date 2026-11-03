# Two cooperating functions: one reads a name, the other draws it in a box.

def display_box(name):
    message = f"* Hello {name} *"
    # string multiplication makes a border as wide as the message
    print("*" * len(message))
    print(message)
    print("*" * len(message))


def greet_user():
    print("Please enter your name")
    name = input()
    # call the other function; execution returns here when it ends
    display_box(name)


greet_user()
