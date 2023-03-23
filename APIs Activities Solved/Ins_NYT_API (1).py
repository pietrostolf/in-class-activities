#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import requests
from pprint import pprint

api_key = '...'

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"


# In[2]:


# Search for articles that mention granola
query = "granola"


# In[3]:


# Build query URL
combined_url = f"{url}q={query}&api-key={api_key}"
print(combined_url)


# In[9]:


# Request articles
data = requests.get(combined_url).json()
# The "response" property in articles contains the actual articles


# In[20]:


pprint(data["response"]["docs"][4]["snippet"])


# In[21]:


# Print the web_url of each stored article
for article in data["response"]["docs"]:
    print(article["web_url"])
    


# In[ ]:




