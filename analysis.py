import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cars24data.csv") 
import pandas as pd

pd.set_option('display.max_columns', None)

# print(df.info())
# print(df.isnull().sum())
# Remove duplicate rows
# print(df.info())
# print(df.describe())  
# print(df['Manufacturing_year'].mean())
print(df['Engine capacity'].mean())
# Histogram of Engine Capacity
# df['Engine capacity'].value_counts().sort_index().plot(kind='bar', figsize=(12, 6))
# plt.title('Frequency of Engine Capacities')
# plt.xlabel('Engine Capacity (cc)')
# plt.ylabel('Number of Cars')
# plt.grid(True)
# plt.show()
# Pie Chart for Spare Keys & Transmission & Ownership & Fuel Type
spare_key_counts = df['Fuel type'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(5,5))
plt.pie(spare_key_counts, labels=spare_key_counts.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'red','green'])
plt.title('Distribution of Cars Transmission')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.show()

# KM driven mean 
# print(df['KM driven'].mean())