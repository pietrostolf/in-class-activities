#!/usr/bin/env python
# coding: utf-8

# In[2]:


grades = {
    "Mike" : 87,
    "Jim" : 92,
    "James" : 83,
    "John" : 65
}


# In[6]:


try: 
    print(grades["Jim"])
except: 
    print("Student is not found!")


# In[7]:


myStudents = ["Mike", "Mary", "Jim", "John", "James", "Piro"]


# In[9]:


for student in myStudents: 
    try:
        print(grades[student])
    except:
        print("Student not found")
    print("-------------")


# In[ ]:




