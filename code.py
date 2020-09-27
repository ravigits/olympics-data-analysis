# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data = pd.read_csv(path)
data.rename(columns={"Total": "Total_Medals"}, inplace=True)
print(data.head(10))
# Summer or Winter
data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer', np.where(data['Total_Summer']<data['Total_Winter'], 'Winter','Both'))
better_event = data['Better_Event'].value_counts().sort_values(ascending=False).index[0]
print(better_event)

# Top 10
top_countries = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(df,col):
    country_list = []
    top10 = df.nlargest(10, col)
    country_list = list(top10['Country_Name'])
    return country_list

top_10_summer = top_ten(top_countries, 'Total_Summer')
print('Top 10 Summer - ',top_10_summer)
top_10_winter = top_ten(top_countries, 'Total_Winter')
print('Top 10 Winter - ',top_10_winter)
top_10 = top_ten(top_countries, 'Total_Medals')
print('Top 10 - ',top_10)
common =  list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print('Common countries - ', common)
# Plotting top 10
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

plt.figure(figsize=(10,4))
summer_df.plot(x='Country_Name', y='Total_Summer', kind='bar')
plt.title('Top 10 Summer')
plt.xlabel('Country Name')
plt.ylabel('Total Summer Medals')
plt.show()


winter_df.plot(x='Country_Name', y='Total_Winter', kind='bar')
plt.title('Top 10 Winter')
plt.xlabel('Country Name')
plt.ylabel('Total Winter Medals')
plt.show()


top_df.plot(x='Country_Name', y='Total_Medals', kind='bar')
plt.title('Top 10')
plt.xlabel('Country Name')
plt.ylabel('Total Medals')

plt.show()

# Top Performing Countries
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio']  == summer_df['Golden_Ratio'].max()]['Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio']  == winter_df['Golden_Ratio'].max()]['Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = list(top_df[top_df['Golden_Ratio']  == top_df['Golden_Ratio'].max()]['Country_Name'])
top_country_gold = top_country_gold[0]
# Best in the world 
data_1 = data[:-1]
data_1['Total_Points'] = (data_1['Gold_Total']*3) + (data_1['Silver_Total']*2) + (data_1['Bronze_Total'])
most_points = data_1['Total_Points'].max()
print('Most points - ', most_points)
best_country = list(data_1[data_1['Total_Points'] == data_1['Total_Points'].max()]['Country_Name'])
best_country = best_country[0]
print('Best country - ', best_country)

# Plotting the best
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked='False')
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()


