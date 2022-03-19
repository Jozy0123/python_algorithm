from LinkedList import LinkedListUnderFLow
from LinkedList import LNode
from DoubleLinkedList import DoubleList


class DLNode(LNode):

    def __init__(self,
                 elem,
                 prev_node=None,
                 next_node=None):
        LNode.__init__(self, elem, next_node)
        self.prev_node = prev_nodev


class DLList(DoubleList):

    def __init__(self):
        DoubleList.__init__(self)

    def prepend(self, elem):
        node = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = node
        else:
            node.next.prev_node = node
        self._head = node

    def append(self, elem):
        node = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = node
            self._rear = node
        else:
            self._rear = node
            node.next.prev_node = node

    def pop(self):
        if self._head is None:
            raise LinkedListUnderFLow("in popping element from the front end")
        elif self._head == self._rear:
            elem = self._head.elem
            self._head = None
            self._rear = None
            return elem
        else:
            elem = self._head.next.elem
            self._head = self._head.next
            self._head.prev_node = None
            return elem

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderFLow("in popping the last element")
        elif self._head == self._rear:
            elem = self._head.elem
            self._head = None
            self._rear = None
            return elem
        else:
            elem = self._rear.elem
            self._rear = self._rear.prev_node
            self._rear.next = None
            return elem











