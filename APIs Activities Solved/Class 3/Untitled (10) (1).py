#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
from pprint import pprint
from config import geoapify_key


# In[5]:


geoapify_key


# In[6]:


url = f'https://api.geoapify.com/v1/geocode/search?text=Sydney%2C%20Australia&lang=en&type=city&format=json&apiKey={geoapify_key}'
print(url)


# In[7]:


data = requests.get(url).json()
pprint(data)


# In[12]:


print(data["results"][0]["lon"], data["results"][0]["lat"])


# In[19]:


url = f'https://api.geoapify.com/v1/geocode/search?text=Sydney%2C%20Australia&lang=en&type=city&format=json&apiKey={geoapify_key}'

base_url = 'https://api.geoapify.com/v1/geocode/search'
text = 'Toronto, Canada'
lang = 'en'
q_type = 'city'
q_format = 'json'


# In[20]:


params = {
    "text" : text,
    "lang" : lang,
    "type" : q_type,
    "format" : q_format
}


# In[21]:


response = requests.get(base_url, params=params)


# In[22]:


response.url


# In[28]:


url = 'https://api.geoapify.com/v2/places?categories=commercial.vehicle&conditions=no_fee&filter=place:51f63a16f2dbd853c059ccb2cf1489dc4540f00101f90173f2040000000000c00209920307546f726f6e746f&lang=en&limit=20&apiKey=YOUR_API_KEY'


base_url = 'https://api.geoapify.com/v2/places'
params = {
    "categories" : "commercial.vehicle",
    "conditions" : "no_fee",
    "lang" : "en", 
    "limit" : "40", 
    "filter" : 'place:51f63a16f2dbd853c059ccb2cf1489dc4540f00101f90173f2040000000000c00209920307546f726f6e746f',
    "apiKey" : geoapify_key
}


# In[29]:


data = requests.get(base_url, params=params).json()
pprint(data)


# In[34]:


len(data["features"])


# In[ ]:




