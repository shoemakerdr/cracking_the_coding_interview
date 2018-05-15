
from problems.ch02.p02 import kth_to_last
from problems.ch02.linked_list import LinkedList

def test_implementation_is_correct():
    l1 = LinkedList(1).append(5).append(7).append(2)
    assert kth_to_last(2, l1) == 7
    l2 = LinkedList(1)
    assert kth_to_last(2, l2) == None
    l3 = LinkedList(1).append(5).append(7).append(2)
    assert kth_to_last(1, l3) == 2
    l4 = LinkedList(1).append(5).append(7).append(2)
    assert kth_to_last(4, l4) == 1
