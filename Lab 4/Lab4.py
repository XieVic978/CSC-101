# Lab 4
# Victor Xie
# Your Section:


# Write your functions for each part in the space below.

# Task 1 - last_element
# input/output: list[list[float]] -> list
# purpose: Take the last index of each value of each sublist and return a list
# how to implement: [1,2,3,4,5],[1,4,3,5,6] -> [5,6]

#from typing import Optional
def last_element(nums:list[list[float]])->list:
    idx = 0
    newList = []
    while idx <len(nums):
        if len(nums[idx]) > 0:
            last_val = nums[idx][len(nums[idx])-1]
            newList.append(last_val)
        idx+=1
    return newList




# Task 2 - pass_fail
# input/output: list[list[int]], int -> 'Pass' or 'Fail'
# purpose: If list of students' grades are higher than threshold int, then it will be pass and vice versa
# how to implement: [[90,90,100],[89,98,100]],80 -> Pass

def pass_fail(nums:list[list[int]], nums2:int) -> list[str]:
    idx = 0
    list_pass_fail = []

    while idx < len(nums):
        fail_var = 0
        for item in range(len(nums[idx])):
            if nums[idx][item] < nums2:
                fail_var+=1
        if fail_var>= 1:
            list_pass_fail.append('Fail')
        else:
            list_pass_fail.append('Pass')
        idx+=1
    return list_pass_fail


# Task 3 - search_value
# input/output: list, val -> string
# purpose: Find whether the value is found inside the list or not.
# how to implement:[1,2,3] val = 3 - > 'Found

def search_value(anything:list,val) ->str:
    found_notFound = ''
    foundCounter = 0
    for i in range(len(anything)):
        if val == anything[i]:
            foundCounter +=1
        if foundCounter >=1:
            found_notFound = 'Found'
        else:
            found_notFound = 'Not Found'
    return found_notFound


# Task 4 - search_any
# input/output: a list of anything -> True or False
# purpose: To search the list and if the value if found then return True if not return False
# how to implement:[1,2,3,4,5] val = 2, -> True

def search_any(anything:list,val)->bool:
    true_false = bool
    counter = 0
    for idx in range(len(anything)):
        if val == anything[idx]:
            counter +=1
        if counter >=1:
            true_false = True
        else:
            true_false = False

    return true_false

# Task 5 - reverse_value
# input/output: list or string - > list or string
# purpose: To reverse the list or string.
# how to implement: hello - > olleh.... [1,2,3] -> [3,2,1]
def reverse_value(value):
    newVal = ''
    a = []
    if type(value)==str:
        for idx in range(len(value) - 1, -1, -1):
            newVal = newVal + value[idx]
        return newVal
    else:
        for idx in range(len(value)-1,-1,-1):
            a.append(value[idx])
    return a



