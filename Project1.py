#Name:Victor
#Section:

from data import *

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input: string
output: integer
purpose: To find the amount of vowels in the string and return the integer value
Steps: 
1) make a counter that is 0 
2)make a list with all the vowels
3) make a while or for loop that will loop through the test string
4) make another loop for the vowel list
5) if the string at an index is equal to any one of those vowels, then increase counter by 1
6) repeat and then return counter

'''
# Implementation
def vowel_count(string:str)->int:
    counter = 0
    idx = 0
    list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while idx < len(string):
        for i in range(len(list1)):
            if string[idx] == list1[i]:
                counter += 1

        idx += 1
    return counter


# Part 2
'''Design Recipe (Write your design recipe here!)
input:nested list
output:nested list
purpose:To return a nested list with only sublists with length of 3 or larger
Steps: 
1)create a new list. 
2)loop through the nested list and get each sublist
3)check if each sublist is greater or equal 3
4)if it is equal or greater than 3, then append that sublist into the new list
5) repeat until finished
'''
# Implementation

def long_list(newList2:list[list[int]])->list[list[int]]:
    newList = []
    for sublist in newList2:
        if len(sublist) >= 3:
            newList.append(sublist)

    return newList


# Part 3
'''Design Recipe (Write your design recipe here!)
input:nested list
output:nested list
purpose:to make descending sublists with only sublist that contains 2 elements. everything else stays the same
Steps:
1)create a new list
2)create a list 'pairlist' for sublist with 2 elements
3)loop through each sublist
4)write an if statement to see if sublist contains only 2 elements
5)if first int is smaller than 2nd int, rearrange them by putting 2nd int into the first spot using the empty pair list, then append the newlist with the pairlist
6)if first int is larger than 2nd int, then just append sublist
7)if sublist is not of 2 elements, just append the sublist
'''
# Implementation

def descending_pairs(list1:list[list[int]])->list[list[int]]:
    newList = []
    pairList=[]
    for sublist in list1:
        if len(sublist) == 2:
            if sublist[0] < sublist[1]:
                pairList = [sublist[1],sublist[0]]
                newList.append(pairList)
            else:
                newList.append(sublist)
        else:
            newList.append(sublist)
    return newList

# Part 4
'''Design Recipe (Write your design recipe here!)
input: 2 price objects
output:2 price objects
purpose: adding 2 price objects
Steps:
1)in the parameters of add_prices, it needs to pass the object
2)make a new dollar variable that adds the dollars of both objects
3) make a new cents variable to add all the cents
4) if the cents add up and are greater than 99, then use module to get only the decimal integers
5) use floor division by 100 on the cents to get just the integer without the decimals
6) add the dollars with the floor divided cent which is basically just dollars
7) return both dollars and cents
'''
# Implementation

def add_prices(p1: Price, p2: Price)->Price:
    dollars  = p1.dollars + p2.dollars
    cents = p1.cents + p2.cents
    newCents = 0
    if cents>99:
        newCents = cents%100
        cents = cents // 100
        dollars+=cents
    else:
        newCents = p1.cents + p2.cents

    return Price(dollars,newCents)

# Part 5
'''Design Recipe (Write your design recipe here!)
input:Rectangle object
output: Rectangle object
purpose: to calculate the perimeter of the rectangle object
Steps:
1) Find the width by taking the absolute difference between top_left.x and bottom_right.x
2) Find the height by taking the absolute difference between top_left.y and bottom_right.y
3) Calculate the perimeter using the formula: 2 * (width + height)
4) Return the total perimeter as a float
'''
# Implementation

def rectangle_perimeter(rect:Rectangle)->float:
    perimeter_x =abs((rect.top_left.x - rect.bottom_right.x))
    perimeter_y = abs((rect.top_left.y-rect.bottom_right.y))
    total_perimeter = 2*(perimeter_x + perimeter_y)
    return total_perimeter

# Part 6
'''Design Recipe (Write your design recipe here!)
input:list of Point
output:list of Point
purpose:to return all Points that are negative
Steps:
1)make a new list
2)loop through all the points in the list
3)make a conditional statement so if both x and y points are negative, it would append those values to newlist
4)return and repeat
'''
# Implementation

def are_in_negative_quadrant(values:list[Point])->list[Point]:
    newList = []
    for i in range(len(values)):
        if values[i].x < 0 and values[i].y < 0:
            newList.append(values[i])
    return newList

# Part 7
'''Design Recipe (Write your design recipe here!)
input: rectangle object
output: circle object
purpose: to return the radius and center of the circle that encloses the rectangle, and that the circle touches the edge at all 4 corners
Steps:
1)find center_x by adding left x point by right x point and dividing it by 2
2)find center_y by adding left y point by right y point and dividing it by 2
3)take a point, left or right doesnt matter. to find radius, subtract center_x by that x point and then square it. do the same for the y value. add both x and y values and then sqrt the value
4) return the center and the radius
'''
# Implementation


def circle_bound(rect:Rectangle)->Circle:
   center_x = (rect.top_left.x + rect.bottom_right.x) / 2
   center_y = (rect.top_left.y +rect.bottom_right.y)/2

   radius = math.sqrt(((rect.bottom_right.x - center_x)**2) + ((rect.bottom_right.y - center_y)**2))
   return Circle(Point(center_x,center_y),radius)






# Part 8
'''Design Recipe (Write your design recipe here!)
input: Employee object
output: list of string
purpose: return the employees that are paid higher than the average pay of all employees
Steps:
1) Check if the list is empty, if so return an empty list
2) Create a variable to store total_pay initialized to 0
3) Loop through all employees and add each employee's pay_rate to total_pay
4) Calculate average_pay by dividing total_pay by the number of employees
5) Create a new empty list called newEmployees
6) Loop through all employees again
7) If an employee's pay_rate is greater than average_pay, append their name to newEmployees
8) Return newEmployees list
'''
# Implementation

def higher_than_average(value:list[Employee])->list[str]:
    average_pay = 0
    total_pay = 0
    newEmployees =[]
    if len(value)==0:
        return newEmployees
    for i in range(len(value)):
        total_pay+=value[i].pay_rate
    average_pay = total_pay / len(value)

    for i in range(len(value)):
        if value[i].pay_rate > average_pay:
            newEmployees.append(value[i].name)

    return newEmployees

