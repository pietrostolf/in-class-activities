#!/usr/bin/env python
# coding: utf-8

# In[1]:


census_api = '70d9f889fe9a252e3b1789035c7408208a1751fc'


# In[2]:


get_ipython().system(' pip install census')


# In[9]:


from census import Census
import pandas as pd 


c = Census(census_api)


# In[6]:


census_data = c.acs5.get(
    (
        "NAME",
        "B19013_001E",
        "B01003_001E",
        "B01002_001E",
        "B19301_001E",
        "B17001_002E"
    ),
    {"for" : "zip code tabulation area:*" }
)


# In[10]:


census_df = pd.DataFrame(census_data)
census_df.head()


# In[13]:


census_df = census_df.rename(
    columns = {
        "B01003_001E": "Population",
        "B01002_001E": "Median Age",
        "B19013_001E": "Household Income",
        "B19301_001E": "Per Capita Income",
        "B17001_002E": "Poverty Count",
        "NAME": "Name",
        "zip code tabulation area": "Zipcode"
    }
)
census_df.head()


# In[14]:


census_df["Poverty Rate"] = 100 * census_df["Poverty Count"] / census_df["Population"]
census_df.head()


# In[ ]:




