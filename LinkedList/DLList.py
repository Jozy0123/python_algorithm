from LinkedList import LinkedListUnderFLow
from LinkedList import LNode
from DoubleLinkedList import DoubleList


class DLNode(LNode):

    def __init__(self,
                 elem,
                 prev_node=None,
                 next_node=None):
        LNode.__init__(self, elem, next_node)
        self.prev_node = prev_node


class DLList(DoubleList):

    def __init__(self):
        DoubleList.__init__(self)

    def prepend(self, elem):
        node = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = node
        else:
            node.next.prev = node
        self._head = node





