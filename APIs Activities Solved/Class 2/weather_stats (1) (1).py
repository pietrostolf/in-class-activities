#!/usr/bin/env python
# coding: utf-8

# In[38]:


# Dependencies
import requests
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from pprint import pprint


# In[6]:


# Save config information.
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
units = "metric"
api_key = 'f63015d444cb11f63b0c3b241efec560'

# Build partial query URL
parameter_1 = 'q='
parameter_2 = '&appid='
parameter_3 = '&units='


# In[10]:


# Get latitude and temperature for cities
cities = ["Paris", "London", "Oslo", "Beijing", "Mumbai", "Manila", "New York", "Seattle", "Dallas", "Taipei"]

# set up lists to hold reponse info
lat = []
temp = []

# Loop through the list of cities and perform a request for data on each
for city in cities:
    combined_url = f"{base_url}{parameter_1}{city}{parameter_2}{api_key}{parameter_3}{units}"
    response = requests.get(combined_url).json()
    lat.append(response['coord']['lat'])
    temp.append(response['main']['temp'])

print(f"The latitude information received is: {lat}")
print(f"The temperature information received is: {temp}")


# In[11]:


# create a data frame from cities, lat, and temp
weather_dict = {
    "city": cities,
    "lat": lat,
    "temp": temp
}
weather_data = pd.DataFrame(weather_dict)
weather_data


# In[12]:


# Create a Scatter Plot for temperature vs. latitude
plt.scatter(weather_data["lat"], weather_data["temp"])
plt.show()


# In[14]:


# Perform a linear regression on temperature vs. latitude
(slope, intercept, rvalue, pvalue, stderr) = linregress(weather_data["lat"], weather_data["temp"])

# Get regression values
regress_values = slope * weather_data["lat"] + intercept


# In[19]:


# Create line equation string
line_eq = f"y = {round(slope, 2)}x + {round(intercept, 2)}"
print(line_eq)


# In[21]:


# Create Plot
plt.scatter(weather_data["lat"], weather_data["temp"])
plt.plot(weather_data["lat"], regress_values)

# Label plot and annotate the line equation
plt.annotate(line_eq, (20, 5), color='red')

# Print r square value
print(rvalue**2)

# Show plot
plt.show()


# In[23]:


# Use the line equation to predict the temperature for Florence at a latitude of 43.77 degrees
florence_lat = 43.77
predicted_flor = (florence_lat * slope) + intercept
print(predicted_flor)


# In[33]:


# Use API to determine actual temperature
city = "Florence"
combined_url = f"{base_url}{parameter_1}{city}{parameter_2}{api_key}{parameter_3}{units}"
print(combined_url)
response = requests.get(combined_url).json()
print(response["coord"]["lat"])
print(response["main"]["temp"])


# In[50]:


city = "London"
combined_url = f"{base_url}{parameter_1}{city}{parameter_2}{api_key}{parameter_3}{units}"
data = requests.get(combined_url).json()
pprint(data)
print("---------------------------")


# In[52]:


try: 
    print(data["wind"]["speed"])
    print(data["wind"]["gust"])
except: 
    print("some data not avaiable")


# In[ ]:




