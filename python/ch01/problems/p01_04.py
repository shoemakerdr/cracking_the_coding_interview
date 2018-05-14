"""
Problem 1.4

Palindrome Permutation: Given a string, write a function to check if it is a
permutation of a palin- drome. A palindrome is a word or phrase that is the
same forwards and backwards. A permutation is a rearrangement of letters.The
palindrome does not need to be limited to just dictionary words.
"""


def palindrome_permutation_1(s):
    freq = make_frequency_table(s.lower())
    odd_count = 0
    print(freq)
    for c in freq:
        if freq[c] % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


def make_frequency_table(s):
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        elif not c == ' ':
            freq[c] = 1
    return freq
