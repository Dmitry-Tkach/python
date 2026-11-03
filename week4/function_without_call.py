# What happens without a call? Defining a function does not run it.

# the function is created in memory, but its body does not run yet
def greet_user():
    print("Hello")

# No greet_user() call here, so this program prints nothing
