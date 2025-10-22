more = [x+1 for x in [1,2,3,4]] #It loops through the values in list more and then adds 1 to them. So x=1, x=2, x=3, x=4.
print() #The value is more = [2,3,4,5]


def square(n:int) ->int:
    return n*n              # n=1, 1 , n=2, 4, n=3, 9, n=4, 16

squares = [square(x) for x in[1,2,3,4]] #squares = [1,4,9,16]
print() #These values relate to the values above because it takes each value in the list and calls square(n)
        #and then inside that function, it returns the square of that value. Then it puts it back in that list and repeats.

def check(n:int) -> bool:
    return n>2                                # n=0, False, n=1,False, n=2,False, n=3,True, n=4,True

answer = [x for x in range(5) if check(x)]    #The value of answer is answer = [3,4]
print()


def inc(m:int) ->int:
    return m+1              #x =   0+1=1, 1+1=2, 2+1=3, 3+1=4, 4+1=5

def check2(n:int) -> bool:
    return n>2              # n=0, False, n=1,False, n=2,False, n=3,True, n=4,True

answer2 = [inc(x) for x in range(5) if check2(x)]
print()   #At the end it takes 3 and 4 and then adds 1 to both of them making the list [4,5]
