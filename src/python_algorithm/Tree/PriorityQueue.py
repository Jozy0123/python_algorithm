from python_algorithm.Tree.Heap import Heap


class PriorityQueueError(ValueError):
    pass


class PriorityQueue:

    def __init__(self, enlist=None):
        if enlist is None:
            enlist = []
        self._elems = enlist
        self._elems.sort(reverse=True)

    def enqueue(self, elem):
        for i in range(len(self._elems)):
            if elem > self._elems[i]:
                self._elems.insert(i, elem)
                return
        self._elems.append(elem)

    def dequeue(self):
        if len(self._elems) == 0:
            raise PriorityQueueError("Empty PriorityQueue")
        self._elems.pop(0)

    def is_empty(self):
        return len(self._elems) == 0

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError("Empty PriorityQueue")
        return self._elems[0]


class PriorityQueueHeap(Heap):

    def __init__(self, enlist=None):
        if enlist is None:
            enlist = []
        super().__init__(enlist)


if __name__ == "__main__":
    lt = [3, 34, 24, 45, 4]
    queue = PriorityQueue(lt)
    print(queue.is_empty())
    print(queue.peek())
    print(queue.enqueue(36))
    print(queue._elems)
    print(queue.dequeue())
    print(queue._elems)
