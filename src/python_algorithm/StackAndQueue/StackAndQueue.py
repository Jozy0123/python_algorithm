from python_algorithm.LinkedList.LinkedList import LList, LNode


class StackUnderFlow(ValueError):
    pass


class QueueUnderFlow(ValueError):
    pass


class SStack:

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return len(self._elems) == 0

    def top(self):
        if self.is_empty():
            raise StackUnderFlow("in peeking the top element")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("in pop")
        p = self._elems[-1]
        self._elems = self._elems[:-1]
        return p


class LStack:

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderFlow("in peeking the first element")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderFlow("in pop")
        p = self._top.elem
        self._top = self._top.next
        return p

    def __str__(self):
        p = self._top
        lt = []
        if p is None:
            return ''
        while p.next is not None:
            elem = p.elem
            lt.append(elem)
            p = p.next
        lt.append(p.elem)
        return ','.join(lt)


class LQueue(LList):

    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def enqueue(self, elem):
        if self._rear is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def is_empty(self):
        return self._head is None

    def dequeue(self):
        if self._rear is None:
            raise QueueUnderFlow("in dequeue")
        else:
            e = self._head.elem
            if self._head != self._rear:
                self._head = self._head.next
            else:
                self._head = self._rear = None
        return e

    def peek(self):
        if self._head is None:
            raise QueueUnderFlow("in peeking")
        else:
            return self._head.elem


class SQueue:

    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self.is_empty():
            raise QueueUnderFlow("in peeking")
        else:
            return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise QueueUnderFlow("in dequeue")
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._num
        self._num -= 1
        return e

    def enqueue(self, elem):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = elem
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0


if __name__ == "__main__":
    weight_goal = 40
    wlist = [3, 23, 17, 60]
    knap_rec(weight_goal, wlist, 0)
