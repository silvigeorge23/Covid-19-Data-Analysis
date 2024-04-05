#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
from datetime import datetime


# In[20]:


covid_df = pd.read_csv(r"C:\Users/silvi/Downloads/Covid-19/covid_19_india.csv")


# In[21]:


covid_df.head(10)


# In[22]:


covid_df.info()


# In[23]:


covid_df.describe()


# In[26]:


#Learn how to drop unnecessary columns


# In[27]:


covid_df.drop(columns=["Sno","Time","ConfirmedIndianNational","ConfirmedForeignNational"], inplace = True, axis = 1)


# In[28]:


covid_df.head()


# In[29]:


#Change format of date column


# In[30]:


covid_df["Date"] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')


# In[31]:


covid_df.head()


# In[32]:


#Find total number of active cases. Confirmed-(Cured+Deaths)


# In[33]:


covid_df['Active_cases'] = covid_df['Confirmed']-covid_df['Cured']+ covid_df['Deaths']
covid_df.tail()


# In[34]:


#Create a pivot table


# In[35]:


statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"],
                           index = "State/UnionTerritory", aggfunc = max)


# In[36]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise["Confirmed"]


# In[37]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise["Confirmed"]


# In[38]:


statewise = statewise.sort_values(by = "Confirmed", ascending = False)


# In[39]:


#Plot Pivot table (CMAP = Colour Map provided by MatPlotlib)


# In[40]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[41]:


# Top 10 active cases states


# In[49]:


top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[["Active_cases", "Date"]].sort_values(by=['Active_cases'], ascending =False).reset_index()


# In[50]:


fig = plt.figure(figsize =(16,9))


# In[51]:


plt.title("Top 10 States with Most Active Cases in India", size = 25)


# In[54]:


ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "red")


# In[55]:


top_10_active_cases = covid_df.groupby(by = "State/UnionTerritory").max()[["Active_cases", "Date"]].sort_values(by=['Active_cases'], ascending =False).reset_index()
fig = plt.figure(figsize =(16,9))
plt.title("Top 10 States with Most Active Cases in India", size = 25)
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = "Active_cases", x = "State/UnionTerritory", linewidth = 2, edgecolor = "red")

plt.xlabel("States")
plt.ylabel("Total Active Cases")


# In[58]:


#Find top 10 States with highest deaths

top_10_deaths = covid_df.groupby(by = "State/UnionTerritory").max([["Deaths","Date"]]).sort_values(by = ["Deaths"],ascending = False).reset_index()

fig = plt.figure(figsize = (18,5))

plt.title("Top 10 States with Most Deaths", size = 25)

ax = sns.barplot(data = top_10_deaths.iloc[:12],y="Deaths", x = "State/UnionTerritory", linewidth = 2, edgecolor = "black")

plt.xlabel("States")
plt.ylabel("Total Death Cases")
plt.show

