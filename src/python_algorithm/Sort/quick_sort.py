from python_algorithm.Sort.record import Record
from typing import List


def quick_sort_recursion(lst, start, end):
    if start >= end:
        return

    small_list_start = start
    large_list_start = end

    pivot = lst[small_list_start]
    empty_lot = small_list_start

    is_pointer_front = False
    while small_list_start <= large_list_start:

        if is_pointer_front and lst[small_list_start] <= pivot:
            small_list_start += 1

        elif is_pointer_front and lst[small_list_start] > pivot:
            lst[empty_lot] = lst[small_list_start]
            empty_lot = small_list_start
            small_list_start += 1
            is_pointer_front = False

        elif is_pointer_front is False and lst[large_list_start] > pivot:
            large_list_start -= 1

        else:
            lst[empty_lot] = lst[large_list_start]
            empty_lot = large_list_start
            large_list_start -= 1
            is_pointer_front = True

    if empty_lot != start:
        lst[empty_lot] = pivot

    quick_sort_recursion(lst, start, empty_lot - 1)
    quick_sort_recursion(lst, empty_lot + 1, end)


def quick_sort(lt: List[Record]):
    quick_sort_recursion(lt, 0, len(lt) - 1)


# Driver code to test above
if __name__ == "__main__":
    test = [8, 9, 1, 7, 6, 8, 20, 8, 5, 7, 6, 7, 8, 11, 20, 60, 55, 42, 35, 66, 5, 4]
    quick_sort(test)
    print(test)
