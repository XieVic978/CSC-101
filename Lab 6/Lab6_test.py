import Lab6
from Lab6 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = Lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = Lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = Lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = Lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        Lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_sorting_books(self):
        lst = [Book(["jay"],"Warriors"), Book(["May"],"Man Nice")]
        expected = [Book(["May"],"Man Nice"), Book(["jay"],"Warriors")]
        Lab6.selection_sort_books(lst)
        self.assertEqual(expected,lst)
    def test_sorting_books2(self):
            book1 = Book("Author A", "Zebra Tales")
            book2 = Book("Author B", "Apple Stories")
            book3 = Book("Author C", "Middle Book")
            books = [book1, book2, book3]
            expected = [book2, book3, book1]
            selection_sort_books(books)
            self.assertEqual(expected, books)

    def test_selection_sort_books_empty(self):
        books = []
        expected = []
        selection_sort_books(books)
        self.assertEqual(expected, books)
    # Part 2
    def test_swap_case(self):
        word = 'Whats up man'
        result = swap_case(word)
        expected = 'wHATS UP MAN'
        self.assertEqual(expected,result)

    def test_swap_case_non_english_letters(self):
        input_str = "Café MÜNCHEN naïve"
        expected = "cAFÉ münchen NAÏVE"
        result = swap_case(input_str)
        self.assertEqual(expected, result)

    def test_swap_case_mixed_with_numbers_and_symbols(self):
        input_str = "HeLLo123!@#WoRLD$%^"
        expected = "hEllO123!@#wOrld$%^"
        result = swap_case(input_str)
        self.assertEqual(expected, result)

    def test_swap_case_empty_string(self):
        input_str = ""
        expected = ""
        result = swap_case(input_str)
        self.assertEqual(expected, result)

    def test_swap_case_only_symbols(self):
        input_str = "123 !@# $%^ &*()"
        expected = "123 !@# $%^ &*()"
        result = swap_case(input_str)
        self.assertEqual(expected, result)


    # Part 3
    def test_str_translate(self):
        string = 'abcdcba'
        result = str_translate(string, 'a', 'x')
        expected = 'xbcdcbx'
        self.assertEqual(expected,result)
    def test_str_translate(self):
        string = 'mama'
        result = str_translate(string, 'a', 'x')
        expected = 'mxmx'
        self.assertEqual(expected,result)

    def test_no_occurrence(self):
        result = str_translate('hello', 'z', 'q')
        self.assertEqual(result, 'hello')

    def test_mixed_case(self):
        result = str_translate('Apple and apricot', 'a', 'x')
        self.assertEqual(result, 'Apple xnd xpricot')

    def test_empty_string(self):
        result = str_translate('', 'a', 'x')
        self.assertEqual(result, '')



    # Part 4

    def test_histogram(self):
        string = 'hey bro hey man how you doing'
        expected = {'hey': 2, 'bro':1,'man':1,'how':1,'you':1,'doing':1}
        result = histogram(string)
        self.assertEqual(expected, result)

    def test_basic_counting(self):
        text = "cat dog cat fish dog dog"
        expected = {"cat": 2, "dog": 3, "fish": 1}
        self.assertEqual(histogram(text), expected)

    def test_empty_string(self):
        self.assertEqual(histogram(""), {})





if __name__ == '__main__':
    unittest.main()
