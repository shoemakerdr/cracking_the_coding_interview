
from problems.ch02.p01 import remove_dups_1

def test_implementation_is_correct():
    l1 = {'value': 1, 'next': {'value': 5, 'next': {'value': 1, 'next': {'value': 2, 'next': None}}}}
    assert remove_dups_1(l1)
