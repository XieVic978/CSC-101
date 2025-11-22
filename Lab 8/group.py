
def groups_of_3(lst: list[int])->list[list[int]]:
    newList = []
    numList = []

    for num in lst:

        numList.append(num)
        if len(numList) == 3:
            newList.append(numList)
            numList = []
    if len(numList) > 0:
        newList.append(numList)


    return newList





