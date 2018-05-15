
from problems.ch01.p02 import check_permutation_1, check_permutation_2

def test_both_implementations_are_correct():
    s1 = 'qwerty'
    s2 = 'ytrewq'
    s3 = 'HELLO'
    s4 = 'HHELLO'
    assert check_permutation_1(s1, s2)
    assert not check_permutation_1(s1, s3)
    assert not check_permutation_1(s3, s4)
    assert check_permutation_2(s1, s2)
    assert not check_permutation_2(s1, s3)
    assert not check_permutation_2(s3, s4)
