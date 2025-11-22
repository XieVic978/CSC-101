from convert import *
'''
input: user input
output: list of float
purpose: user will be prompted to input a number each time and that will be turned into a list of float. if the user 
            inputs a non float then it will be skipped. it ends when user types 'done'
example: input(3,5,2,3) -> [3.0,5.0,2.0,3.0],   input(5,'what',4,'juice) -> [5.0,4.0]
'''

def gather_numbers()->list[float]:
    newList = []

    while True:
        user = input('Enter an integer: ')
        if user.lower()=='done':
            break
        num = str_to_float(user)
        if num is not None:
            newList.append(num)

    return newList

if __name__ == '__main__':
    numbers = gather_numbers()
    print('Sum: ', sum(numbers))