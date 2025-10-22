# Your Name:
# Your
import Lab4
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Task 1
    def test_last_element_1(self):
        input = [[1,2], [3,4],[]]
        result = Lab4.last_element(input)
        expected = [2, 4]
        self.assertEqual(expected, result)

    def test_last_element_2(self):

        input = [[67,67,6,7],
                 [1,2],
                 [],
                 [4444,6565654,68]]
        result = Lab4.last_element(input)
        expected = [7,2,68]
        self.assertEqual(expected, result)

        pass


    # Task 2
    def test_pass_fail(self):
        threshold = 75
        students = [[10,100,100],
                    [98,74,100],
                    [99,89,80]]
        result = Lab4.pass_fail(students, threshold)
        expected = ['Fail','Fail','Pass']
        self.assertEqual(expected,result)
    def test_pass_fail2(self):
        threshold = 80
        students = [[89,90,67,89,32,1],
                    [89,67,90,12],
                    [89,534,2],
                    [100,100,100,100,100,1],
                    [81,90,99,89,89,97]]
        result = Lab4.pass_fail(students, threshold)
        expected = ['Fail', 'Fail', 'Fail', 'Fail','Pass']
        self.assertEqual(expected,result)

    # Task 3
    def test_found_notfound(self):
        value = 5
        list1 = [1,2,3,5,1,6]
        result = Lab4.search_value(list1, value)
        expected = 'Found'
        self.assertEqual(expected, result)

    def test_found_notfound2(self):
        value = 'A'
        list1 = ['B','B','C','D','A']
        result = Lab4.search_value(list1, value)
        expected = 'Found'
        self.assertEqual(expected, result)

    # Task 4
    def test_search_any(self):
        value = 1
        list2 = [5,2,3,4,4]
        result = Lab4.search_any(list2, value)
        expected = False
        self.assertEqual(expected, result)


    def test_search_any2(self):
        value = 'Bruhh I bombed my Physics test'
        list2 = ['heklo',None,'What the', 'Bruhh I bombed my Physics test', 100]
        result = Lab4.search_any(list2, value)
        expected = True
        self.assertEqual(expected, result)

    # Task 5
    def test_reverse_val(self):
        value = 'Whats up MAn'
        result = Lab4.reverse_value(value)
        expected = 'nAM pu stahW'
        self.assertEqual(expected, result)

    def test_reverse_val2(self):
        value = [1,2,3,None]
        result = Lab4.reverse_value(value)
        expected = [None,3,2,1]
        self.assertEqual(expected, result)

    def test_reverse_val3(self):
        value = [1,2,3,4,'sfsfds',True,False,None,32423,65,'heyeyeye']
        result = Lab4.reverse_value(value)
        expected = ['heyeyeye',65,32423, None, False,True, 'sfsfds',4,3,2,1]
        self.assertEqual(expected, result)

    def test_reverse_val4(self):
        value = 'Hey, I am doing awesome '
        result = Lab4.reverse_value(value)
        expected = ' emosewa gniod ma I ,yeH'
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
