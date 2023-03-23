#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import json
from pprint import pprint
api_key = '....'


# In[17]:


url = "http://www.omdbapi.com/?s="
api = "&apikey=" + api_key
movie_name = 'Star Trek'
omdb_type = 'series'
year = '2020'
combined_url = f'{url}{movie_name}{api}&type={omdb_type}&y={year}'
print(combined_url)


# In[9]:


# Performing a GET request similar to the one we executed
# earlier
response = requests.get(combined_url)


# In[10]:


# Converting the response to JSON, and printing the result.
data = response.json()
pprint(data)


# In[11]:


# Print a few keys from the response JSON.
data.keys()


# In[14]:


data["Search"][0]["Title"]


# In[ ]:




