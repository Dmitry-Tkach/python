# One parameter, two different calls.

# plan is the parameter: it receives the value given in each call
def escape_by(plan):
    print("Plan:", plan)


# each call passes a different argument to the same function
escape_by("jumping over")
escape_by("cross bridge ahead")
