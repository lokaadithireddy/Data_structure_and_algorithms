#!/usr/bin/env python
# coding: utf-8

# In[21]:


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


# In[22]:


print(sub_child.get_users())
# returns ["sub_child_user"]


# In[23]:

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name() or user in group.get_users():
        return True
    for g in group.get_groups():
        if is_user_in_group(user,g):
            return True
    return False

# In[24]:


# My test cases


print(is_user_in_group(sub_child_user, sub_child))  
# returns True
print(is_user_in_group('', child))  
# returns False
print(is_user_in_group(sub_child_user, parent))  
# returns True
print(is_user_in_group("parent", child))  
# returns False
print(is_user_in_group("child", child))  
# returns True
print(is_user_in_group("sub_child_user", parent))  
# returns True


# In[ ]:




