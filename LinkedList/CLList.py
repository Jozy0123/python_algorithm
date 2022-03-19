from LinkedList import LNode


class LCList:

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def printall(self):
        p = self._rear
        if p is None:
            return
        while True:
            if p.next is not self._rear:
                p = p.next
                print(p.elem)
            else:
                break
        p = p.next
        print(p.elem)

    def find(self, pred):
        if self._rear is None:
            return
        p = self._rear
        while True:
            p = p.next
            if pred(p.elem):
                return p.elem
            if p is self._rear:
                break
        if pred(p.elem):
            return p.elem
        else:
            return

    def pop(self):
        if self._rear is None:
            return
        if self._rear == self._rear.next:
            p = self._rear.elem
            self._rear = None
            return p
        else:
            elem = self._rear.next.elem
            self._rear.next = self._rear.next.next
            return elem

    def interleaving(self, another):
        p = self._rear.next
        head = self._rear.next
        while True:
            elem = another._rear.next.elem
            if elem is not None:
                if p is self._rear:
                    p.next = another._rear.next
                    another._rear.next = head
                    self._rear = another._rear
                    return
                p.next = LNode(another.pop(), p.next)
                p = p.next.next
            else:
                break
            if another._rear is None:
                return

    # def del_minimal(self):
    #     if self._rear is None:
    #         return
    #     p = self._rear
    #     min = self._rear.elem
    #     n = 0
    #     while p.next is not None:
    #         p = p.next
    #         if p is self._rear:
    #             break
    #         if p.elem < min:
    #             min = p.elem
    #             n += 1


if __name__ == "__main__":
    test = LCList()
    test.prepend(5)
    test.prepend(4)
    test.prepend(3)
    test.prepend(2)
    another_test = LCList()
    another_test.prepend(7)
    another_test.prepend(8)
    test.interleaving(another_test)
    test.printall()
