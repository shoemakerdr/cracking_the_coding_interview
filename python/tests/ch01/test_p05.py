
from problems.ch01.p05 import one_away_1

def test_implementation_is_correct():
    s1 = 'pale'
    s2 = 'ple'
    s3 = 'pales'
    s4 = 'pale'
    s5 = 'pale'
    s6 = 'bale'
    s7 = 'pale'
    s8 = 'bake'
    assert one_away_1(s1, s2)
    assert one_away_1(s3, s4)
    assert one_away_1(s5, s6)
    assert not one_away_1(s7, s8)
