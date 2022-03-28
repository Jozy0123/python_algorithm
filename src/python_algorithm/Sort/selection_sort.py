from python_algorithm.Sort.record import Record
from typing import List


def selection_sort(lst: List[Record]) -> List[Record]:

    sorted_index = len(lst) - 1

    while sorted_index > 0:
        current_max = lst[sorted_index]
        cur_max_index = 0
        i = 0

        while i < sorted_index:
            if lst[i] > current_max:
                cur_max_index = i
                current_max = lst[i]
            i += 1

        print(cur_max_index, current_max.data, [i.data for i in lst])

        if current_max > lst[sorted_index]:
            lst[sorted_index], lst[cur_max_index] = lst[cur_max_index], lst[sorted_index]
        sorted_index -= 1

    return lst


if __name__ == "__main__":
    lst = [6, 7, 4, 4, 2, 8, 1]
    lt = []
    for i in lst:
        lt.append(Record(i, i))
    print([i.data for i in selection_sort(lt)])
