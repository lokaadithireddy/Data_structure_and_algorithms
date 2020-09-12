# Huffman Coding

I initially encode function where in I used dictionary to store character of text as key and frequency as value.

Later I stored a list of Node objects by sorting them in descending order.
I created a tree by taking last two elements with lowest frequencies and combined their sum as parent node.
This way it forms an overall tree structure recursively in function 'encode'.

I updated the tree in 'update_tree' function using binary codes and it returns a dictionary.

Then, concatenation would be final encoded_data and tree is also returned.


For decoding, 'decode' is used recursively for every next index and text is returned

# Time and Space Complexity

Sorting frequency list : O(nlogn)
Huffman encoding and decoding takes O(n^2) because of tree traversal and dictionary update

Overall time complexity: O(n^2)

Space complexity : O(n) as all the characters and codes.





