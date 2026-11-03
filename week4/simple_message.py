# Entry-point guard: protect code from running when the file is imported.

def simple_message():
    print("Welcome to COM411!")


# __name__ is "__main__" only when this file is run directly
if __name__ == "__main__":
    simple_message()
