from contextlib import nullcontext


def smallest(n: float, m: float) -> float:
    if n < m:
        return n #This statement will never be evaluated because in both procedure calls, n will never be less than m.
    else:
        return m
first = smallest(3,2) # The value would be 2
second = smallest(2,2) #The value would also be 2. Yes this is reasonable because in the first if statement in the function, 2 cannot be less than 2. If that is not true it will return m, which is 2 in this case.
print()


def function2(a:int, b:int, c:int) -> int:
    if a>b and a>c:
        return a-b #It will evaluate this statement when a is greater than b AND a is greater than c
    elif b>c:
        return b+c #It will evaluate this statement when the first if statement is not true and if b is greater than c
    else:
        return 2*c #It will evaluate this statement when the first two if statements are not true

answer1 = function2(3,2,1) #The value of answer1 is 1
answer2 = function2(2,3,1) #The value of answer2 is 4
answer3 = function2(2,1,3) #The value of answer3 is 6
print()


from typing import Optional

def checked_access(L:list[int], idx:int)->Optional[int]:
    test = idx >= 0 and idx < len(L) #The value on the first call is False. The value on the second call is True
    if test:                         #This check prevents indexes that is larger than the length of L. So if idx is larger than the List it will return none.
        return L[idx]
    else:
        return None
first1 = checked_access([1,0,1], 9) #The value is None
second1 = checked_access([1,0,1], 2) #The value is 1
print()

def length_sum(L:list[str]) ->int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])
            #The first call will be evaluated since it has a length of list L greater than 2
            #The values being added are length of 'this, 'is', 'the' which is 4+2+3 = 9
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])
            #The third call will be evaluated
            #The values being added are 'another', 'call', which is 7+4 = 11
    elif len(L) >0:
        result = len(L[0])
            #The second call will be evaluated
            #The values being added are 'second call' 6+1+4 = 11 (The space counts as a character)
    else:
        result = 0
    return result
first2 = length_sum(['this', 'is', 'the', 'first', 'call'])
second2 = length_sum(['second call'])
third2 = length_sum(['another', 'call'])
print()


def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L
words = ['this', 'is', 'confusing', 'code.']
first3 = surprising(words, 'Avoid')
second3 = surprising(words, 'such.')
#The value of words after both calls is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#The value of first and second are both ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
'''In the first call, it takes the words list and appends the parameter 'other' to 'Avoid' and uses upper() to make it 
uppercase. Afterwards, it goes down to the second call and append the list with 'such' and also make it uppercase.
After both first and second calls were called, the words list was modified with 'AVOID' and 'SUCH.' So the first call 
'''
print()
