#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Dependencies
import requests
import json


# In[4]:


# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v2/launchpads"


# In[14]:


# Print the response object to the console
response = requests.get(url)
#myoutput = response.text
#type(myoutput)


# In[15]:


# Retrieving data and converting it into JSON
body = response.json()


# In[19]:


# Pretty Print the output of the JSON
from pprint import pprint 

pprint(body)


# In[21]:


body[0]["full_name"]


# In[24]:


for pad in body: 
    print(pad["full_name"])


# In[ ]:




