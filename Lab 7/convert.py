from typing import Optional
'''
input:str
output: float
purpose: to convert a string into a float if it is possible, if not possible return None
Example: str_to_float('3.14') -> 3.14

'''

def str_to_float(string:str)->Optional[float]:
    try:
        num = float(string)
        return num
    except  ValueError:
        return None




