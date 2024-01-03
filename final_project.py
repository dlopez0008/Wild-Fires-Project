import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker

co2_raw = pd.read_csv('Atmospheric_CO2_Concentrations.csv')
co2 = co2_raw[co2_raw['Unit'] == "Parts Per Million"]
co2 = co2[['Date', 'Value']].rename(columns={'Date': 'date', 'Value': 'ppm'})
co2['date'] = co2['date'].str.replace("M", "-")
co2['date'] = co2['date'] + '-01'
co2['date'] = pd.to_datetime(co2['date'])
co2['year'] = co2['date'].dt.year
co2['month'] = co2['date'].dt.month

co2 = co2[co2['date'] >= pd.to_datetime("1985-01-01")]

plt.figure(figsize=(10, 6))
plt.scatter(co2['date'], co2['ppm'], alpha=0.5, color='blue')
plt.title('Scatter Plot of Atmospheric CO2 Concentrations Over Time')
plt.xlabel('Year')
plt.ylabel('CO2 Concentration (Parts Per Million)')
plt.show()




df = pd.read_csv('federal_wildfiresfull.csv')

df['Fires'] = pd.to_numeric(df['Fires'].str.replace(',', ''), errors='coerce')
df_sorted = df.sort_values(by='Fires')

years = df_sorted['Year']
fires = df_sorted['Fires']

plt.figure(figsize=(10, 6))
plt.scatter(years, fires, color='blue', alpha=0.7)
plt.title('Federal Wildfires Over the Years')
plt.xlabel('Years')
plt.ylabel('Number of Fires')

plt.grid(True)
plt.show()

df['Acres'] = pd.to_numeric(df['Acres'].str.replace(',', ''), errors='coerce')

df_sorted = df.sort_values(by='Acres')

years = df_sorted['Year']
acres = df_sorted['Acres']

plt.figure(figsize=(10, 6))
plt.scatter(years, acres, color='green', alpha=0.7)
plt.title('Federal Wildfires Over the Years(Acres affected)')
plt.xlabel('Years')
plt.ylabel('Number of Acres')

plt.ticklabel_format(style='plain', axis='y')
plt.grid(True)
plt.show()




temp = pd.read_csv('surface_temp_annual.csv')
print(temp.columns)
temp['Year'] = pd.to_numeric(temp['Year'].str.replace('F', ''), errors='coerce')
temp['Temperature'] = pd.to_numeric(temp['Temperature'], errors='coerce')
temp_us = temp[temp['Country'] == 'United States']

plt.figure(figsize=(10, 6))
plt.scatter(temp_us['Year'], temp_us['Temperature'], color='blue', alpha=0.7)
plt.title('Surface Temperature in the United States Over the Years')
plt.xlabel('Year')
plt.ylabel('Temperature')

plt.grid(True)
plt.show()


merged_data = pd.merge(co2, df_sorted, left_on='year', right_on='Year', how='inner')

merged_data = merged_data.drop_duplicates(subset='year')

plt.figure(figsize=(10, 6))
plt.scatter(merged_data['ppm'], merged_data['Fires'], color='purple', alpha=0.7)
plt.title('Scatter Plot of CO2 Concentrations vs. Wildfires')
plt.xlabel('CO2 Concentrations (Parts Per Million)')
plt.ylabel('Number of Wildfires')

plt.grid(True)
plt.show()

merged_data = pd.merge(co2, df_sorted, left_on='year', right_on='Year', how='inner')

merged_data = merged_data.drop_duplicates(subset='year')

plt.figure(figsize=(10, 6))
plt.scatter(merged_data['ppm'], merged_data['Acres'], color='green', alpha=0.7)
plt.title('Scatter Plot of CO2 Concentrations vs. Acres Burned in Wildfires')
plt.xlabel('CO2 Concentrations (Parts Per Million)')
plt.ylabel('Number of Acres Burned')

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

plt.grid(True)
plt.show()


merged_data = pd.merge(temp_us, df, on='Year', how='inner')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Fires', data=merged_data, color='red', alpha=0.7)
plt.title('Scatter Plot of Surface Temperature vs. Wildfires')
plt.xlabel('Surface Temperature')
plt.ylabel('Number of Wildfires')

plt.grid(True)
plt.show()


merged_data = pd.merge(temp_us, df, on='Year', how='inner')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Temperature', y='Acres', data=merged_data, color='green', alpha=0.7)
plt.title('Scatter Plot of Surface Temperature vs. Acres Burned in Wildfires')
plt.xlabel('Surface Temperature')
plt.ylabel('Number of Acres Burned')

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

plt.grid(True)
plt.show()
