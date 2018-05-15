
from .linked_list import LinkedList


"""
Problem 2.1

Remove Dups: Write code to remove duplicates from an unsorted linked list. How would you
solve this problem if a temporary buffer is not allowed?
"""

def remove_dups_1(l):
    s = set()
    p = l
    while p is not None and p.next is not None:
        s.add(p.value)
        if p.next.value in s:
            p.next = p.next.next
        p = p.next
    return l

def remove_dups_2(l):
    p1 = l
    while p1 is not None:
        p2 = p1
        while p2 is not None and p2.next is not None:
            if p1.value == p2.next.value:
                p2.next = p2.next.next
            p2 = p2.next
        p1 = p1.next
    return l


