
from problems.ch01.p04 import palindrome_permutation_1

def test_implementation_is_correct():
    s1 = 'Tact Coa'
    s2 = 'hello'
    s3 = 'r ac ec ar'
    assert palindrome_permutation_1(s1)
    assert not palindrome_permutation_1(s2)
    assert palindrome_permutation_1(s3)
