
from problems.ch02.p01 import remove_dups_1, remove_dups_2
from problems.ch02.linked_list import LinkedList

def test_implementation_is_correct():
    l1 = LinkedList(1).append(5).append(1).append(2)
    l2 = LinkedList(1).append(5).append(2)
    assert list(remove_dups_1(l1)) == list(l2)
    assert list(remove_dups_2(l1)) == list(l2)
    l3 = LinkedList(2).append(4).append(5).append(5).append(1).append(2)
    l4 = LinkedList(2).append(4).append(5).append(1)
    assert list(remove_dups_1(l3)) == list(l4)
    assert list(remove_dups_2(l3)) == list(l4)
    l5 = LinkedList(2).append(2)
    l6 = LinkedList(2)
    assert list(remove_dups_1(l5)) == list(l6)
    assert list(remove_dups_2(l5)) == list(l6)
    l7 = LinkedList(2)
    l8 = LinkedList(2)
    assert list(remove_dups_1(l7)) == list(l8)
    assert list(remove_dups_2(l7)) == list(l8)
