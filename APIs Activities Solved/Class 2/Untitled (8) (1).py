#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests


# In[47]:


api_key = '..'
query = 'Bujumbura'
unit = "metric"


# In[48]:


base_url = 'https://api.openweathermap.org/data/2.5/weather?'
parameter_1 = 'q='
parameter_2 = '&appid='
parameter_3 = '&units='
combined_url = f"{base_url}{parameter_1}{query}{parameter_2}{api_key}{parameter_3}{unit}"
print(combined_url)


# In[49]:


data = requests.get(combined_url).json()
data


# In[46]:


data["main"]["temp"]


# In[50]:


cities = ["Paris", "Athens", "London", "Oslo", "Beijing", "Perth"]


# In[51]:


lat = []
temp = []


# In[54]:


for city in cities: 
    combined_url = f"{base_url}{parameter_1}{city}{parameter_2}{api_key}{parameter_3}{unit}"
    data = requests.get(combined_url).json()
    print(city)
    print(data["coord"]["lat"])
    lat.append(data["coord"]["lat"])
    print(data["main"]["temp"])
    temp.append(data["main"]["temp"])


# In[55]:


lat


# In[57]:


temp


# In[58]:


import pandas as pd


# In[59]:


weather_data = {
    "city" : cities,
    "lat" : lat, 
    "temp" : temp
}
weather_data


# In[60]:


weather_df = pd.DataFrame(weather_data)
weather_df.head()


# In[61]:


import matplotlib.pyplot as plt


# In[62]:


plt.scatter(weather_df["lat"], weather_df["temp"], marker="^")
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Celsius)")
plt.xlabel("Latitude")
plt.grid(True)
plt.show()


# In[ ]:




