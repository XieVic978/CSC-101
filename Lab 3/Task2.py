def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num   #total = 0, total=0+4=4, total=4+9=13, total=13+2=15, total=15+1=16, total=16
    return total

result = tally([4,9,2,1])


def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])  #idx at 0 [4],idx at 1 [4,9],idx at 2 [4,9,2],idx at 3 [4,9,2,1],

    return new_list                 #This loop differs because it gives the indexes of the list instead of the actual
                                    #value of the list. Then when you append it, you take the nums list at that index
                                    #and append it to new_list

result2 = copy([4,9,2,1])
print()


def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for values in nums:
        new_list.append(values + 1) #4+1=5, 9+1=10, 2+1=3, 1+1=2

    return new_list                 #new_list = [5,10,3,2]

result3 = increment_all([4,9,2,1])
print()