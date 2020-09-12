For routing problem, I pretty much implemented the trie in the same except that a handler 
is included for this problem.For adding into the trie, I initially the split the path and
added each part of the result to each level of the tree/trie and once the entire path is done,
I assigned the handler. In a similar way, to search the given path, I split the path similarly
and checked if each part is present in the dictionary. If present returned the handle else 
not found.

Time Complexity:

Initially I split the path with '/' into subpaths and each subpath is to be assigned to a level in 
the trie.The time complexity for insert function is O(p) where p is the number of subpaths present 
in the path that is being inserted. The lookup function and add_handler has not much operation on
its own but acts as mediator.Lookup function and add_handler calls split_path function which takes O(n) 
(where n is length of path)for splitting the path and also calls find function which takes O(p) 
where p is number of subpaths in the path. Similary the time complexity for search function is it takes O(n) 
for splitting and O(p) for searching.The time complexity of find function is O(p) where p is the number of subpaths 
present in the path that is being searched.


Space Complexity: 

The worst case space complexity for inserting a path into trie is O(p) when all the subpaths 
in the path doesn't match with those in trie. However, the space complexity for search function is 
O(1) as no additional space is being used while searching and its only read only.Similarly, the
space complexity for lookup and find is O(1) as it is read only and no additional space is required
for this purpose.

