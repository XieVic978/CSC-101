from group import *
import unittest


class TestCases(unittest.TestCase):
    def test_group_of_3(self):
        list1 = [1,2,3,4,5,6,7,8,9]
        expected = [[1,2,3],[4,5,6],[7,8,9]]
        result = groups_of_3(list1)
        self.assertEqual(expected,result)

    def test_group_of_3_1(self):
        list1 = [1,2,3,4,5,6,7,8]
        expected = [[1,2,3],[4,5,6],[7,8]]
        result = groups_of_3(list1)
        self.assertEqual(expected,result)