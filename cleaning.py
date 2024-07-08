#Data Cleaning
# 1.  Changing the datatype 
# 2.  Handling missing values
# 3.  Removing duplicates
# 4.  Renaming columns


import numpy as np
import pandas as pd 
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

fifa_data = pd.read_csv("FIFA WC data/WorldCupMatches.csv")
#print(fifa_data.head())

#print(fifa_data.columns)
#print(fifa_data.shape)
#print(fifa_data.info())

fifa_data['Datetime'] = fifa_data['Datetime'].str.replace('June', 'Jun')
fifa_data['Datetime'] = fifa_data['Datetime'].str.replace('July', 'Jul')
print(fifa_data.info())
#changing the datatype 
fifa_data['Datetime'] = pd.to_datetime(fifa_data['Datetime'])
fifa_data['Home Team Goals'] = pd.to_numeric(fifa_data['Home Team Goals'])
fifa_data['Away Team Goals'] = pd.to_numeric(fifa_data['Away Team Goals'])
fifa_data['Attendance'] = pd.to_numeric(fifa_data['Attendance'])

#float to int type
#fifa_data['Home Team Goals'] = fifa_data['Home Team Goals'].astype(int)
#fifa_data['Away Team Goals'] = fifa_data['Away Team Goals'].astype(int)
#fifa_data['Attendance'] = fifa_data['Attendance'].astype(int)
#fifa_data['Half-time Home Goals'] = fifa_data['Half-time Home Goals'].astype(int)
#fifa_data['Half-time Away Goals'] = fifa_data['Half-time Away Goals'].astype(int)
#fifa_data['RoundID'] = fifa_data['RoundID'].astype(int)
#fifa_data['MatchID'] = fifa_data['MatchID'].astype(int)

print(fifa_data.info(verbose=True))

#print(fifa_data.select_dtypes(include=['object']))

#Handling missing values
fifa_data = fifa_data.dropna()
print(fifa_data.isna().any(axis=1))


fifa_data.to_csv('FIFA WC data/WorldCupMatches_cleaned.csv', index=False)

# bar graph
plt.figure(figsize=(10, 6))
sns.histplot(pd.DataFrame(fifa_data['Home Team Goals']), bins=20, kde=True, color='blue', label='Home Team Goals')
sns.histplot(pd.DataFrame(fifa_data['Away Team Goals']), bins=20, kde=True, color='red', label='Away Team Goals')
plt.legend()
plt.title('Distribution of Goals Scored by Home and Away Teams')
plt.xlabel('Goals')
plt.ylabel('Frequency')
#plt.show()

correlation_matrix = fifa_data[['Home Team Goals', 'Away Team Goals', 'Attendance']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
#plt.show()


#Analysis
#number of matches played each year
plt.figure(figsize=(20, 5))
ax = sns.countplot(x='Year', data=fifa_data)
ax.set_title('Number of Matches Played Each Year' , color = 'white')
ax.set_xlabel('Year', color = 'white')
ax.set_ylabel('Number of Matches' , color = 'white')
ax.tick_params(colors = 'white' , which = 'both')
plt.xticks(rotation=45)
plt.show()

#average attendance per year
plt.figure(figsize=(20, 5))
ax = sns.barplot(x='Year', y='Attendance', data=fifa_data)
ax.set_title('Average Attendance Per Year' , color = 'white')
ax.set_xlabel('Year', color = 'white')
ax.set_ylabel('Average Attendance' , color = 'white')
ax.tick_params(colors = 'white' , which = 'both')
plt.xticks(rotation=45)
plt.show()

#teams per group
#plt.figure(figsize=(20, 5))
#sns.barplot(x=fifa_data.Stage.value_counts().index, 
#            y=fifa_data.Stage.value_counts().values).set_title("TEAM COUNTS PER GROUP", 
#                                                                          fontsize=30, color='white', pad = 20)
#plt.tick_params(colors='white', labelsize=20)
#plt.ylabel('COUNT', fontsize= 20, color='white')
#plt.xlabel('GROUP TYPE', fontsize= 20, color='white')
#plt.xticks(rotation=45)

#plt.show()