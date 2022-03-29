import unittest
from python_algorithm.Sort.selection_sort import selection_sort
from python_algorithm.Sort.record import Record


class SelectionSort(unittest.TestCase):

    def test_sort(self):
        lst = [6, 7, 4, 4, 2, 8, 1]
        lst = [Record(i, i) for i in lst]
        sorted_lst = [1, 2, 4, 4, 6, 7, 8]
        self.assertEqual(selection_sort(lst), [Record(i, i) for i in sorted_lst])


if __name__ == "__main__":
    unittest.main()