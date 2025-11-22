# Project 3 Graduate Rate (2017-2018)
# Name:
# Instructor: Dr. S. Einakian
# Section: 

# unittest cases for graduate rate will include here
# At least two test cases for each function
import unittest

from graduate_funcs import *

class TestCases(unittest.TestCase):

    def test_read_file_1(self):
        """Test that read_file returns proper tuple structure"""
        # Create a test file
        with open('test_data.csv', 'w') as f:
            f.write("UNITID,INSTNM,STABBR\n")
            f.write("Institution Name,State\n")
            f.write("Data for 2017-2018\n")
            f.write("4000,Engineering\n")
            f.write("4001,Mechanical,100,50,20,10,5,2\n")

        headers, data = read_file('test_data.csv')

        self.assertEqual(len(headers), 3)
        self.assertEqual(len(data), 2)
        self.assertTrue(headers[0].startswith("UNITID"))

        # Clean up
        import os
        os.remove('test_data.csv')

    def test_read_file_2(self):
        """Test that headers and data are separated correctly"""
        with open('test_data2.csv', 'w') as f:
            f.write("Header1\n")
            f.write("Header2\n")
            f.write("Header3\n")
            f.write("Data1\n")
            f.write("Data2\n")

        headers, data = read_file('test_data2.csv')

        self.assertEqual(headers[0].strip(), "Header1")
        self.assertEqual(data[0].strip(), "Data1")
        self.assertEqual(len(data), 2)

        import os
        os.remove('test_data2.csv')
    def test_create_division1(self):
        test_data = [
            "UNITID,INSTNM,STABBR\n",
            "Institution Name,State\n",
            "Data for 2017-2018\n",
            "4000,Engineering and Technology\n",
            "4001,Mechanical Engineering,450,425,180,165,45,40\n",
            "4002,Electrical Engineering,380,360,210,195,55,50\n",
            "4003,Civil Engineering,290,275,125,115,30,28\n",
            "5000,Computer Science\n",
            "5001,Software Engineering,520,500,240,225,60,55\n",
            "5002,Data Science,410,395,190,180,42,38\n",
            "5003,Cybersecurity,335,320,155,145,35,32\n",
            "6000,Business Administration\n",
            "6001,Finance,680,650,310,290,70,65\n",
            "6002,Marketing,590,570,270,255,48,45\n",
            "6003,Management,510,490,230,215,52,48\n",
            "7000,Health Sciences\n",
            "7001,Nursing,720,695,340,320,85,78\n",
            "7002,Public Health,445,425,205,195,50,46\n",
            "7003,Medical Technology,380,365,175,165,40,37\n"
        ]
        divisions = create_division(test_data)

        self.assertEqual(len(divisions), 4)
        self.assertEqual(divisions[0].id, '4000')
        self.assertEqual(divisions[0].division_name, 'Engineering and Technology')

    def test_create_division2(self):
        test_data = [
            "UNITID,INSTNM,STABBR\n",
            "Institution Name,State\n",
            "Data for 2017-2018\n",
            "4000,Engineering and Technology\n",
            "4001,Mechanical Engineering,450,425,180,165,45,40\n",
            "4002,Electrical Engineering,380,360,210,195,55,50\n",
            "4003,Civil Engineering,290,275,125,115,30,28\n",
            "5000,Computer Science\n",
            "5001,Software Engineering,520,500,240,225,60,55\n",
            "5002,Data Science,410,395,190,180,42,38\n",
            "5003,Cybersecurity,335,320,155,145,35,32\n",
            "6000,Business Administration\n",
            "6001,Finance,680,650,310,290,70,65\n",
            "6002,Marketing,590,570,270,255,48,45\n",
            "6003,Management,510,490,230,215,52,48\n",
            "7000,Health Sciences\n",
            "7001,Nursing,720,695,340,320,85,78\n",
            "7002,Public Health,445,425,205,195,50,46\n",
            "7003,Medical Technology,380,365,175,165,40,37\n"
        ]
        divisions = create_division(test_data)
        self.assertEqual(divisions[2].id, '6000')
        self.assertEqual(divisions[2].division_name, 'Business Administration')

    def test_create_graduate(self):
        graduate = Graduate(100,'Computer Science',(1000,5000),(65,78),(6,7))
        graduate2 = Graduate(100,'Computer Science',(1000,5000),(65,78),(6,7))
        self.assertEqual(graduate,graduate2)

    def test_create_graduate2(self):
        test_data = [
            "UNITID,INSTNM,STABBR\n",
            "Institution Name,State\n",
            "Data for 2017-2018\n",
            "4000,Engineering and Technology\n",
            "4001,Mechanical Engineering,450,425,180,165,45,40\n",
            "4002,Electrical Engineering,380,360,210,195,55,50\n",
            "4003,Civil Engineering,290,275,125,115,30,28\n",
            "5000,Computer Science\n",
            "5001,Software Engineering,520,500,240,225,60,55\n",
            "5002,Data Science,410,395,190,180,42,38\n",
            "5003,Cybersecurity,335,320,155,145,35,32\n",
            "6000,Business Administration\n",
            "6001,Finance,680,650,310,290,70,65\n",
            "6002,Marketing,590,570,270,255,48,45\n",
            "6003,Management,510,490,230,215,52,48\n",
            "7000,Health Sciences\n",
            "7001,Nursing,720,695,340,320,85,78\n",
            "7002,Public Health,445,425,205,195,50,46\n",
            "7003,Medical Technology,380,365,175,165,40,37\n"
        ]
        graduates = create_graduate(test_data[3:])
        for grad in graduates:
            self.assertFalse(grad.id.endswith('00'),
                             f"Graduate ID {grad.id} should not end in '00'")


    # Run the unit tests.

if __name__ == '__main__':
    unittest.main()
