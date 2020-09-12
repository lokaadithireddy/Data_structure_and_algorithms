#!/usr/bin/env python
# coding: utf-8

# In[14]:


#!/usr/bin/env python
# coding: utf-8

# In[88]:


import os

def find_files(suffix, path='.'):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if(suffix is None or suffix ==''):
        print('please enter valid suffix')
        return
    try:
        list_of_paths = []
        if os.path.isfile(path):
            if path.endswith(suffix):
                return [path]
        else: 
            get_all_paths =  os.listdir(path)
            for val in get_all_paths:
                list_of_paths += find_files(suffix, path+'/'+val)
        return list_of_paths
    except:
        print('please enter valid directory')



# In[15]:


print('------------------------------------------------------------')
print(find_files('.c', 'testdir/subdir3'))


print('------------------------------------------------------------')
print(find_files('.c', '.'))


print('------------------------------------------------------------')
print(find_files('','testtest'))


print('------------------------------------------------------------')
print(find_files(None,'testdir'))


print('------------------------------------------------------------')
print(find_files('.c','testtest'))


# In[ ]:




