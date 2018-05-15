
from problems.ch01.p03 import urlify_1

def test_implementation_is_correct():
    s1 = 'Mr John Smith      '
    s2 = 'H i   '
    s3 = '   '
    assert urlify_1(s1, 13) == 'Mr%20John%20Smith'
    assert urlify_1(s2, 3) == 'H%20i'
    assert urlify_1(s3, 1) == '%20'
