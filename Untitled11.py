#!/usr/bin/env python
# coding: utf-8

# In[2]:


#задание 1:Калькулятор
a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a//b)


# In[4]:


#задание 2
a=int(input())
b=int(input())
c=int(input())
d=((a+2)/(b+5))**4-0.001*c
print(d)


# In[6]:


a=int(input())
if(a>=1 and a<=2):
    print("зима")
elif(a>=3 and a<=5):
    print("весна")
elif(a>=6 and a<=8):
    print("лето")
elif(a>=9 and a<=11):
    print("осень")
elif(a==12):
    print("зима")
else:
    print("Ошибка")


# In[7]:


a=int(input())
if a<=0:
    print("Нет здоровья")
else:
    print("Есть здоровья")


# In[16]:


a=int(input())
if   (a == 1):
    print("Понедельник")
elif (a == 2):
    print("Вторник")
elif (a == 3):
    print("Среда")
elif (a == 4):
    print("Четверг")
elif (a == 5):
    print("Пятница")
elif (a == 6):
    print("Суббота")
elif (a == 7):
    print("Воскресенья")
else:
    print("Ошибка")
      


# In[19]:


a=int(input())
print(str(a)+ " Киллометров это " + str(a*1000)+ " Метров ")


# In[22]:


#практическая задача 1
sample={3,25,1221}
sample={3,25}
s=sample-sample
print(s)
print(type(s))


# In[23]:


sample=['abc',25,1221]
print(sample[2])


# In[25]:


for i in range(5,10):
    print(i)


# In[27]:


for i in range(5,10):
    print(i)


# In[29]:


sum=0
for i in range(0,21):
    sum=sum+i
    print(sum)


# In[31]:


a=[14,14,45,6,57,68,7,6,8,68,6,86,68,6,89,77,857,64]
for i in a:
    print(i*2)


# In[32]:


a=['white','red','black','grey','green']
for i in a:
    print("Color: " + i)


# In[33]:


a=0
while (a <10):
    a=a+2
    print(a)


# In[ ]:


d=int(input()) 
for i in range(0,d + 1):
    print(i)


# In[ ]:


d=int(input()) 
for i in range(0,d + 1):
    print(i)


# In[35]:


d=int(input())
c=int(input())
for i in range(d,c + 1):
    print(i)


# In[ ]:


d=int(input())
c=int(input())
if (d<c):
    for i in range(d,c):
        print(i)
else:
    for i in range(d,c, - 1):
        print(i)


# In[1]:





# In[ ]:


d=int(input())
c=int(input())
if (d<c):
    for i in range(d,c):
        print(i)
else:
    for i in range(d,c,-1):
        print(i)


# In[3]:


d=int(input())
c=int(input())
if (d<c):
    for i in range(d,c):
        print(i)
else:
    for i in range(d,c,-1):
        print(i)


# In[4]:


sum=0
a=int(input())
for i in range(0,a+1):
    sum=sum+i
    print(sum)


# In[ ]:




