# -*- coding: utf-8 -*-
"""Covid - 19 Data Analysis Project using Python

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/178eAt0wnBrEr1_fPMZytREkPfvoM0TaI
"""

# 1. Import the dataset using Pandas from above mentioned url.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
Url = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')
Url

#2. High Level Data Understanding:
# a)Find no. of rows & columns in the dataset

#No of rows---
Url.shape[0]

#No of columns---
Url.shape[1]

# b)Data types of columns.
Url.dtypes

#c) Info & describe of data in dataframe.
#info---
Url.info()

#Describe--
Url.describe()

#3. Low Level Data Understanding 
# a)Find count of unique values in location column.
len(Url.location.unique())

# b) Find which continent has maximum frequency using values counts-

Url['continent'].value_counts().max()

#c. Find maximum & mean value in 'total_cases'.

#maximum value of "total_cases"--
Url['total_cases'].max()

#mean value of "total_cases"
Url['total_cases'].mean()

# d)Find 25%,50% & 75% quartile value in 'total_deaths'.

quartiles = Url['total_deaths'].describe(percentiles=[0.25, 0.5, 0.75])

print("25th quartile value:", quartiles['25%'])
print("50th quartile value :", quartiles['50%'])
print("75th quartile value:", quartiles['75%'])

#e)Find which continent has maximum 'human_development_index'.

maximum_continents = Url.groupby('continent')['human_development_index'].max()
maximum_continents = maximum_continents.idxmax()

print("Continent with maximum human_development_index:", maximum_continents)

# f)Find which continent has minimum 'gdp_per_capita'.
minimum_continents = Url.groupby('continent')['gdp_per_capita'].min()
minimum_continents = minimum_continents.idxmin()

print("Continent with minimum gdp_per_capita:", minimum_continents)

#4. Filter the dataframe with only this columns ['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index'] and update the data frame.

data = Url.loc[:, ['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']]
data

#5. Data Cleaning
# a)Remove all duplicates observations
Url.drop_duplicates(inplace=True)
Url

# b. Find missing values in all columns
missing_values = Url.isnull().sum()

print(missing_values)

#c)Remove all observations where continent column value is missing Tip : using subset parameter in dropna
Url.dropna(subset=['continent'],inplace = True)
Url

# d)Fill all missing values with 0
Url.fillna(0,inplace = True)
Url

#6. Date time format :
#a)Convert date column in datetime format using pandas.to_datetime
Url['date'] = pd.to_datetime(Url['date'])
Url

#b. Create new column month after extracting month data from date column.
Url['month'] = Url['date'].dt.month
Url

#7. Data Aggregation:
#a. Find max value in all columns using groupby function on 'continent' columnTip: use reset_index() after applying groupby
Url.groupby('continent').max().reset_index()

#  b. Store the result in a new dataframe named 'df_groupby'.(Use df_groupby dataframe for all further analysis)
df_groupby = Url.groupby('continent').max().reset_index()

print(df_groupby)

#8. Feature Engineering : a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'
df_groupby = Url['total_deaths_to_total_cases'] = Url['total_deaths'] / Url['total_cases']
df_groupby

# 9. Data Visualization :
# a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot.
df_groupby = sns.displot(Url['gdp_per_capita'])
df_groupby

#  b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
#df_groupby = Url.plot(kind = "scatter",x = "total_cases",y= "gdp_per_capita")
#df_groupby
df_groupby = px.scatter(x=Url['total_cases'],y = Url['gdp_per_capita'])
df_groupby

#d. Plot a bar plot of 'continent' column with 'total_cases' .
#Tip : using kind='bar' in seaborn catplot 
df_groupby = sns.catplot(data= Url, kind='bar', x='continent', y='total_cases')
df_groupby

#c. Plot Pairplot on df_groupby dataset.
df_groupby = Url.groupby(["continent"]).agg({"total_cases":"sum", "total_deaths":"sum", "population":"mean"}).reset_index()
sns.pairplot(df_groupby)

#10.Save the df_groupby dataframe in your local drive using pandas.to_csv function
df_groupby.to_csv('grouped_data.csv')