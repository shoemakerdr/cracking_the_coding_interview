"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def one_away_1(s1, s2):
    calc_index = (lambda i, count: i) if len(s1) == len(s2) else (lambda i, count: i + count)
    str1 = min(s1, s2, key=len)
    str2 = max(s2, s1, key=len)
    count = 0
    for i,c in enumerate(str1):
        if not c == str2[calc_index(i, count)]:
            count += 1
        if count > 1:
            return False
    return True

