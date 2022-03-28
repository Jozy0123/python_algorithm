from python_algorithm.Sort.record import Record
from typing import List


def insertion_sort(lst: List[Record]) -> List[Record]:
    sorted_index = len(lst) - 1

    for i in range(len(lst)-2, -1, -1):
        current_elem = lst[i]
        j = sorted_index

        while j < len(lst):
            if current_elem > lst[j]:
                lst[j-1] = lst[j]
                j += 1
            else:
                break

        lst[j-1] = current_elem
        sorted_index -= 1

    return lst


if __name__ == "__main__":
    lst = [6, 7, 4, 4, 2, 8, 1]
    lt = []
    for i in lst:
        lt.append(Record(i, i))
    print([i.data for i in insertion_sort(lt)])
