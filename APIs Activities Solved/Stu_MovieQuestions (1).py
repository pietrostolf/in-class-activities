#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Dependencies
import requests
import json
from pprint import pprint 
from config import api_key 
from pprint import pprint
print(api_key)
base_url = f"http://www.omdbapi.com"
paramater_1 = "t="
parameter_2 = "apikey="


# In[24]:


# Who was the director of the movie Aliens?
movie_title = "Aliens"
combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
data = requests.get(combined_url).json()
pprint(data["Director"])


# In[26]:


# What was the movie Gladiator rated?
movie_title = "Gladiator"
combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
data = requests.get(combined_url).json()
pprint(data["Rated"])


# In[28]:


# What year was 50 First Dates released?
movie_title = "50 First Dates"
combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
data = requests.get(combined_url).json()
pprint(data["Released"])


# In[30]:


# Who wrote Moana?
movie_title = "50 First Dates"
combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
data = requests.get(combined_url).json()
pprint(data["Writer"])


# In[33]:


# What was the plot of the movie Sing?
movie_title = "Sing"
combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
data = requests.get(combined_url).json()
pprint(data["Plot"])


# In[34]:


movies = ["Aliens", "Gladiator", "50 First Dates", "Moana", "Sing"]


# In[35]:


output = []


# In[36]:


for movie_title in movies: 
    combined_url = f"{base_url}/?{paramater_1}{movie_title}&{parameter_2}{api_key}"
    data = requests.get(combined_url).json()
    output.append(data["Plot"])


# In[37]:


output


# In[ ]:




