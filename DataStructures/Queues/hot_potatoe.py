import Queue

def hot_potatoe(names,number):
    """A simulation of the game Hot Potatoe.
    Removes a person every "number" of passes until only one remains,
    then returns that name.

    names = a list of names
    number = the number of passes before the person holding the potatoe
    (at the front of the queue) is removed."""
    circle = Queue.Queue()
    for name in names:
        circle.enqueue(name)
    while circle.size() > 1:
        for index in range(number):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.dequeue()

print(hot_potatoe(["Bill","David","Susan","Jane","Kent","Brad"],7))