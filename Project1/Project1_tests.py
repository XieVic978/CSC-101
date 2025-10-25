# Name:Victor
# Section:

from Project1 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count1(self):
        str1 = 'This is a test for vowels'
        expected = 7
        self.assertEqual(expected, vowel_count(str1))

    def test_vowel_count2(self):
        str1 = 'Brother find AeIoU'
        expected = 8
        self.assertEqual(expected,vowel_count(str1))

    def test_vowel_count(self):
        str1 = 'What does AEIOU mean tho?'
        expected = 11
        result = vowel_count(str1)
        self.assertEqual(expected,result)

    # Part 2
    def test_long_lists1(self):
        list1 = [[1,2,3],[4,5,6]]
        expected = [[1,2,3],[4,5,6]]
        self.assertEqual(expected,long_list(list1))

    def test_long_lists2(self):
        list1 = [[2,3],[432,65,231,765],[],[5435,43,232,32,32,32]]
        expected = [[432,65,231,765],[5435,43,232,32,32,32]]
        self.assertEqual(expected,long_list(list1))


    def test_short_lists3(self):
        list1 = [[],[],[3,3],[333,33,3333]]
        expected = [[333,33,3333]]
        self.assertEqual(expected,long_list(list1))

    # Part 3
    def test_decending_pairs1(self):
        lst = [[12, 2, 3], [10, 2], [-9, 0, 9, 78], [15, 6], [1, 2]]
        expected = [[12, 2, 3], [10, 2], [-9, 0, 9, 78], [15, 6], [2,1]]
        self.assertEqual(expected,descending_pairs(lst))

    def test_decending_pairs2(self):
        lst = [[12, 2, 3], [10, 2, 0], [-9, 0, 9, 78], [1, 5, 6]]
        expected = [[12, 2, 3], [10, 2, 0], [-9, 0, 9, 78], [1, 5, 6]]
        self.assertEqual(expected,descending_pairs(lst))

    def test_decending_pairs3(self):
        lst = [[1,2],[0,100000],[1,2,3],[3]]
        expected = [[2,1],[100000,0],[1,2,3],[3]]
        self.assertEqual(expected,descending_pairs(lst))

    # Part 4
    def test_Price_add1(self):
        price1 = Price(3,75)
        price2 = Price(2,50)
        expected = Price(6,25)
        result = add_prices(price1,price2)
        self.assertEqual(expected,result)

    def test_Price_add2(self):
        price1 = Price(5, 106)
        price2 = Price(16, 1008)
        expected = Price(32,14)
        result = add_prices(price1, price2)
        self.assertEqual(expected, result)

    def test_Price_add3(self):
        price1 = Price(3, 1)
        price2 = Price(2, 1)
        expected = Price(5, 2)
        result = add_prices(price1, price2)
        self.assertEqual(expected, result)

    def test_Price_add3(self):
        p1 = Price(2, 100)
        p2 = Price(3, 100)
        expected = Price(7, 0)
        result = add_prices(p1, p2)
        self.assertEqual(expected, result)

    # Part 5
    def test_perimeter1(self):
        rect = Rectangle(Point(1, 1), Point(2, 0))
        expected = 4.0
        result = rectangle_perimeter(rect)
        self.assertEqual(expected,result)

    def test_perimeter2(self):
        rect = Rectangle(Point(1,5),Point(-12,6))
        expected = 28
        result = rectangle_perimeter(rect)
        self.assertEqual(expected,result)

    # Part 6

    def test_negative_quadrant_1(self):
        points = [Point(2, -1), Point(-1, -7), Point(0, 5), Point(-9, -3)]
        expected = [Point(-1,-7),Point(-9,-3)]
        result = are_in_negative_quadrant(points)
        self.assertEqual(expected,result)

    def test_negative_quadrant_2(self):
        points = [Point(-1,-2),Point(2,4),Point(-6,-20),Point(-10,-50),Point(432,432)]
        expected = [Point(-1,-2),Point(-6,-20),Point(-10,-50)]
        result = are_in_negative_quadrant(points)
        self.assertEqual(expected,result)

    # Part 7
    def test_circle_bound_1(self):
        rec = Rectangle(Point(-5, 20), Point(12, 10))
        expected = (Circle(Point(3.5,15.0),math.sqrt(((12-3.5)**2) + ((10 - 15)**2))))
        result = circle_bound(rec)
        self.assertAlmostEqual(expected,result)
    def test_circle_bound_2(self):
        rec = Rectangle(Point(-10,20),Point(10,-15))
        expected = Circle(Point(0,2.5),math.sqrt(((10-0)**2) + ((-15-2.5)**2)))
        result = circle_bound(rec)
        self.assertEqual(expected,result)
    def test_circle_bound_3(self):
        rec = Rectangle(Point(-4, 2), Point(-1, -1))
        expected = (Circle(Point(-2.5, 0.5), 2.1213203435596424))
        result = circle_bound(rec)
        self.assertEqual(expected,result)

    # Part 8
    def test_higher_than_average1(self):
        emps = [Employee('Sam', 3000.0), Employee('Tom', 5000.0),
                Employee('Mary', 4000.0)]

        expected = ['Tom']
        result = higher_than_average(emps)
        self.assertEqual(expected,result)

    def test_higher_than_average2(self):
        emps = [Employee('Sam', 4000.0), Employee('Tom', 4000.0),
                Employee('Mary', 4000.0)]
        expected = []
        result=higher_than_average(emps)
        self.assertEqual(expected,result)

    def test_higher_than_average(self):
        emps = [Employee('Victor',50000), Employee('Ryan',80000),Employee('Malic',80000),
                Employee('John',100),Employee('Yitong',2)]
        expected = ['Victor','Ryan','Malic']
        result = higher_than_average(emps)
        self.assertEqual(expected,result)

    def test_higher_than_average3(self):
        emps = []
        expected = []
        result = higher_than_average(emps)
        self.assertEqual(expected, result)




if __name__ == '__main__':
    unittest.main()
