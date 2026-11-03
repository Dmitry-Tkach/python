# Return a value: get_name sends the name back to the caller.

def get_name():
    print("Please enter your name")
    name = input()
    # return passes the value back to where the function was called
    return name


# the call get_name() is replaced by the returned name
print("Retrieved name:", get_name())
