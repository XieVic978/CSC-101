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

def selection_sort_books(books:list[Book])->list[Book]:
    newList = []

    for book in books:
        newList.append(ord(book.title))
    sortedInt = selection_sort(newList)



# Part 2
# input:
# output:
# purpose:
# example:
# implementation:

# Part 3
# input:
# output:
# purpose:
# example:
# implementation:

# Part 4
# input:
# output:
# purpose:
# example:
# implementation:


