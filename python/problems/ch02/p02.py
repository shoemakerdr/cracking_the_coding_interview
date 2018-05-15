
"""
Problem 2.2

Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

def kth_to_last(n, l):
    p1 = l
    p2 = l
    while n > 1 and p2.next is not None:
        p2 = p2.next
        n -= 1
    if n > 1:
        return None
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p1.value

