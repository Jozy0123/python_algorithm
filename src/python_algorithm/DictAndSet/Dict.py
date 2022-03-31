from python_algorithm.DictAndSet.DictABC import DictABC
from python_algorithm.Sort.record import Record


class DictList(DictABC):

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def num(self):
        return len(self._elems)

    def search(self, key):
        for i in self._elems:
            if i.key == key:
                return i.data

    def insert(self, key, value):
        for i in self._elems:
            if i.key == key:
                i.data = value
                return
        self._elems.append(Record(key, value))

    def delete(self, key):
        for i in range(self.num()):
            if self._elems[i].key == key:
                del self._elems[i]
                break

    def values(self):
        for i in self._elems:
            yield i.data

    def entries(self):
        for i in self._elems:
            yield i.key, i.data


class DictOrdList(DictList):

    def __init__(self):
        super().__init__()
        self._elems.sort(key=lambda x: x.key)

    def search(self, key):
        low, high = 0, len(self._elems)-1
        while low <= high:
            mid = low + (high - low) // 2
            if key == self._elems[mid].key:
                return self._elems[mid].data
            elif key > self._elems[mid].key:
                low = mid + 1
            else:
                high = mid - 1

    def insert(self, key, value):
        if self.is_empty():
            self._elems.append(Record(key, value))
            return
        low, high, mid = 0, len(self._elems)-1, 0
        while high >= low:
            mid = low + (high - low) // 2
            if key == self._elems[mid].key:
                self._elems[mid].data = value
                return
            elif key > self._elems[mid].key:
                low = mid + 1
            else:
                high = mid - 1
        if low > high:
            mid = low
        if mid < len(self._elems):
            self._elems.insert(mid, Record(key, value))
        else:
            self._elems.append(Record(key, value))

    def delete(self, key):
        low, high = 0, len(self._elems)-1
        while low <= high:
            mid = low + (high - low) // 2
            if key == self._elems[mid].key:
                del self._elems[mid]
                break
            elif key > self._elems[mid].key:
                low = mid + 1
            else:
                high = mid - 1


if __name__ == '__main__':

    custom_dict = DictOrdList()
    lt = [2, 4, 5, 6, 5, 65]
    for i, j in enumerate(lt):
        custom_dict.insert(j, i)
        custom_dict.delete(4)
        print([i for i in custom_dict.entries()])
