#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=[34,7.98,"fake"]
del(a[1])
print(a)


# In[3]:


a=[34,7.98,"fake"]
a.append("ship")
print(a)


# In[4]:


a=[34,7.98,"fake"]
a.append(48)
print(a)


# In[5]:


a=[34,7.98,"fake",100]
a.count(100)


# In[7]:


a=[34,7.98,"fake",100,100]
a.count(100)


# In[8]:


a=["soup"]
len(a)


# In[10]:


a=('soup")
a.index(2)


# In[11]:


a=[23,68,93,58,51,3,53,6]
a.sort()
a


# In[12]:


a=sorted([23,68,93,58,51,3,53,6],reverse=True)
print(a)


# In[14]:


a={"anne":"blue"}
print(a["anne"])


# In[21]:


a={"grisha":"green","lisa":"black"}
del(a["grisha"])
print(a)


# In[ ]:





# In[ ]:




