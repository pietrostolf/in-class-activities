#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import requests
from pprint import pprint


# In[2]:


base_url = "http://api.worldbank.org/v2/"


# In[24]:


# Get the list of lending types the world bank has
lending_response = requests.get(f"{base_url}lendingTypes?format=json").json()
lending_types = [item["id"] for item in lending_response[1]]
lending_types


# In[25]:


# Next, determine how many countries fall into each lending type.
# Hint: Look at the first element of the response array.
totals = []
for ltype in lending_types: 
    data = requests.get(f"{base_url}countries?lendingType={ltype}&format=json").json()
    totals.append(data[0]["total"])


# In[27]:


# Print the number of countries of each lending type
for i in range(4):
    print(f"{lending_types[i]} has {totals[i]} lending countries. ")


# In[ ]:




