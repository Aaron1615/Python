from node import Node
from unordered_list import Unordered_list

def is_cyclic(linked_list):
    """Returns whether or not the linked list is cyclic."""
    slow = linked_list.head
    fast = linked_list.head
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False