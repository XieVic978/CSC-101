"""
2+3
5
2*3
6
2**3
8
49//3
16
49/3
16.333333333333332
49%3
1
4*3+17//2-5
15
4*(3+17)//2-5
35
4 * 3 + (17 // 2) - 5
15
4 * (3 + 17) // (2-5)
-27
x=1
y=2
2*x+y
4

"""
"""
a=1+2
print(a)

x=3**2   #9
y=4**2   #16  The ** is an exponentiation operator
z=x*y #144
print()

a=2
b=a+1   #3
a=9    #value of a is 9. value of b is 3
print(a)


a = not True    #False
x = a and True or False   #False
print()
"""
"""
def function1(x,y):
    z=x+y*2
    return z+4
result =function1(2*2,4-1)
"""

"""
def square(n:float) -> float:
    return n*n # It is n squared. The value that you assign is n

result = square(square(2)) # It is 16
print()

def function2(a:int,b:int) -> int:
    c=a+b  #yes they are related
    return c**2 # The value is 256
a=9
b=7
answer = function2(a,b) # The value of answer is also 256
print() #you cannot call c because it is a local variable. It is inside function2
"""