#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import matplotlib.pyplot as plt 


# $f(x) = x^2 - 3x +1$
# 
# $ \frac{df(x)}{dx} = 2x -3$

# In[5]:


funcao   = lambda x : x**2 - 3*x + 1

d_funcao = lambda x : 2*x-3


# In[11]:


iteradas = 10
x = 10
for i in range(iteradas):
    x = x  - funcao(x)/d_funcao(x)
    print(x)


# In[12]:


#teste
print(funcao(x))


# In[ ]:




