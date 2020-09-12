#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
def union(llist_1, llist_2):
    data_structure = set()
    cur = llist_1.head
    # Your Solution Here
    while cur:
        data_structure.add(cur.value)
        cur = cur.next
    cur = llist_2.head
    while cur:
        data_structure.add(cur.value)
        cur=cur.next
    #Append to linkedlist as return type is linkedlist
    ll1 = LinkedList()
    for val in data_structure:
        ll1.append(val)
    return ll1
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    data_1 = set()
    cur = llist_1.head
    while cur:
        data_1.add(cur.value)
        cur = cur.next
    data_2 = set()
    cur = llist_2.head
    while cur:
        data_2.add(cur.value)
        cur = cur.next
    #Check for common elements
    ll2 = LinkedList()
    for v in data_1:
        if v in data_2:
            ll2.append(v)
    return ll2


# In[9]:


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)
print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
for i in element_1:
    linked_list_3.append(i)
for i in element_2:
    linked_list_4.append(i)
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))


# In[14]:


# My test case 3

ll1 = LinkedList()
ll2 = LinkedList()
l1 = [32]
l2 = [32,12]
for i in l1:
    ll1.append(i)
for i in l2:
    ll2.append(i)
print (union(ll1,ll2))
print (intersection(ll1,ll2))


# In[15]:


ll3 = LinkedList()
ll4 = LinkedList()
l3 = []
l4 = []
for i in l3:
    ll3.append(i)
for i in l4:
    ll4.append(i)
print (union(ll3,ll4))
print (intersection(ll3,ll4))


# In[ ]:




