"""
Problem 1.3

Urlify: Write a method to replace all spaces in a string with '%20: You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use a character array so that you can perform this
operation in place.)

In Python, string are IMMUTABLE, so you cannot modify in place. Therefore, my
solution returns a new string. This would be different in the case of Java or
C/C++.
"""


def urlify_1(s, count):
    new_s = ''
    space = '%20'
    for i,c in enumerate(s):
        if i == count:
            return new_s
        new_s += space if c == ' ' else c
    return new_s
