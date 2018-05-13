
from problems.p01_01 import is_unique_1, is_unique_2

def test_both_implementations_are_correct():
    s1 = 'qwerty'
    s2 = 'qqwerty'
    assert is_unique_1(s1)
    assert is_unique_2(s1)
    assert not is_unique_1(s2)
    assert not is_unique_2(s2)
