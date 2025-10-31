<<<<<<< HEAD
from datetime import datetime
import time

current_time = datetime.now().strftime("%I:%M %p")
idx = 0
while True:
    print(current_time)
    time.sleep(10)
=======
from typing import Optional

from book_class import *

Books = [Book(["JK Rowling"], "Harry Potter"), Book(["Rick Riordan"], "Percy Jackson")]

def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


def selection_sort(values:list[int]) -> list[int]:
    newList = []
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        # SWAPPING
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

        newList.append(tmp)
    return newList


lst = ['hello','my','name','is','victor']
newList = []
newList2 = []
lst.sort()
print(lst)
>>>>>>> b27c0693c4edd6009a63aa9260d135de919407c5
