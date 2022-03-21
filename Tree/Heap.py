from PriorityQueue import PriorityQueueError


class Heap:

    def __init__(self, elist=None):
        if elist is None:
            elist = []
        self._elems = list(elist)  # copy elements to a new variable and avoid using the same list, extend to iterable
        if len(self._elems) > 0:
            self.build_heap()

    def is_empty(self):
        return len(self._elems) == 0

    def peek(self):
        if self.is_empty():
            raise PriorityQueueError("empty heap")
        else:
            return self._elems[0]

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, 2 * begin + 1
        elems[i] = e
        while j < end:
            while j + 1 < end and elems[j+1] < elems[j]:
                j += 1
            if elems[i] < elems[j]:
                elems[i], elems[j] = elems[j], elems[i]
            else:
                break
            i, j = j, j * 2 + 1

    def enqueue(self, elem):
        if self.is_empty():
            self._elems.append(elem)
        else:
            self._elems.append(elem)
            index = len(self._elems)
            parent_index = (index - 1) // 2
            while self._elems[parent_index] <= self._elems[index]:
                self._elems[parent_index], self._elems[index] = self._elems[index], self._elems[parent_index]
                if parent_index == 0:
                    break
                else:
                    index = parent_index
                    parent_index = index // 2

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError("Empty PriorityQueue")
        if len(self._elems) == 1:
            self._elems = []
            return self._elems[0]
        self._elems[0] = self._elems[-1]
        elem = self._elems.pop()
        self.siftdown(elem)

    def build_heap(self):
        for i in self._elems:
            self.siftdown(i, 0, len(self._elems))


if __name__ == "__main__":
    h = Heap([1, 5, 43, 24, 45, 65])
    print(h._elems)

