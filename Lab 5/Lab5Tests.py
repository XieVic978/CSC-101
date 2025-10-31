# Name:
# Section:
#########################################################

import unittest

from Lab5 import *

# Write your test cases for each part below.

class TestCases(unittest.TestCase):


# Task 1
    def testX(self):
        list1 = [Point(1,2),Point(2,4),Point(8,9)]
        expected = [1,2,8]
        result = x_coordinates(list1)
        self.assertEqual(expected,result)


    def test_x_coordinates_basic(self):
        points = [Point(1, 2), Point(3, 4), Point(-2, 5)]
        self.assertEqual(x_coordinates(points), [1, 3, -2])


    def test_x_coordinates_empty(self):
        points = []
        self.assertEqual(x_coordinates(points), [])

# Task 2
    def test_quadrant(self):
        list1 = [Point(-1,2),Point(-10,-8),Point(10,24),Point(1,-2),Point(1,2),Point(-1,0),Point(8,2),]
        expected = [Point(10,24),Point(1,2),Point(8,2)]
        result = are_in_positive_quadrant(list1)
        self.assertEqual(expected,result)


    def test_quadrant2(self):
        points = [Point(-1, 2), Point(3, -4), Point(-2, -3)]
        result = are_in_positive_quadrant(points)
        self.assertEqual(result, [])
# Task 3

    def test_distance1(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertAlmostEqual(distance(p1, p2), 5.0)


    def test_distance2(self):
        p1 = Point(-1, -1)
        p2 = Point(2, 3)
        self.assertAlmostEqual(distance(p1, p2), 5.0)


# Task 4
    def test_manhattan_distance1(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertAlmostEqual(manhattan_distance(p1, p2), 7.0)


    def test_manhattan_distance2(self):
        p1 = Point(-2, 5)
        p2 = Point(3, -1)
        self.assertAlmostEqual(manhattan_distance(p1, p2), 11.0)


    def test_distance_all1(self):
        points = [Point(0, 0), Point(3, 4), Point(1, -2)]
        result = distance_all(points)
        self.assertEqual(result, [0.0, 7.0, 3.0])  # using Manhattan distance


    def test_distance_all2(self):
        points = [Point(-1, -1), Point(2, 5), Point(-3, 4)]
        result = distance_all(points)
        self.assertEqual(result, [2.0, 7.0, 7.0])  # using Manhattan distance


# Task 5

# Task 6
#    Part 1 tests should be in data_tests.py.

# Task 7
#    Part 2 tests should be in data_tests.py.


# Task 8
    def test_Time(self):
        time = Time(2,58,45)
        time2 = Time(3,52,57)
        result = time_add(time,time2)
        expected = Time(6,51,42)
        self.assertEqual(expected,result)


    def test_Time2(self):
        time = Time(2, 58, 45)
        time2 = Time(3, 52, 57)
        result = time_add(time, time2)
        expected = Time(6, 51, 42)
        self.assertEqual(expected, result)


    def test_Time_no_second_carry(self):
        t1 = Time(0, 0, 0)
        t2 = Time(0, 0, 1)
        result = time_add(t1, t2)
        expected = Time(0, 0, 1)
        self.assertEqual(expected, result)


# Task 9
    def test_descending(self):
        list1 = [5.4,4,3.2,2,1]
        expected = True
        result = is_descending(list1)
        self.assertEqual(expected,result)

    def test_descending2(self):
        list1 = [5,4,3,3.2,3,1,2,3]
        expected = False
        result = is_descending(list1)
        self.assertEqual(expected,result)


    def test_descending_empty_list(self):
        list1 = []
        expected = True
        result = is_descending(list1)
        self.assertEqual(expected, result)


# Task 10

    def test_largest_between(self):
        list1 = [10,20,40,20,50,60]
        result = largest_between(list1, 1,5)
        expected = 5
        self.assertEqual(expected,result)


    def test_LargestBetween_1(self):
        nums = [3, 8, 2, 10, 5]
        result = largest_between(nums, 1, 4)
        expected = 3
        self.assertEqual(expected, result)


    def test_LargestBetween_2(self):
        nums = [4, 7, 1, 9]
        result = largest_between(nums, 3, 1)
        expected = None
        self.assertEqual(result, expected)


    def test_negative_lower_is_out_of_bounds(self):
        nums = [10, 20, 30, 40]
        result = largest_between(nums, 0, 3)
        self.assertEqual(3,result)


    def test_largest_between_all_negative_numbers(self):
        list1 = [-5, -10, -3, -20]
        result = largest_between(list1, 0, 3)
        expected = 2  # Index 2 has -3, which is the largest
        self.assertEqual(expected, result)


# Task 11
    def test_furthest_from_Org(self):
        list1 = [Point(0,1),Point(10,20),Point(-4,9),Point(-50,-90)]
        expected = 3
        result = furthest_from_origin(list1)
        self.assertEqual(expected,result)


    def test_FurthestFromOrigin_1(self):
        points = [Point(1, 2), Point(3, 4), Point(-5, 12)]
        result = furthest_from_origin(points)
        expected = 2
        self.assertEqual(expected, result)


    def test_FurthestFromOrigin_2(self):
        points = []
        result = furthest_from_origin(points)
        expected = None
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
