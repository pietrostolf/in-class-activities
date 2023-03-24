#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Dependencies
import requests
from config import api_key
import time

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

# Store a search term
query = "obama"

# Search for articles published between a begin and end date
begin_date = "20160101"
end_date = "20160130"

query_url = f"{url}api-key={api_key}&q={query}&begin_date={begin_date}&end_date={end_date}"


# In[8]:


# Retrieve articles
articles = requests.get(query_url).json()
articles_list = articles["response"]["docs"]

for article in articles_list:
    print(f'A snippet from the article: {article["snippet"]}')
    print('---------------------------')


# In[9]:


# BONUS: How would we get 30 results? 
# HINT: Look up the page query param

# Empty list for articles
articles_list = []

# loop through pages 0-2
for page in range(0, 3):
    query_url = f"{url}api-key={api_key}&q={query}&begin_date={begin_date}&end_date={end_date}"
    # create query with page number
    query_url = f"{query_url}&page={str(page)}"
    articles = requests.get(query_url).json()
    
    # Add a one second interval between queries to stay within API query limits
    time.sleep(1)
    # loop through the response and append each article to the list
    for article in articles["response"]["docs"]:
        articles_list.append(article)


# In[11]:


for article in articles_list:
    print(article['snippet'])
    print('---------------------------')


# In[ ]:




