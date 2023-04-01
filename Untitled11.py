#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
r=int(input())
pi=math.pi
t=2*pi*r
print(t)


# In[5]:


import math
math.e


# In[6]:


import math
math.pi


# In[7]:


import random
a=[1,5,62,89,"Зима",9]
e=random.choice(a)
print(e)


# In[8]:


import random
random.randrange(1000)


# In[9]:


import random
random.random()


# In[11]:


import random
random.randint(1,100)


# In[17]:


import random
a=[1,5,62,89,"Зима",9]
random.shuffle(a)
print(a)


# In[21]:


import random
print("Добро пожаловать в розыгрыш призов")
t=['Саша',"Саша","Саша"]
print("Победитель розыгрыша", random.choice(t))


# In[ ]:


import random
print("добро пожаловать в игру кальмара")
i=input("Введите имя первого игрока: ")
t=input("Введите имя второго игрока:  /n")
w=[1,2,3,4,5,6,7,8,9,10]
h=[1,2,3,4,5,6,7,8,9,10]
ScoreOne=0
scoreTwo=0
def throwDise():
    for j in range(5):
        random.shuffle(w)
        random.shuffle(h)
    return w[0] + h[0]
for j in range(3):
    result = throwDise()
    scoreOne += result
    print("Игрок",i,"выбросил: ",result)
    print("Сумма очков у игрока",i,":",ScoreOne)
    z=input("Чтобы сделать следующий бросок,нажмите enter /n")
    result = throwDise()
    scoreOne += result
    print("Игрок",i,"выбросил: ",result)
    print("Сумма очков у игрока",i,":",ScoreOne)
    z=input("Чтобы сделать следующий бросок,нажмите enter /n")
if (i>t):
    print("Игрок",i,"победил")
    print(i,"набрал",ScoreOne, "очков")        
elif(i<t):          
    print("Игрок",t,"победил")
    print(t,"набрал",ScoreTwo, "очков")        
else:
    print("ничия")


# In[ ]:




