#!/usr/bin/env python
# coding: utf-8

# Problem1

# In[2]:


from collections import OrderedDict
class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.my_dict = OrderedDict()
        self.capacity=capacity    
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        try:
            v = self.my_dict[key]
            del self.my_dict[key]
            self.my_dict[key]=v
        except:
            v = -1
        return v
    def set(self, key, value):
        if type(key)!=int:
            print('enter valid key and value')
            return        
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        try:
            if(len(self.my_dict)==self.capacity):  
                #print('hi',self.my_dict[list(self.my_dict)[0:1][0]])
                del self.my_dict[list(self.my_dict)[0:1][0]]
                self.my_dict[key]=value
            else:
                self.my_dict[key]=value
        except:
            print('We donot perform operations on a 0 capacity cache')


# In[3]:


my_cache = LRU_Cache(5)

my_cache.set(1, 1);
my_cache.set(2, 2);
my_cache.set(3, 3);
my_cache.set(4, 4);
print(my_cache.get(1))       
# returns 1
print(my_cache.get(2))       
# returns 2
print(my_cache.get(9))      
# returns -1 as 9 is not present in cache
my_cache.set(5, 5) 
my_cache.set(6, 6)
print(my_cache.get(3))      
# returns -1 because 3 is not present in cache as 3 was removed as LRU in above statement.


# In[4]:


# Edge case for empty cache
my_cache = LRU_Cache(0)
my_cache.set(2, 1)  
# We donot perform operations on a 0 capacity cache
print(my_cache.get(1))  
# returns -1


# In[5]:


our_cache = LRU_Cache(10)

our_cache.set(100, 10)
our_cache.set(8000, 20)
our_cache.set(1010, 30)
our_cache.set(50, 170)

print(our_cache.get(100))
# returns 10
print(our_cache.get(20))
# retuns -1
print(our_cache.get(8000))
# returns 20
print(our_cache.get(90))
# returns -1

our_cache.set(90, 50)
our_cache.set(110, 50)
our_cache.set(2000, 550)
our_cache.set(10, 80)
our_cache.set(600, 60)
our_cache.set(700, 8880)
our_cache.set(70, 880)
#print(our_cache.my_dict)
print(our_cache.get(8000))
# returns 20
print(our_cache.get(1010))
# returns -1 as 100 and 8000 are changed to most recently used and hence when cache is filled, 1010 is removed.


# In[6]:


our_cache = LRU_Cache(2)

our_cache.set('','')
# prints for asking to enter valid key and value
our_cache.set(1,1)
our_cache.set(2, 2)
print(our_cache.get(1))       
# returns 1
our_cache.set(3, 2)
print(our_cache.get(1))       
# returns 1
print(our_cache.get(2))       
# returns -1 (as 2 is removed when 3 is added because 2 was LRU)
print(our_cache.get(''))    
# return -1

#Handling null values
our_cache.set(None,None)
# prints for asking to enter valid key and value


# In[ ]:





# In[ ]:





# In[ ]:




