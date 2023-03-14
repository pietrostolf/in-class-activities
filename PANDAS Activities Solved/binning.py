#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import Dependencies
import pandas as pd


# In[3]:


raw_data = {
    'Class': ['Oct', 'Oct', 'Jan', 'Jan', 'Oct', 'Jan'], 
    'Name': ["Cyndy", "Logan", "Laci", "Elmer", "Crystle", "Emmie"], 
    'Test Score': [90, 59, 72, 88, 98, 60]}
df = pd.DataFrame(raw_data)
df


# In[4]:


bins = [0, 59.9, 69.9, 79.9, 89.9, 100]
#group_names = ["F", "D", "C", "B", "A"]
labels = ["F", "D", "C", "B", "A"]


# In[5]:


df["Grade"] = pd.cut(df["Test Score"], bins, labels=labels)
df.head()


# In[ ]:




