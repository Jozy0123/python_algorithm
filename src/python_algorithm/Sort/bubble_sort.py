from python_algorithm.Sort.record import Record
from typing import List


def bubble_sort(lst: List[Record]) -> List[Record]:
    end = len(lst)
    while True:
        found = False
        for i in range(end, 0, -1):
            for j in range(1, i):
                if lst[j-1] > lst[j]:
                    lst[j-1], lst[j] = lst[j], lst[j-1]
                    found = True

        if found is False:
            break

    return lst


if __name__ == "__main__":
    lst = [6, 7, 4, 4, 2, 8, 1]
    lt = []
    for i in lst:
        lt.append(Record(i, i))
    print([i.data for i in bubble_sort(lt)])
