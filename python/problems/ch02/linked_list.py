
class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self._position = self

    def __iter__(self):
        return self.copy()

    def __next__(self):
        if self._position is None:
            raise StopIteration
        next = self._position
        self._position = next.next
        return next.value

    def append(self, value):
        if self.next is None:
            self.next = LinkedList(value)
        else:
            self.next.append(value)
        return self

    def copy(self):
        new_list = LinkedList(self.value)
        next = self.next
        while next is not None:
            new_list.append(next.value)
            next = next.next
        return new_list
