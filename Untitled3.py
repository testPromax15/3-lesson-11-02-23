#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
x=["Apple","Samsung","HTC","Honor","Xiomi"]
y=[1095,9966,1095,2300,10000]
plt.bar(x,y)
plt.plot(x,y,color="red",label="Линия продаж")
plt.xlabel("Наименовании компании")
plt.ylabel("Количество продаж")
plt.title("Объем продаж")
plt.grid ()
plt.text(0,30,"Тренд")
plt.show


# In[ ]:


import matplotlib.pyplot as plt
x=["Apple","Samsung","HTC","Honor","Xiomi"]
y=[1095,9966,1095,2300,10000]

plt.show

