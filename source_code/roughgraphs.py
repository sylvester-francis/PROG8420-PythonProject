#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import init_notebook_mode, iplot


# In[19]:


pwd


# In[26]:


df = pd.read_csv('Downloads\\building.csv')
df


# In[27]:


fig1 = px.histogram(df, x = "province", color = "isAvailable")
fig1.show()


# In[28]:


fig1 = px.histogram(df, x = "City", color = "isFurnished")
fig1.show()


# In[9]:


df1 = pd.read_csv('Downloads\\apartment1.csv')
df1


# In[13]:


#df1['Rent'] = df1['rentPrice'].str.split('$', expand=True)[0]
df1['Rent'] = df1['rentPrice'].str.replace("[$]", '').astype(int)
df1


# In[14]:


df1['noOfWashrooms'] = df1['noOfWashrooms'].astype(str)
df1.info()


# In[15]:


#df1['Rent'] = pd.to_numeric(df1['Rent'])
#df1.head()


# In[16]:


fig1 = px.bar(df1, y = "Rent", x = "unitType", color = "Rent",color_continuous_scale=px.colors.sequential.Viridis, title = "Rent based on Unit Type",labels = {"unitType":"Unit Type"} )
fig1.show()


# In[43]:


df2 = pd.read_csv('Downloads\\rental.csv')
df2


# In[44]:


df2['Rent'] = df2['rentalPrice'].str.replace("[$]", '').astype(int)
df2


# In[58]:


fig1 = px.bar(df2, x = "City", y = "Rent",color="City", title = "Rent across City" )
fig1.show()


# In[ ]:


barmode = 'group'

