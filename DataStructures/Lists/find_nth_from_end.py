import unordered_list
import ordered_list

def find_nth_node_from_end(list, n):
    """Given a linked list and a number (n),
    returns the node n numbers away from the end."""

    current = list.head
    accumulator = 1
    if not list.head:
        return None
    else:
        while current.next:
            current = current.next
            accumulator +=1
    stop = accumulator+1 - n
    if not 0 < n < accumulator:
        return None
    accumulator = 1
    current = list.head
    while accumulator < stop:
        current = current.next
        accumulator += 1
    return current
