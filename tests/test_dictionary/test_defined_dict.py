import unittest
from python_algorithm.DictAndSet.Dict import DictList, DictOrdList
from python_algorithm.Sort.record import Record


class DictTest(unittest.TestCase):

    lst = [6, 7, 4, 4, 2, 8, 1]

    def test_dict_list(self):
        dict1 = DictList()
        for i, j in enumerate(DictTest.lst):
            dict1.insert(j, i)
        self.assertEqual(dict1.search(7), 1)

    def test_ordered_dict_list(self):
        dict2 = DictOrdList()
        for i, j in enumerate(DictTest.lst):
            dict2.insert(j, i)
        self.assertEqual(dict2.search(7), 1)


if __name__ == "__main__":
    unittest.main()
