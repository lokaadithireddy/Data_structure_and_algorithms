# Finding files

Since every folder has repetition of tasks, it is better to do recursion as discussed in lesson 3

input taken is suffix, path.

Output will be list of files ending with .c

As per given OS module exploration code, the tasks becomes easy with (endswith,isfile and listdir) 

Task is done by calling same function(find_files) recursively for each directory.

# Time Complexity and Space Complexity

Time complexity is O(n1 X n2). 

n1 being number of levels.

n2 being number of directories under each level.

Space complexity is O(n), 
n being number of levels

