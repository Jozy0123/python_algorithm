from python_algorithm.Sort.record import Record
from typing import List


def heap_sort(lst: List[Record]) -> List[Record]:

    def siftdown(lt: List[Record], index: int, end=None):
        if end is None:
            end = len(lst)
        i = index
        while i < end and (i * 2 + 1) < end:
            j = i * 2 + 1
            if j + 1 < end:
                if lt[j + 1] > lt[j]:
                    j = j + 1
            if lt[i] < lt[j]:
                lt[i], lt[j] = lt[j], lt[i]
            else:
                break
            i = j

    for i in range(len(lst) // 2, -1, -1):
        siftdown(lst, i)

    print([i.data for i in lst])

    for i in range(len(lst)-1, 0, -1):
        elem = lst[i]
        lst[i] = lst[0]
        lst[0] = lst[i-1]
        lst[i-1] = elem
        siftdown(lst, 0, i-1)

    return lst


if __name__ == "__main__":
    lst = [6, 7, 4, 4, 2, 8, 1]
    lt = []
    for i in lst:
        lt.append(Record(i, i))
    print([i.data for i in heap_sort(lt)])
