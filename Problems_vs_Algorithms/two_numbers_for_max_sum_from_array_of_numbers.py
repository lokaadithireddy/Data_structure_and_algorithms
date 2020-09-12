# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:39:36 2020

@author: 17204
"""
def rearrange_digits(input_list):
    
    
    if len(input_list)<=1:
        return input_list
    
    
    def merge_sort(a):
        if len(a)>1:
            middle=len(a)//2
            left_subarray=a[:middle]
            right_subarray=a[middle:]
            
            merge_sort(left_subarray)
            merge_sort(right_subarray)
            
            l=m=n=0
            
            while(l<len(left_subarray) and m<len(right_subarray)):
                if left_subarray[l]>right_subarray[m]:
                    a[n]=right_subarray[m]
                    m+=1
                    n+=1
                else:
                    a[n]=left_subarray[l]
                    l+=1
                    n+=1
            while(l<len(left_subarray)):
                a[n]=left_subarray[l]
                n+=1
                l+=1
            
            while(m<len(right_subarray)):
                a[n]=right_subarray[m]
                m+=1
                n+=1
                
            return a
        
    list_ascending=merge_sort(input_list)
    #print('hi',list_ascending)

    
    x = y = 0
    exponent=0
    for i in range (0, len(list_ascending), 2):
        x = x+((10**exponent)*list_ascending[i])
        if i+1<len(list_ascending):
            y = y+((10**exponent)*list_ascending[i+1])

        exponent+=1
    if x>y:
        return [x,y]
    else:
        return [y,x]
        

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
print(rearrange_digits([4, 6, 2, 5, 9, 8]))  # [964, 852]]

print(rearrange_digits([42]))  # [42]

print(rearrange_digits([8, 7, 6, 4, 2, 1]))  # [862, 741]

test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case2=[[1, 2, 3, 4, 5], [531, 42]]
test_case3=[[1,1,1],[11,1]]
test_case4=[[0,0,0],[0,0]]   
test_case5=[[0,0,1],[10,0]] 
test_function([[],[]])

test_function(test_case1)
test_function(test_case2)
test_function(test_case3)
test_function(test_case4)
