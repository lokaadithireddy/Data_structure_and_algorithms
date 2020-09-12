To determine the index of given number in rotated sorted array. I used binary search approach.
I have taken three pointers low,mid,high. The basic idea idea is to divide the 
search space into halves and update the pointers low,mid and high such that we determine the
sub space in which we need to search.

Time Complexity:O(log n)
Space Complecity:O(1)