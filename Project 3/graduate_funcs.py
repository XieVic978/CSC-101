# Project 3 – Graduate Rate (2017-2018)
# Name: victor
# Instructor: Dr. S. Einakian
# Section:
# classes and functionalities will be provided here

# Create class Division

class Division:
    def __init__(self, id, division_name):
        self.id = id
        self.division_name = division_name

    def __repr__(self):
        return f"Division(ID: {self.id}, Division: {self.division_name})"




# Create class Graduate
class Graduate:
    def __init__(self, id, major, bachelor:tuple, master:tuple, doctor:tuple):
        self. id = id
        self. major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __repr__(self):
        return f'Graduate(id:{self.id}, major: {self.major}, bachelor: {self.bachelor}, master: {self.master}, doctor: {self.doctor})'

    def __eq__(self, other):
        return(self is other or type(other) == Graduate
               and self.bachelor == other.bachelor
               and self.master == other.master
               and self.doctor == other.doctor)

'''
# Design Recipe
#input: string of files
#output: tuple of 2 lists
#purpose: To read all of the files in the graduate_rate.csv
#Step 1) open the file
2) make a new list
3) loop through the all the files
4) append each line into the new list
5) the headers is first 3 so slice is to get first 3 
6) the data is everything else so everything after 3
7)close the file and then return the tuple with 2 lists
'''
# read file and return list of strings
#
def read_file(file_name: str) -> tuple[list[str], list[str]]:
    """
    Reads a CSV file and returns headers and data.
    Input: file_name - string name of the CSV file
    Output: tuple (headers as list of strings, data as list of strings)
    """
    newList = []
    file = open(file_name,'r')
    for line in file:
        newList.append(line)
    file.close()

    header = newList[:3]
    data = newList[3:]

    return header,data




'''
# Design Recipe
Input: list_str - list of strings, each representing a line from graduate_rate.csv
    Output: list of strings, each containing a division row (id and division_name)
    Purpose: Extract division information from CSV data by identifying rows with IDs 
             divisible by 100 and greater than 3000
    Steps:
        1) Clean each row by splitting on commas and removing empty strings
        2) Loop through each cleaned row
        3) Check each item in the row to see if it's a number
        4) If number is divisible by 100 and > 3000, join the row back into a string
        5) Add the joined string to the result list and break to avoid duplicates
        6) Return the list of division row strings
'''
# create list of Division objects


def get_ID_Division(list_str:list[str])->list[str]:

    newList = []
    for item in list_str:
        parts = item.strip().split(',')
        newList.append(parts)

    newList2 = []
    for val in newList:
        get_id = val[0]
        if get_id[-2:]=='00':
            newList2.append(val)
    return newList2

def create_division(list_str: list[str])-> list[Division]:
    division_list = get_ID_Division(list_str)
    newList = []
    for item in division_list:
        id = item[0]
        division_name = item[1]
        newList.append(Division(id,division_name))
    return newList



# create list of Graduate objects
'''
# Design Recipe for create_graduate
Input: list_str - list of strings, each representing a line from graduate_rate.csv
Output: list of Graduate objects
Purpose: Extract graduate/major information from CSV data and create Graduate objects
         for each major (rows with IDs NOT ending in '00')
Steps:
    1) Call helper function get_Graduate() to filter rows that don't end in '00'
    2) Initialize empty list to store Graduate objects
    3) Loop through each filtered graduate row
    4) Split the row by commas and strip whitespace from each part
    5) Check if row has at least 8 parts (id, major, 6 numeric values)
    6) Extract data:
       - id: first part
       - major: second part
       - bachelor tuple: (female count, male count) from parts 2 and 3
       - master tuple: (female count, male count) from parts 4 and 5
       - doctor tuple: (female count, male count) from parts 6 and 7
    7) Create Graduate object with extracted data and append to list
    8) Handle any ValueError or IndexError exceptions (skip invalid rows)
    9) Return list of Graduate objects
'''

def get_Graduate(list_str:list[str]):
    newList = []
    for item in list_str:
        parts = item.split(',')
        if len(parts) > 0:
            num = parts[0].strip()
            if len(num) >= 2 and num[-2:] != '00':
                newList.append(item)
    return newList

def create_graduate (list_str: list[str])-> list[Graduate]:
    new_graduateList = []
    graduateList = get_Graduate(list_str)

    for line in graduateList:
        try:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 8:
                id = parts[0]
                major = parts[1]
                bachelor = (int(parts[2]), int(parts[3]))
                master = (int(parts[4]), int(parts[5]))
                doctor = (int(parts[6]), int(parts[7]))
                new_graduateList.append(Graduate(id, major, bachelor, master, doctor))
        except (ValueError, IndexError):
            continue
    return new_graduateList



# Design Recipe
'''
input: list[Division], list[Graduate]
output: none
purpose: to create 4 files of each division and inputting the ids, majors, total bachelors, masters, and doctors
example: Division("3200", "Agriculture operations and related sciences")
Division("3400", "Computer and information sciences and support services")
Division("3600", "Education")
Division("3800", "Engineering technologies/construction trades/mechanics and repairers")
lst_grad_obj
Graduate("3201", "Crop Science", [120, 5], [30, 2], [10, 1])
Graduate("3202", "Animal Science", [140, 3], [25, 1], [8, 2])
Graduate("3401", "Software Engineering", [300, 10], [90, 4], [15, 1])
Graduate("3601", "Curriculum & Instruction", [110, 0], [40, 3], [6, 1])
Graduate("3801", "Construction Technology", [90, 2], [20, 1], [4, 0])

Agriculture.csv
"This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18"
id,major,bachelor,master,doctor
3201,"Crop Science",125,32,11
3202,"Animal Science",143,26,10
Computer.csv
"This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18"
id,major,bachelor,master,doctor
3401,"Software Engineering",310,94,16
Education.csv
"This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18"
id,major,bachelor,master,doctor
3601,"Curriculum & Instruction",110,43,7
Engineering.csv
"This table shows Bachelor's, master's, and doctor's degrees conferred by postsecondary institutions, of student and discipline division: 2017-18"
id,major,bachelor,master,doctor
3801,"Construction Technology",92,21,4

steps:
1) loop through each division in list division
2) split the name of the division in each list and get the first word and concatenate csv with it 
3) use with open to write a new file depending on the filename
4) write the headers
5) loop through each graduate object in graduate list
6) get id, major, bachelor, master, and doctor and give them variables
7) if the first 2 strings of graduate is the same as first 2 string of division then write to the file 
8) continue until all files are written 
'''
# create files for each division
def create_files (lst_div_obj: list[Division], lst_grad_obj: list[Graduate]):

    for division in lst_div_obj:
        division_words = division.division_name.split()
        filename = division_words[0]+'.csv'
        with open(filename, 'w') as file:
            file.write('"This table shows Bachelor\'s, master\'s, and doctor\'s degrees conferred by postsecondary institutions, of student and discipline division: 2017-18"\n')
            file.write('id,major,bachelor,master,doctor\n')


            for graduate in lst_grad_obj:

                if graduate.id[:2]==division.id[:2]:
                    id = graduate.id
                    major = graduate.major
                    bachelor = str(graduate.bachelor[0] + graduate.bachelor[1])
                    master = str(graduate.master[0] + graduate.master[1])
                    doctor = str(graduate.doctor[0] + graduate.doctor[1])

                    file.write(f'{id},{major},{bachelor},{master},{doctor}\n')

















