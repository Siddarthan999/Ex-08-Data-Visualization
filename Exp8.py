# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Superstore2.csv', encoding='unicode_escape')

# Data Cleaning: Drop unnecessary columns
df.drop(['Row ID', 'Order ID', 'Ship Date', 'Customer ID', 'Postal Code', 'Product ID'], axis=1, inplace=True)

# Feature Generation: Extract Year and Month from Order Date
df['Year'] = pd.DatetimeIndex(df['Order Date']).year
df['Month'] = pd.DatetimeIndex(df['Order Date']).month_name()

# 1. Which Segment has Highest sales?
segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='Segment', y='Sales', data=segment_sales)
plt.title('Segment-wise Sales')
plt.show()

# 2. Which City has Highest profit?
city_profit = df.groupby('City')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)
plt.figure(figsize=(12,8))
sns.barplot(x='City', y='Profit', data=city_profit.head(10))
plt.title('Top 10 Cities by Profit')
plt.show()

# 3. Which ship mode is profitable?
shipmode_profit = df.groupby('Ship Mode')['Profit'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='Ship Mode', y='Profit', data=shipmode_profit)
plt.title('Ship Mode-wise Profit')
plt.show()

# 4. Sales of the product based on region
region_sales = df.groupby('Region')['Sales'].sum().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='Region', y='Sales', data=region_sales)
plt.title('Region-wise Sales')
plt.show()

# 5. Find the relation between sales and profit
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', data=df)
plt.title('Sales vs. Profit')
plt.show()

# 6. Find the relation between sales and profit based on the following category.
# i) Segment
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='Segment', data=df)
plt.title('Sales vs. Profit based on Segment')
plt.show()

# ii) City
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='City', data=df)
plt.title('Sales vs. Profit based on City')
plt.show()

# iii) States
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='State', data=df)
plt.title('Sales vs. Profit based on State')
plt.show()

# iv) Segment and Ship Mode
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='Segment', style='Ship Mode', data=df)
plt.title('Sales vs. Profit based on Segment and Ship Mode')
plt.show()

# v) Segment, Ship mode and Region
plt.figure(figsize=(8,5))
sns.scatterplot(x='Sales', y='Profit', hue='Segment', style='Ship Mode', size='Region', data=df)
plt.title('Sales vs. Profit based on Segment, Ship Mode and Region')
plt.show()
