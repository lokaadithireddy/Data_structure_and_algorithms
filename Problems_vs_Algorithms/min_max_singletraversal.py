# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:17:42 2020

@author: 17204
"""

def get_min_max(ints):
    
    if len(ints)==0:
        return None
    maximum=float('-inf')
    minimum=float('inf')
    
    for i in ints:
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    return (minimum,maximum)


## Example Test Case of Ten Integers
import random

l = [i for i in range(-10, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((-10, 9) == get_min_max(l)) else "Fail")

#print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print(get_min_max([]))  #None
print(get_min_max([1])) #(1,1)
print(get_min_max([10, 5, 6, 0, 12, 8]))  # (0, 12)
print(get_min_max([-5, -6, -12, -80, -8]))  # (-80,-5)
print(get_min_max([1, -22, 5, 6, 0, 12, 8, -9, 4, 4, 2, 20]))  # (-22, 20)

