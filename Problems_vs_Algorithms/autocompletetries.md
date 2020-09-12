Inorder to perform "autocomplete with tries", I have used "Trie" data structure.
For implementing trie, I have created two classes named TrieNode(which represents
single node) and trie. Inorder to insert words into trie I have checked each 
character if its already present in children dictionary or not. If not present,
I inserted else checked the next character. I aslo set 'word_end' to True once word
is completed. I used recursive approach to determine the possible words for the 
given characters.


Time Complexity:

The time complexity for insert function is O(l) where l is the length of the word being 
inserted. Similary the time complexity for search function is also O(l). So, the time taken
for inserting n words into trie is O(n*a) where a is average length of words.


Space Complexity:

The worst case space complexity for inserting a word into trie is O(l) when all the letters 
in the word doesn't match with those in trie. Inserting all n words requires O(l*n) space.
Here l is length of word.However, the space complexity for search function is O(1) as not additional space is being used
while searching.

 