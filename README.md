# Ex-08-Data-Visualization

# AIM:

To Perform Data Visualization on the given dataset and save the data to a file. 

# Explanation:

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, outliers, and patterns in data.

# ALGORITHM:

### STEP 1

Read the given Data

### STEP 2

Clean the Data Set using Data Cleaning Process

### STEP 3

Apply Feature generation and selection techniques to all the features of the data set

### STEP 4

Apply data visualization techniques to identify the patterns of the data.

# PROGRAM:

    #Import required libraries

    import pandas as pd

    import seaborn as sns

    import matplotlib.pyplot as plt

    #Load the dataset

    df = pd.read_csv('Superstore2.csv', encoding='unicode_escape')

    #Data Cleaning: Drop unnecessary columns

    df.drop(['Row ID', 'Order ID', 'Ship Date', 'Customer ID', 'Postal Code', 'Product ID'], axis=1, inplace=True)

    #Feature Generation: Extract Year and Month from Order Date

    df['Year'] = pd.DatetimeIndex(df['Order Date']).year

    df['Month'] = pd.DatetimeIndex(df['Order Date']).month_name()

    #1. Which Segment has Highest sales?

    segment_sales = df.groupby('Segment')['Sales'].sum().reset_index()

    plt.figure(figsize=(8,5))

    sns.barplot(x='Segment', y='Sales', data=segment_sales)

    plt.title('Segment-wise Sales')

    plt.show()

    #2. Which City has Highest profit?

    city_profit = df.groupby('City')['Profit'].sum().reset_index().sort_values(by='Profit', ascending=False)

    plt.figure(figsize=(12,8))

    sns.barplot(x='City', y='Profit', data=city_profit.head(10))

    plt.title('Top 10 Cities by Profit')

    plt.show()

    #3. Which ship mode is profitable?

    shipmode_profit = df.groupby('Ship Mode')['Profit'].sum().reset_index()

    plt.figure(figsize=(8,5))

    sns.barplot(x='Ship Mode', y='Profit', data=shipmode_profit)

    plt.title('Ship Mode-wise Profit')

    plt.show()

    #4. Sales of the product based on region

    region_sales = df.groupby('Region')['Sales'].sum().reset_index()

    plt.figure(figsize=(8,5))

    sns.barplot(x='Region', y='Sales', data=region_sales)

    plt.title('Region-wise Sales')

    plt.show()

    #5. Find the relation between sales and profit

    plt.figure(figsize=(8,5))

    sns.scatterplot(x='Sales', y='Profit', data=df)

    plt.title('Sales vs. Profit')

    plt.show()

    #6. Find the relation between sales and profit based on the following category.

    #i) Segment

    segment_sales_profit = df.groupby('Segment')['Sales', 'Profit'].mean().reset_index()
    
    plt.figure(figsize=(8,5))
    
    sns.barplot(x='Segment', y='Sales', data=segment_sales_profit, color='blue', alpha=0.5, label='Sales')
    
    sns.barplot(x='Segment', y='Profit', data=segment_sales_profit, color='green', alpha=0.5, label='Profit')
    
    plt.title('Segment-wise Sales and Profit')
    
    plt.legend()
    
    plt.show()

    #ii) City

    city_sales_profit = df.groupby('City')['Sales', 'Profit'].mean().reset_index().sort_values(by='Profit', ascending=False).head(10)
    
    plt.figure(figsize=(12,8))
    
    sns.barplot(x='City', y='Sales', data=city_sales_profit, color='blue', alpha=0.5, label='Sales')
    
    sns.barplot(x='City', y='Profit', data=city_sales_profit, color='green', alpha=0.5, label='Profit')
    
    plt.title('Top 10 Cities by Sales and Profit')
    
    plt.legend()
    
    plt.show()

    #iii) States

    plt.figure(figsize=(8,5))

    sns.scatterplot(x='Sales', y='Profit', hue='State', data=df)

    plt.title('Sales vs. Profit based on State')

    plt.show()

    #iv) Segment and Ship Mode

    plt.figure(figsize=(8,5))

    sns.scatterplot(x='Sales', y='Profit', hue='Segment', style='Ship Mode', data=df)

    plt.title('Sales vs. Profit based on Segment and Ship Mode')

    plt.show()

    #v) Segment, Ship mode and Region

    plt.figure(figsize=(8,5))

    sns.scatterplot(x='Sales', y='Profit', hue='Segment', style='Ship Mode', size='Region', data=df)

    plt.title('Sales vs. Profit based on Segment, Ship Mode and Region')

    plt.show()

# OUPUT:
![Figure_1](https://user-images.githubusercontent.com/91734840/235737847-4030b496-1d40-4664-ba02-ff9d1d1f2a70.png)
![Figure_2](https://user-images.githubusercontent.com/91734840/235737905-c36fdbc7-6a50-437f-bb62-c59b967e71a4.png)
![Figure_3](https://user-images.githubusercontent.com/91734840/235737962-fe1e4677-c170-49b7-9b59-460f1f90a9ba.png)
![Figure_4](https://user-images.githubusercontent.com/91734840/235737975-c96de982-6c50-43ac-800c-3a3eeb463b94.png)
![Figure_5](https://user-images.githubusercontent.com/91734840/235737991-2644ecaa-98f7-4b7e-b003-e7274124f74c.png)
![Figure_6](https://github.com/Siddarthan999/Ex-08-Data-Visualization/assets/91734840/8e2a3ca2-92a2-40d4-993f-7ec5a33e476b)
![Figure_7](https://github.com/Siddarthan999/Ex-08-Data-Visualization/assets/91734840/0b18e935-25a2-4489-8197-61c1e25f307e)
![Figure_8](https://user-images.githubusercontent.com/91734840/235738051-df018720-d391-4afd-aa4c-9e99051f3b9a.png)
![Figure_9](https://user-images.githubusercontent.com/91734840/235738081-fa581566-5c31-4a0d-a054-fc25344fb606.png)
![Figure_10](https://user-images.githubusercontent.com/91734840/235738093-68565df2-348d-49bb-a98e-2422ab591fab.png)

# RESULT:

Thus, to Perform Data Visualization on the given dataset and save the data to a file has been successfully performed.
