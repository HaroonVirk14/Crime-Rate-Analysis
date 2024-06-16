import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('C:/Users/Haroon Virk/Downloads/Data Analysis/TSK-000-190/Montreal Crime Data.csv')


print("Column Names:", data.columns)


data.columns = data.columns.str.strip()


print(data.head())


data['date'] = pd.to_datetime(data['date'])
data['Month'] = data['date'].dt.month
data['Year'] = data['date'].dt.year
data['DayOfWeek'] = data['date'].dt.dayofweek


print(data.head())


crime_by_type = data['category'].value_counts()
print(crime_by_type)


crime_over_time = data.groupby('Year').size()
print(crime_over_time)


crime_by_location = data['neighbourhood'].value_counts()
print(crime_by_location)


plt.figure(figsize=(10, 6))
sns.barplot(x=crime_by_type.index, y=crime_by_type.values)
plt.title('Crime Incidents by Type')
plt.xlabel('Crime Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=0)
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(crime_over_time.index, crime_over_time.values)
plt.title('Crime Rates Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.show()


plt.figure(figsize=(10, 6))
sns.barplot(x=crime_by_location.index[:10], y=crime_by_location.values[:10])
plt.title('Top 10 Locations with Highest Crime Rates')
plt.xlabel('Location')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=0)
plt.show()


crime_by_month = data['Month'].value_counts().sort_index()
print(crime_by_month)


plt.figure(figsize=(10, 6))
crime_by_month.plot(kind='bar')
plt.title('Crime Incidents by Month')
plt.xlabel('Month')
plt.ylabel('Number of Incidents')
plt.show()


crime_by_day = data['DayOfWeek'].value_counts().sort_index()
print(crime_by_day)


plt.figure(figsize=(10, 6))
crime_by_day.plot(kind='bar')
plt.title('Crime Incidents by Day of the Week')
plt.xlabel('Day of the Week (0=Monday)')
plt.ylabel('Number of Incidents')
plt.show()


correlation_matrix = data[['count', 'longitude', 'latitude']].corr()
print(correlation_matrix)


plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()


top_locations = data['neighbourhood'].value_counts().head(10)
print(top_locations)


plt.figure(figsize=(10, 6))
top_locations.plot(kind='bar')
plt.title('Top 10 Crime Locations')
plt.xlabel('Location')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=0)
plt.show()
