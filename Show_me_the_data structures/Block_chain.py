#!/usr/bin/env python
# coding: utf-8

# In[40]:


import hashlib

import datetime


# In[41]:



class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
        
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = str(self.data).encode('utf-8')+str(self.previous_hash).encode('utf-8')+str(self.timestamp).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()
    def __str__(self):
        return '\nBlockHash: {}\n Timestamp: {}\n Data: {}\n Previous Hash: {}\n'.format(self.hash, self.timestamp, self.data, self.previous_hash)


# In[62]:


class Node:
    def __init__(self,data,previous_hash):
        self.block = Block(datetime.datetime.utcnow(), data, previous_hash)
        self.next = None
        self.data = data
        self.tail = None

class Blockchain:
    def __init__(self):
        self.head = None
    def append(self, data=None):
        if data==None:
            print('Block data cannot be none')
            return  
        if self.head is None:
            self.head = Node(data,None)
            self.tail = self.head
        else:
            self.tail.next = Node(data,self.tail.block.hash)
            self.tail = self.tail.next
        


# In[63]:


block = Block(datetime.datetime.utcnow(),'My_info_1',675)


block_chain = Blockchain()
block_chain.append("Information1")
block_chain.append("Information2")
block_chain.append("Information3")

print(block_chain)
print('head',block_chain.head.block,'data',block_chain.head.data,'hash',block_chain.head.data)
print(block_chain.head.data)

block = Block(datetime.datetime.utcnow(),'My_info_2',4563)


# In[64]:


# Custom Edge case

block_chain = Blockchain()

block_chain.append()
block_chain.append("place this information")
block_chain.append()
# prints can't store empty block

print(block_chain)


# In[65]:


blockchain = Blockchain()

# Edge test cases

blockchain.append()

# Test cases
blockchain.append("0")
blockchain.append("1")
blockchain.append("2")

print(block_chain.head.block)


# In[ ]:




