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

    def siftdown(self):
        index = 0
        child_index_left = 1
        child_index_right = 2

        while child_index_left <= len(self._elems):
            if len(self._elems) > child_index_right + 1:
                if self._elems[index] <= self._elems[child_index_left] < self._elems[child_index_right]:
                    self._elems[index], self._elems[child_index_right] = self._elems[child_index_right], self._elems[
                        index]
                    index = child_index_right
                    child_index_left = index * 2 + 1
                    child_index_right = index * 2 + 2
                elif self._elems[index] <= self._elems[child_index_right] < self._elems[child_index_left]:
                    self._elems[index], self._elems[child_index_left] = self._elems[child_index_left], self._elems[index]
                    index = child_index_left
                    child_index_left = index * 2 + 1
                    child_index_right = index * 2 + 2

                else:
                    break
            elif self._elems[index] < self._elems[child_index_left]:
                self._elems[index], self._elems[child_index_left] = self._elems[child_index_left], self._elems[index]
            else:
                break

    def dequeue(self):
        if self.is_empty():
            raise PriorityQueueError("Empty PriorityQueue")
        if len(self._elems) == 1:
            self._elems = []
            return self._elems[0]
        elem = self._elems[0]
        self._elems[0] = self._elems[-1]
        self._elems.pop()
        self.siftdown()
        return elem

    def build_heap(self):
        for _ in self._elems:
            self.siftdown()


if __name__ == "__main__":
    h = Heap([1, 5, 43, 24, 45, 65])
    print(h._elems)
    h.siftdown()
    print(h._elems)
