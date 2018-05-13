"""
Problem 1.2

Check Permutation: Given two strings, write a method to decide if one is a
permutation of the other.

The problem does not address whether lowercase letter would be different
than uppercase of the same letter.
"""


def check_permutation_1(s1, s2):
    """
    Naive implementation.

    Complexity: O(n log n)
    """
    return sorted(s1) == sorted(s2)


def check_permutation_2(s1, s2):
    """
    Faster implementation creates frequency tables for both strings after
    checking that they have the same length. Uses helper function.

    Complexity: O(n + m)
    """
    if len(s1) is not len(s2):
        return False
    freq1 = make_frequency(s1)
    freq2 = make_frequency(s2)
    for c in freq1:
        if freq1[c] is not freq2[c]:
            return False
    return True


def make_frequency(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq
