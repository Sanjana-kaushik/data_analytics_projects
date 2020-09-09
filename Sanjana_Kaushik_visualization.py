#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('mathplotlib', 'inline')
import seaborn as sns


# In[126]:


df = pd.read_clipboard()


# In[127]:


df.head(5)


# In[128]:


df


# In[129]:


df = pd.read_clipboard(header = None)


# In[130]:


df


# In[131]:


df_math = df


# In[138]:


df_math.head(10)


# In[133]:


df_science = pd.read_clipboard(header = None)


# In[139]:


df_science.head(10)


# In[140]:


df_reading = pd.read_clipboard(header = None)


# In[141]:


df_reading.head(10)


# In[142]:


df_science


# In[143]:


df_reading


# In[144]:


df_math.columns = ['Str', 'Country', 'Score']


# In[145]:


df_math.head(5)


# In[148]:


df_reading.columns = ['Str', 'Country', 'Score']


# In[149]:


df_reading.head(5)


# In[150]:


df_science.columns = ['Str', 'Country', 'Score']


# In[151]:


df_science.head(5)


# In[152]:


df_final1 = pd.merge(df_math, df_science, on='Country', how='outer')


# In[153]:


df_final1.head(5)


# In[154]:


df_final2 = pd.merge(df_final1, df_reading, on='Country', how = 'outer')


# In[156]:


df_final2.head(5)


# In[157]:


del df_final2['Str_y']


# In[158]:


df_final2.head(5)


# In[159]:


df_final2.drop(['Str_x','Str'], axis = 1, inplace = True)


# In[160]:


df_final2.head(5)


# In[161]:


df_final2.columns =['Country','Math','Science','Reading']


# In[162]:


df_final2.head(5)


# In[163]:


df_final2.mean()


# In[164]:


df_final2['Average'] = (df_final2['Math'] + df_final2['Science'] + df_final2['Reading']) / 3


# In[165]:


df_final2.head(5)


# In[168]:


df_final2['Rank'] = df_final2['Average'].rank(ascending = False)


# In[169]:


df_final2.head(5)


# In[174]:


x = df_final2['Average']
y = df_final2['Math']
bins = 20
plt.hist(x, bins, facecolor='r', alpha=0.5, label='x')
plt.hist(y, bins,facecolor='b', alpha=0.5, label='y')
plt.legend(loc='upper right')
plt.xlabel('Value Range')
plt.ylabel('Probability')
plt.title('Assignment 6')
plt.show()


# In[203]:


df_Country = df_final2['Country']

def find_outliner(str):
    for index in range(0,len(str)):
       
        if (str[index] > ( (1.8 * (np.std(str)) + np.mean(str)))or (str[index] < (np.mean(str) -(1.8* np.std(str))))):
            print(" ["+ df_Country[index] +"]")
            
    return ""
        


    
    
            

print("The outliners in Math are ")
print((find_outliner(df_final2['Math'])))  

print("The outliners in Average are ")
print(find_outliner(df_final2['Average'])) 
print("The outliners in Science are ")
print(find_outliner(df_final2['Science'])) 
print("The outliners in Reading are ")
print(find_outliner(df_final2['Reading'])) 





      


# In[104]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




