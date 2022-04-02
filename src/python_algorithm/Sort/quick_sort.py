from python_algorithm.Sort.record import Record
from typing import List


def quick_sort(lst: List[Record]) -> List[Record]:
    quick_sort_recursion(lst, 0, len(lst)-1)


def quick_sort_recursion(lst, start, end):
    if start >= end:
        return

    small_list_start = start
    large_list_start = end

    pivot = lst[small_list_start]
    empty_lot = small_list_start

    is_pointer_front = False
    while small_list_start < large_list_start:
        if is_pointer_front:
            if lst[small_list_start] <= pivot:
                small_list_start += 1
                continue
            elif lst[small_list_start] > pivot:
                lst[empty_lot] = lst[small_list_start]
                empty_lot = small_list_start
                small_list_start += 1
                is_pointer_front = False
                continue
        else:
            if lst[large_list_start] >= pivot:
                large_list_start -= 1
                continue
            elif lst[large_list_start] < pivot:
                lst[empty_lot] = lst[large_list_start]
                empty_lot = large_list_start
                large_list_start -= 1
                is_pointer_front = True
                continue

    lst[empty_lot] = pivot
    quick_sort_recursion(lst, start, empty_lot-1)
    quick_sort_recursion(lst, empty_lot+1, end)


if __name__ == "__main__":
    lst = [8, 9, 1, 7, 6, 8, 20]
    quick_sort(lst)
