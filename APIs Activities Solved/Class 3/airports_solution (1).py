#!/usr/bin/env python
# coding: utf-8

# # Exploring Airports in Australia

# In[5]:


# Dependencies
import pandas as pd
import numpy as np
import requests
import json
from pprint import pprint
import os

# Import API key
geoapify_key = os.environ["GeoApifyKey"]


# ## DataFrame Preparation

# In[6]:


# Import cities file as DataFrame
cities_pd = pd.read_csv("../Resources/cities.csv")
cities_pd.head()


# In[3]:


# Add columns the airports data we will fetch using the Geoapify API
# Note that we used "" to specify initial entry.
cities_pd["Lat"] = ""
cities_pd["Lon"] = ""
cities_pd["Airport Name"] = ""
cities_pd["IATA Name"] = ""
cities_pd["Airport Address"] = ""
cities_pd["Distance"] = ""
cities_pd["Website"] = ""
cities_pd.head()


# ## Look for Geographical Coordinates for Each City

# In[4]:


# Define the API parameters
params = {
    "apiKey":geoapify_key,
    "format":"json"
}

# Set the base URL
base_url = "https://api.geoapify.com/v1/geocode/search"


# In[5]:


# Print a message to follow up the airport search
print("Starting airport search")

# Loop through the cities_pd DataFrame and search coordinates for each city
for index, row in cities_pd.iterrows():

    # Get the city's name & add ", Australia" to the string so geoapify finds the correct city
    city = row["City"] + ", Australia"

    # Add the current city to the parameters
    params["text"] = f"{city}"

    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Convert response to JSON
    response = response.json()

    # Extract latitude and longitude
    cities_pd.loc[index, "Lat"] = response["results"][0]["lat"]
    cities_pd.loc[index, "Lon"] = response["results"][0]["lon"]
    
    # Log the search results
    print(f"Coordinates for {city} fetched...")

# Display sample data to confirm that the coordinates appear
cities_pd.head()


# ## Retrieve Airports' Information

# In[6]:


# Set parameters to search for airport's details
radius = 50000
params = {
    "categories":"airport",
    "apiKey": geoapify_key,
    "limit":20
}

# Print a message to follow up the airport search
print("Starting airport details search")

# Iterate through the types_df DataFrame
for index, row in cities_pd.iterrows():
    
    # Get the city's name
    city = row["City"]
    
    # Get latitude, longitude from the DataFrame
    latitude = row["Lat"]
    longitude = row["Lon"]
    
    # Add the current city's latitude and longitude to the params dictionary
    params["filter"] = f"circle:{longitude},{latitude},{radius}"
    params["bias"] = f"proximity:{longitude},{latitude}"
    
    # Set base URL
    base_url = "https://api.geoapify.com/v2/places"
           
    # Make an API request using the params dictionary
    response = requests.get(base_url, params=params)
        
    # Convert the API response to JSON format
    response = response.json()
    
    # Grab the first airport from the results and store the details in the DataFrame
    try:
        cities_pd.loc[index, "Airport Name"] = response["features"][0]["properties"]["name"]
        cities_pd.loc[index, "IATA Name"] = response["features"][0]["properties"]["datasource"]["raw"]["iata"]
        cities_pd.loc[index, "Airport Address"] = response["features"][0]["properties"]["address_line2"]
        cities_pd.loc[index, "Distance"] = response["features"][0]["properties"]["distance"]
        cities_pd.loc[index, "Website"] = response["features"][0]["properties"]["datasource"]["raw"]["website"]
    except KeyError as e:
        # If no airport is found, log the error.
        print(f"{e.args[0]} not found for {cities_pd.loc[index, 'Airport Name']}")
        
    # Log the search results
    print(f"nearest airport from {city}: {cities_pd.loc[index, 'Airport Name']}")

# Display sample data
cities_pd


# In[7]:


# Save Data to CSV
cities_pd.to_csv("Airport_Output.csv", index=False)

