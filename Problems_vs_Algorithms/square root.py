# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 22:32:00 2020

@author: 17204
"""

def sqrt(number):
    if number<0:
        return 'invalid'
    
    if number==0 or number==1:
        return number
    
    low=0
    high=number
    res=0
    
    while(low<=high):
        mid=(low+high)//2
        
        if mid*mid==number:
            return mid
        elif mid*mid<number:
            low=mid+1
            res=mid
        else:
            high=mid-1
    return res

#Test Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  ('invalid' == sqrt(-11)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print("Pass" if (31426 == sqrt(987654321)) else "Fail")