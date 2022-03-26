from python_algorithm.LinkedList import LList
from python_algorithm.LinkedList import LNode
from python_algorithm.LinkedList import LinkedListUnderFLow
from random import randint


class DoubleList(LList):

    """
    This class is an extension of regular linked list as it points to both the head and rear of the linked list, which
    simplifies some operations for linked list operations.
    """

    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._rear is None:
            raise LinkedListUnderFLow("No element to remove!")
        elif self._head == self._rear:
            elem = self._head.elem
            self._head = None
            self._rear = None
            return elem
        else:
            elem = self._rear.elem
            iter_indicator = self._head
            while iter_indicator.next != self._rear:
                iter_indicator = iter_indicator.next
            iter_indicator.next = None
            self._rear = iter_indicator
            return elem


if __name__ == "__main__":
    mlist1 = DoubleList()
    mlist1.prepend(99)
    for i in range(11, 20):
        mlist1.append(randint(1, 20))

    for x in mlist1.filter(lambda y: y % 2 == 0):
        print(x)
    print(mlist1)
    print(mlist1.pop_last())
