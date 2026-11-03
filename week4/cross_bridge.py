# A function with a loop and a decision.

def cross_bridge(distance):
    # the loop repeats once per step of the bridge
    for step in range(distance):
        print("Crossed step.")
    # the decision picks a message depending on the distance
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


cross_bridge(3)
