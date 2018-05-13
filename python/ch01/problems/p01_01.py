"""
Problem 1.1

Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""


def is_unique_1(chars):
    """
        Uses an additional data structure (a set)
        Problem says nothing about whether whether upper and lower case
        letters are the same.

        Complexity: O(n)
    """
    s = set()
    for c in chars:
        if c in s:
            return False
        s.add(c)
    return True


def is_unique_2(chars):
    """
        No additional data structures, but carries some performance overhead
        for sorting string. 

        Complexity O(n log n)
    """
    chars_sorted = sorted(chars)
    for i in range(len(chars_sorted) - 1):
        if chars_sorted[i] == chars_sorted[i + 1]:
            return False
    return True
