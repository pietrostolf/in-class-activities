#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Dependencies
import requests
from pprint import pprint


# In[11]:


base_url = "http://api.worldbank.org/v2/countries?"
parameter_1 = "format="
api_format = "json"
parameter_2 = '&page='
page_num = 1
combined_url = f"{base_url}{parameter_1}{api_format}{parameter_2}{page_num}"
#print(combined_url)

total_num_pages = 0
# Get country information in JSON format
data = requests.get(combined_url).json()

total_num_pages = data[0]["pages"]
#print(total_num_pages)

for country in data[1]:
    pprint(country["name"])

# First element is general information, second is countries themselves
for i in range(2, total_num_pages+1):
    combined_url = f"{base_url}{parameter_1}{api_format}{parameter_2}{i}"
    data = requests.get(combined_url).json()
    for country in data[1]:
        pprint(country["name"])


# In[ ]:




