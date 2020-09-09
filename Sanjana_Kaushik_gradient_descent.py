#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import python packages
from math import e
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from IPython.display import display,Math, Latex
display(Math(r'f(x) = x^4+200*(x+2000)^2+10000'))


# In[2]:


#define the x's range for plotting
x=np.arange(-120, 80, 0.1)


# In[3]:


#define f(x) based on the function 
def f(x):
    return (x)**4 + 200*(x + 2000)**2 + 10000


# In[4]:


#plot x vs. f(x)
plt.plot(x,f(x))


# In[5]:


def df(x):
    return 4*(x)**3 + 400*(x) + 800000


# In[6]:


x_new = 50
x_old = 70
gamma = 0.00001
precision = 1e-12



 
        


# In[7]:


def find_optimum(x_old,x_new,gamma,precision):
    x_search = [x_new]
    while abs(x_new - x_old) > precision:
        #x_search = [x_new]
        x_old = x_new
        x_new= x_old - gamma*df(x_old)
        x_search.append(x_new)

    print(x_search)
    print(len(x_search), 'iterations')
    print("The local optimum occurs at",(x_search[len(x_search) - 1]))
    print(gamma)
    #return  plt.show(range(0,len(x_search),df(x_search)))
(find_optimum(x_old,x_new,gamma,precision))







        
 


# In[8]:


#create a find_optimum function to automatically set gamma based on 
#t is the decrease rate of gamma
#x_search = [x_new]
def adaptive_optimum(x_old,x_new,gamma,t,precision):
    while True:
        gamma *=t
        x_old_try = x_old
        x_new_try = x_new
        
        for i in range(10000):
            x_old_try = x_new_try
            try:
                while abs(x_new_try - x_old_try) > precision:
                    x_old_try = x_new_try
                    x_new_try = x_old_try - gamma * df(x_old_try)
                    x_search.append(x_new_try)
                    x_final = x_search[len(x_search)-1]
                    if gamma < precision:
                        print("gamma values:", gamma)
                        print(x_final)
                    else:
                        break
            except:
                break
                    
            

   
        



        
        


# In[9]:


x_new = 50
x_old = 70
gamma = 1
t = 0.9
precision = 1e-12



# In[ ]:


adaptive_optimum(x_old,x_new,gamma,t,precision)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




