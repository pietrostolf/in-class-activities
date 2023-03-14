#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[18]:


file = "Resources/Seattle_Housing_Cost_Burden.csv"
file_df = pd.read_csv(file)
file_df.head()


# In[19]:


file_df["INCOME"] = file_df["INCOME"].map("${:,.2f}".format)
file_df["PERCENT3050"] = (file_df["PERCENT3050"]*100).map("{:.1f}%".format)
file_df["TOTAL"] = file_df["TOTAL"].map("{:,}".format)
file_df.head()


# In[ ]:




