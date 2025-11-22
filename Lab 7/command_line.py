import sys
from convert import str_to_float
'''
input: command-line arguments (strings representing numbers)
output: prints the sum of all valid numbers as a float
purpose: to read numbers from the command line, convert them to floats, skip invalid ones, and display their total
example: 
    if run as -> python command_line.py 3.5 2 abc 10
    output -> Sum of numbers: 15.5
'''


def main():
    total = 0
    args = sys.argv[1:]  # skip the filename

    for item in args:
        num = str_to_float(item)
        if num is not None:
            total += num

    print("Sum of numbers:", total)


if __name__ == "__main__":
    main()
