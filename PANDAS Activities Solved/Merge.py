#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


raw_data_info = {
    "customer_id": [112, 403, 999, 543, 123],
    "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
    "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
}
info_df = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
info_df


# In[3]:


# Create DataFrames
raw_data_items = {
    "customer_id": [403, 112, 543, 999, 654],
    "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
    "cost": [3.00, 4.50, 600, 900, 150]
}
items_df = pd.DataFrame(raw_data_items, columns=[
                        "customer_id", "item", "cost"])
items_df


# In[16]:


output_df = pd.merge(items_df, info_df, on=["customer_id"], how="inner") #outer, inner, left, right
output_df


# In[ ]:




