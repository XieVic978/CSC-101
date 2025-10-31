from typing import Optional

#Name: Victor
#Section:
from classes import *

# Write your functions for each part in the space below.

# Part 1
'''Design Recipe (Write your design recipe here!)
input: 2 point objects
output: rectangle object
purpose: to return the rectangle object with points with top left and bottom right
Steps:
1) find the top left x of the 2 points
2) find the bottom right x of the 2 points
3) find the top left y of the 2 points
4) find the bottom right y of the 2 points
5) make a new point object that shows the new point of top left
6) make a new point object that shows the new point of bottom right
7) return rectangle object with the new points
'''
# Implementation
#P(2,2)
# P(10,10) -> (2,10) , (10,2)
def create_rectangle(p1:Point,p2:Point)->Rectangle:

    if p1.x <= p2.x:
        top_x = p1.x
        right_x = p2.x
    else:
        top_x = p2.x
        right_x = p1.x
    if p1.y >= p2.y:
        top_y = p1.y
        bottom_y = p2.y
    else:
        top_y = p2.y
        bottom_y = p1.y

    topLeft = Point(top_x,top_y)
    bottomRight = Point(right_x,bottom_y)
    return Rectangle(topLeft,bottomRight)


# Part 2
'''Design Recipe (Write your design recipe here!)
input: 2 duration objects
output: boolean
purpose: to return true if first duration is smaller than second duration and false otherwise
Steps:
1) turn both the duration into seconds so it is easier to calculate
2) if first second is smaller than the second then return true and if not then return false
'''
# Implementation

def shorter_duration_than(d1:Duration,d2:Duration)->bool:

    d1Seconds = d1.minutes*60 + d1.seconds
    d2Seconds = d2.minutes*60 + d2.seconds
    return d1Seconds<d2Seconds


# Part 3
'''Design Recipe (Write your design recipe here!)
input: list of song and duration object
output: list of song
purpose: to return a list of song if the duration of the song is shorter than the input duration 
Steps:
1) make a new list 
2) turn the input duration into seconds so it is easier to calculate
3) loop through the list
4) calculate the duration of song at idx and if that song is shorter than the input duration append that song into new list
5) return new list
'''
# Implementation

def songs_shorter_than(lst:list[Song],d1:Duration)->list[Song]:
    newList =[]
    inputDuration = d1.minutes * 60 + d1.seconds
    for idx in range(len(lst)):
        if lst[idx].duration.minutes*60 + lst[idx].duration.seconds < inputDuration:
            newList.append(lst[idx])
    return newList


# Part 4
'''Design Recipe (Write your design recipe here!)
input: list of songs and list of int
output: duration object
purpose: to add up the duration of the songs in the given index 
Steps:
1) make a new variable for minutes and seconds
2) loop through the playlist index
3) make sure that the index is actually in the songs list
4)add the minutes and seconds of all the songs
5) after that if seconds is over 60 seconds then use mod to get the seconds and turn the seconds to minutes
6) return the duration 
'''
# Implementation

def running_time(lst:list[Song],playlist:list[int])->Duration:

    minutes = 0
    seconds = 0

    for idx in playlist:
        if 0<=idx<len(lst):
            minutes += lst[idx].duration.minutes
            seconds += lst[idx].duration.seconds

    if seconds >= 60:
        minutes += seconds //60
        seconds = seconds % 60

    return Duration(minutes,seconds)




# Part 5
'''Design Recipe (Write your design recipe here!)
input: list of list of string and list of string
output: true or false
purpose: to return true if the city link is valid and false if the city link is not valid
Steps:
1) use a while loop to loop through the city route
2) make a valid_route so it is true automatically
3) make sure that the index of city does not go over the length of the city route 
4)make a new list for city index and city index +1 and vice versa so that the order doesnt matter
5) if either one of the city index is valid then make the boolean true
6) if it is not valid then just return false 
7) keep on looping through each index and if they are all valid it will return true

'''
# Implementation

def validate_route(city_link:list[list[str]],city:list[str])->bool:
    idx = 0
    valid_route = True
    while idx < len(city):

        if idx + 1 == len(city):
            break
        newList = [city[idx],city[idx+1]]
        newList2 = [city[idx+1],city[idx]]

        if newList in city_link or newList2 in city_link:
            valid_route = True
        else:
            return False
        idx += 1

    return valid_route



# Part 6
'''Design Recipe (Write your design recipe here!)
input: list of integer
output: none or int
purpose: to find the index at longest continious number
Steps:
1) 

lst = [1, 1, 2, 2, 1, 1, 1, 3]
      [0, 1, 2, 3, 4, 5, 6, 7]
      
      [0,1]
'''
# Implementation
def long(lst:list[int]):
    num = 1
    longest_num = 1
    longest_index = 0
    idx = 0
    while idx < len(lst)-1:
        if lst[idx] == lst[idx + 1]:
            num += 1
        else:
            num = 1
        if num > longest_num:
            longest_num = num
            longest_index = idx + 1

        idx += 1

    return longest_index - longest_num + 1

def longest_repetition(lst:list[int])->Optional[int]:
    if len(lst) == 0:
        return None

    else:
        return long(lst)




