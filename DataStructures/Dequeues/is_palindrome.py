from Dequeue import Dequeue

def is_palindrome(str):
    """Given a string, this function will return True if
    the string is a palindrome or False if not"""
    container = Dequeue()
    for letter in str:
        container.add_front(letter)
    
    still_equal = True

    while still_equal and container.size() > 1:
        front = container.remove_front()
        back = container.remove_back()
        if back != front:
            still_equal = False
    return still_equal

