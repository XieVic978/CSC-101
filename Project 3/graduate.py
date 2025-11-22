# Project 3 Graduate Rate (2017-2018)
# Name: victor
# Instructor: Dr. S. Einakian
# Section:
# main program: You need to call the functions you created in the
# graduate_funcs.py in an order to create the csv files for each division and
# analyzing your data by calling the final two functions and print the results.

from graduate_funcs import *

'''
# Design Recipe 
Input: division_name - string representing the filename of a division CSV
Output: tuple (total_graduates, average_graduates)
Purpose: Calculate total and average number of graduates across all degree levels
         (Bachelor, Master, Doctor) for all majors in the given division
Example: 
    If Agriculture.csv contains:
    3201,Agriculture general,2194,301,14
    3202,Animal sciences,1500,200,10
    Returns: (4219, 2109.5)
Steps:
    1) Open the division CSV file
    2) Skip the 2 header lines, read data lines
    3) For each data line, split by comma and sum columns 2, 3, 4 (Bachelor, Master, Doctor)
    4) Calculate average by dividing total by number of majors
    5) Return tuple of (total, average)
'''
def find_total_avg_of_division(division_name: str) -> tuple:
    with open(division_name, 'r') as file:
        lines = []
        for line in file:
            lines.append(line)

    division_data = lines[2:]

    total = 0
    for line in division_data:
        parts = line.strip().split(',')
        total += int(parts[2]) + int(parts[3]) + int(parts[4])

    average = round(total / len(division_data), 2)
    return total, average


'''
# Design Recipe
Input: lst_grad_obj - list of Graduate objects
Output: tuple (total_graduates, average_graduates)
Purpose: Calculate total and average number of graduates across all degree levels
         (Bachelor, Master, Doctor) for all Graduate objects in the list
Example:
    If lst_grad_obj contains 3 graduates with totals of 100, 200, 300
    Returns: (600, 200.0)
Steps:
    1) Initialize total to 0
    2) Loop through each Graduate object
    3) For each object, sum:
       - bachelor[0] + bachelor[1] (female + male)
       - master[0] + master[1]
       - doctor[0] + doctor[1]
    4) Add this sum to running total
    5) Calculate average by dividing total by number of Graduate objects
    6) Return tuple of (total, average)
'''
def find_graduate_total_avg(lst_grad_obj: list[Graduate]) -> tuple:
    total = 0
    for grad in lst_grad_obj:
        bachelor_total = grad.bachelor[0] + grad.bachelor[1]
        master_total   = grad.master[0]   + grad.master[1]
        doctor_total   = grad.doctor[0]   + grad.doctor[1]
        total += bachelor_total + master_total + doctor_total

    average = round(total / len(lst_grad_obj), 2)
    return total, average


def main():
    headers, data = read_file('graduate_rate.csv')
    createDivision = create_division(data)
    createGraduate = create_graduate(data)

    create_files(createDivision, createGraduate)

    for division in createDivision:
        division_words = division.division_name.split()
        filename = division_words[0] + '.csv'
        total, avg = find_total_avg_of_division(filename)
        print(f'{division_words[0]} (Total: {total}, Average: {avg})')

    overall_total, overall_avg = find_graduate_total_avg(createGraduate)
    print(f'Overall (Total: {overall_total}, Average: {overall_avg})')


if __name__ == "__main__":
    main()