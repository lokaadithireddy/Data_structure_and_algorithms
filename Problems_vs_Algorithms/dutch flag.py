# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:45:42 2020

@author: 17204
"""

def sort_012(input_list):
    
    low=mid=0   
    high=len(input_list)-1
    
    while(mid<=high):
        
        if input_list[mid]==1:
            mid+=1
        elif input_list[mid]==0:
            input_list[low],input_list[mid]=input_list[mid],input_list[low]
            low+=1
            mid+=1
        else:
            input_list[high],input_list[mid]=input_list[mid],input_list[high]
            high-=1
            
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([])  #[]
test_function([2])  #[2]
test_function([1, 1, 1, 1, 1, 1])   #[1, 1, 1, 1, 1, 1]
test_function([1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1])   #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]



