#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 


# In[3]:


funcao   = lambda x : x**3 - x  - 2


# In[8]:


iteradas = 100
a=1
b=3
for i in range (iteradas):
    c= (a+b)/2
    if np.abs(funcao(c))< 0.001:
        print("a raiz é",c)
        break
    if np.sign(funcao(c)) == np.sign(funcao(a)):
        a=c
    else: b=c


# In[ ]:




