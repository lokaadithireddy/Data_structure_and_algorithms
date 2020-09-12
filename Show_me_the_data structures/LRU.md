
# Least Recently Used

Since the given condition is all operations must be O(1) time complexity,
Its better to use dictionary as insert,delete and finding key operations would take O(1) time complexity


I used OrderedDict() from collections because of the following: 

Order is maintained and each time we encounter a get(key) method, I updated the key as latest key.

If key is not found, it goes to except block and returns -1.

When the cache is full, my code removes first key in the dictionary as it is least recently used and adds new key as the latest one.

In the set() method, my code handles null values.


# Time Complexity

get() operation is O(1) time complexity because dictionaries consider hashing as a technique.
Accessing a key is therefore O(1)

set() operation is O(1) time complexity.
Updating the key in dictionary is constant time.


# Space Complexity

O(n) as we are storing size of data and all the elements of size n



