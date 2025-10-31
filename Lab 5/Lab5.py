# Name: Victor
# Section: 7 Due 10/31/25
#########################################################
from typing import Optional

from data import *

# Write your functions for each part in the space below.
# Task 1
''' Design Receipe
input: list of Point object
output: list
purpose: to create a list of all the x coordinates
Steps:
1) Make a new list
2) loop through all the Point objects in the list
3) append only the x value 
4) return the new list
'''

def x_coordinates(value:list[Point])->list:
    newList =[]
    for idx in range(len(value)):
        newList.append(value[idx].x)
    return newList



# Task 2
''' Design Receipe
input: list of Point object
output: list of point object
purpose:to return a list of only positive Points
Steps:
1) Make a new List
2) loop through the list
3) if both points are positive append that to new list
4) return new list
'''

def are_in_positive_quadrant(value:list[Point])->list[Point]:
    newList = []
    for val in value:
        if val.x > 0 and val.y > 0:
            newList.append(val)
    return newList

# Task 3
''' Design Receipe
input: 2 point objects
output: float
purpose: to calculate the distance btwn 2 points
Steps:
1)calculate the x distance using the formula
2)calculate the y disntance using the formula
3) find the whole distance by sqrt everything
4) return it
'''

def distance(p1:Point,p2:Point)->float:
    x_distance = (p1.x-p2.x)**2
    y_distance = (p1.y-p2.y)**2
    total_distance = math.sqrt(x_distance+y_distance)
    return total_distance

# Task 4
''' Design Receipe
input:2 point objects
output:float
purpose:take the distance of 2 points using manhattan distance
Steps:
1) find x value by using absolute value of 2 points
2) do the same with y value
3) add both x and y values 
4)return the values
'''

def manhattan_distance(p1:Point,p2:Point)->float:
    x_value = abs(p1.x-p2.x)
    y_value = abs(p1.y-p2.y)
    total = x_value+y_value
    return total

# Task 5
''' Design Receipe
input: list of point object
output: list 
purpose: to calculate all the distances using manhattan distance
Steps:
1) make a new list
2) loop through the whole entire list
3) use the manhattan formula to calculate both x and y values
4) add them up
5) append the distance to the new list
6) return the new list
'''

def distance_all(lst:list[Point])->list:
    #newList = []
    origin = Point(0,0)
    newList = [manhattan_distance(point,origin) for point in lst]
    return newList



# Task 6
   # The function for Taks 6 should be within the class in data.py.


# Task 7
   # The function for Task 7 should be within the class in data.py.


# Task 8
''' Design Receipe
input: 2 time objects
output: one time object
purpose: create and return a new Time object representing the sum of two given times (t1 and t2).
The number of seconds and minutes in the result should always stay within the range 0–59, carrying any overflow into the next larger unit (seconds → minutes, minutes → hours).
Steps:

1)Add the seconds from both Time objects.
2)If seconds are greater than 59, convert the extra seconds into minutes and keep the remainder.
3)Add the minutes from both Time objects.
4)If minutes are greater than 59, convert the extra minutes into hours and keep the remainder.
5)Add the hours from both Time objects plus any carried hours.
6)Return a new Time object using the final hour, minute, and second values.
'''
def time_add(t1:Time,t2:Time)->Time:

    seconds = t1.second + t2.second
    minutes = t1.minute + t2.minute
    hours = t1.hour + t2.hour
    if seconds > 59:
        newMin = seconds //60
        seconds = seconds % 60
        minutes+=newMin
    if minutes > 59:
        newHr = minutes // 60
        minutes = minutes % 60
        hours+=newHr
    return Time(hours,minutes,seconds)


# Task 9
''' Design Receipe
input: a list of floats
output: a boolean
purpose: to return true if the list is descending and false if the list is not descending 
Steps:
1)If the list is empty, return False.
2)Loop through the list and compare each element to the next.
3)If any element is less than or equal to the next, return False.
4)If no comparisons fail, return True.
'''

#list = [4,3,2,1]

def is_descending(lst:list[float])->bool:
    for idx in range(len(lst)-1):
        if lst[idx] <= lst[idx+1]:
            return False
    return True

# Task 10
''' Design Receipe
input: list of int
output: None or int
purpose: to find the index with the largest value between a given lower and higher index
Steps:
1)If low > upper, low < 0, or upper is greater than the last index, return None.
2)Set maxVal to the value at index low.
3)Set newIdx to low.
4)Loop through all indexes from low to upper (inclusive).
5)If the current value is greater than maxVal, update both maxVal and newIdx.
6)After the loop ends, return newIdx.
'''

def largest_between(lst:list[int],low:int,upper:int)->Optional[int]:
    if low > upper or low <0 or upper > len(lst)-1:
        return None
    maxVal = lst[low]
    newIdx = low
    for idx in range(low, upper+1):
        if lst[idx] > maxVal:
            maxVal = lst[idx]
            newIdx = idx
    return newIdx


# Task 11
''' Design Receipe
input:list of point objects
output: none or Point object
purpose: to find the point that is farthest away from origin 
Steps:
1) if list is less than 0 return none
2) create a new list so that we can reuse the function above
3)loop through all the values in the list
4) use manhattan distance to calculate the distance btwn points
5)append the distance into the list
6) return the largest_between function using our new list. 
'''


def furthest_from_origin(lst:list[Point])->Optional[int]:
    if len(lst) == 0:
        return None

    distance1 = []
    for val in lst:
        values = abs(val.x)+abs(val.y)
        distance1.append(values)

    return largest_between(distance1,0,len(lst)-1)










