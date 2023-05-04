#!/usr/bin/env python
# coding: utf-8

# ## COVID Data Analysis--Final Project IA241

# Data source: European Centre for Disease Prevention and Control (https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)

# ![IRAQ](https://cdn.britannica.com/28/1728-004-EBF4B6FF/Flag-Iraq.jpg)

# In[6]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd 


# In[7]:


get_ipython().system('pip install xlrd')


# In[8]:


df = pd.read_excel('s3://zindler-241-2023-python/covid_data.xls') 
df.head() 


# # COVID-19 Background 

# Coronavirus disease (COVID-19) is an infectious disease caused by the SARS-CoV-2 virus. Majority of people infected with the virus will experience mild to moderate respiratory illness and recover without requiring special treatment. However, some will become seriously ill and require medical attention. In March of 2020, there was a declared pandemic due to COVID-19 killing and hospitalizing millions.

# ## Question 1 What were the Top 30 Countries that Suffered the Highest Death Rates? (As of 2020)

# ###  Per Capita COVID-19 Deaths -- Top 30 Countries

# In[9]:


df ['per_capita_deaths']= df['deaths']/df['popData2019']
sum_deaths_per_capita_by_country = df.groupby('countriesAndTerritories')['per_capita_deaths'].sum()
sum_deaths_per_capita_by_country.nlargest(30).plot.bar()


# The bar chart displays the top 30 countries with the highest per capita COVID death rates during the year of 2020. Belgium and San Marino have the most reported COVID deaths by increased margins. European and Latin American countries are primarily represented on this data list.

# ## Iraq COVID-19 Data 

# This data is concentrated to the country of Iraq.

# In[21]:


Iraq_data = df.loc[df['countriesAndTerritories'] == 'Iraq']


# ## Question 2: What was the Number of Deaths Relating to the Number of Cases in Iraq Over Time?

# In[22]:


Iraq_data.plot.scatter(x='cases',y='deaths',c='month')


# This code shows the trend of COVID-19 deaths in relation to the trend of cases in Iraq as of December 2020. This was calculated by using the Iraq COVID-19 data and assigning variables to the number of deaths, number of cases, and time in months. X= 'cases', y='deaths', c='month'. Then a scatterplot was created to highlight the number of deaths similar to number of cases.

# ## Question 3: Which months had the highest cases in Iraq?
# 

# ### Selecting Iraq data 

# In[27]:


DE_data = df.loc[df['countriesAndTerritories'] == 'Iraq']
DE_data[:10] #the top 10 rows


# In[33]:


sum_cases_by_month= DE_data.groupby('month')['cases'].sum()
sum_cases_by_month.plot.bar()  


# This code depicts the amount of COVID-19 cases per month in the country of Iraq. This was calculated by grouping by the sum of the 'month' of the 'cases' and assigning it to the variable 'sum_cases_by_month. Then creating a bar plot by using the command sum_cases_by_month.plot.bar(). The month with the highest cases was month 9 with over 120000 cases in Iraq. 

# ## Conclusion, Limitation, and Further Research 

# In conclusion, the countries with the most cases are concentrated primarily in Latin American and European countries. It is the months from March to June that there are higher deaths due to COVID-19 cases in Iraq. The months with the highest COVID-19 cases in Iraq is in September.
# 
# The Limitations to this data is the data is from three years ago. New strands of COVID-19 have been discovered as well as vaccinations. This could fluctuate the data significantly. 
# 
# Suggestions for further research is to explore for recent COVID-19 data to see how these new vaccinations and strands influence this data. 

# In[ ]:




