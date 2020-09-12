# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 01:36:15 2020

@author: 17204
"""

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children={}
        self.word_end=False
        self.output=[]
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char]=TrieNode()
        
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root=TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current=self.root
        for each_char in word:
            if each_char not in current.children:
                current.insert(each_char)
            
            current=current.children[each_char]
            #print(current.children)
        current.word_end=True       
        
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        
        current=self.root
        
        for each_char in prefix:

            if each_char not in current.children:
                return None

            current=current.children[each_char]
                    
        return current
    
class TrieNode:
    def __init__(self):
        
        self.children={}
        self.word_end=False
        self.output=[]
    
    def insert(self, char):
        self.children[char]=TrieNode()
        
    def suffixes(self, suffix = ''):
        #print('hi',self.children.items())
        if self.children:

            for key, val in self.children.items():

                if val.word_end==True:
                    
                    output.append(suffix + key)

                val.suffixes(suffix + key)

        return list(set(output))
    
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
    
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
        
        
interact(f,prefix='');
output=[]
interact(f,prefix='trip');
output=[]
interact(f,prefix='fu');
output=[]
interact(f,prefix='an');