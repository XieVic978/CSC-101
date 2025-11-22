# Name:
# Section: 7
from book_class import *
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        # SWAPPING
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
# input: list of book objects
# output: list of book objects
# purpose: to sort the list of book objects by title
# example:[ Books(["rick Riordan"],"Percy Jackson"), Books(["JK Rowling"], "Harry Potter") - >  [Book(["JK Rowling"], "Harry Potter"), Book(["Rick Riordan"], "Percy Jackson")]
# Title is Percy Jackson and Harry Potter -> Harry Potter comes first
# implementation:
def min_index(books:list[Book],start:int)->Optional[int]:
    if start < 0 or start > len(books) - 1:
        return None

    minIdx = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[minIdx].title :
            minIdx = idx
    return minIdx



def selection_sort_books(books:list[Book]):
    for idx in range(len(books)-1):
        minIdx = min_index(books,idx)
        tmp = books[minIdx]
        books[minIdx] = books[idx]
        books[idx] = tmp #idx is used only once so values[idx] will be the final answer



# Part 2
# input: string
# output: string
# purpose: if letter of string is lowercase, turn into upper, and vice versa. if not a letter then leave it unmodified
# example: Hello -> hELLO
# implementation:

def swap_case(word:str)->str:
    newString = ''
    for i in word:

        if i.isalpha() and i.isupper():

            newString = newString + str.lower(i)
        elif i.isalpha() and i.islower():
            newString = newString + str.upper(i)

        else:
            newString = newString + i
    return newString


# Part 3
# input: 3 strings
# output: 1 string
# purpose: to replace the string with new string from old string
# example: (Mama, a, o) -> Momo
# implementation:

def str_translate(string:str,old:str,new:str)->str:
    newString = ''
    for letter in string:
        if old in letter:
            newString += new
        else:
            newString+=letter
    return newString



# Part 4
# input:string
# output:dictionary
# purpose:to return a dictonary with a key of the words and a value of how many times that key appears in the string
# example: 'Bro how is bro' -> {'Bro':2,'how':1,'is':1}
# implementation:

def histogram(string:str)->dict:
    new_dict = {}
    lst = string.split()
    for i in lst:
        if i in new_dict:
            new_dict[i]+=1
        else:
            new_dict[i]=1
    return new_dict





