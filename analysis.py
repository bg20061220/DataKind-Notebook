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
# print(df['Engine capacity'].mean())
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
# plt.figure(figsize=(5,5))
# plt.pie(spare_key_counts, labels=spare_key_counts.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'red','green'])
# plt.title('Distribution of Cars Transmission')
# plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
# plt.show()

# KM driven mean 
# print(df['KM driven'].mean())
# num_models = df['Model Name'].nunique()
# print(f"Number of different car models: {num_models}")
# Finding the top 10 models by frequency 
# top_10_models = df['Model Name'].value_counts().head(10)

# # Plotting
# plt.figure(figsize=(10,6))
# top_10_models.plot(kind='bar', color='skyblue')
# plt.title('Top 10 Most Frequent Car Models')
# plt.xlabel('Model Name')
# plt.ylabel('Number of Listings')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# # Finding the average price of the top 10 models 
# top_10_models = df['Model Name'].value_counts().head(10).index

# # Filter the DataFrame for those models
# df_top_10 = df[df['Model Name'].isin(top_10_models)]

# Calculate average prices
# avg_prices = df_top_10.groupby('Model Name')['Price'].mean().sort_values(ascending=False)

# # Plotting the top 10 most ffrequent car models 
# plt.figure(figsize=(10,6))
# avg_prices.plot(kind='bar', color='orange')
# plt.title('Average Price of Top 10 Most Frequent Car Models')
# plt.xlabel('Model Name')
# plt.ylabel('Average Price')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt

# # Calculate the value counts
# ownership_counts = df['Ownership'].value_counts().sort_index()

# # Plotting
# ax = ownership_counts.plot(kind='bar', color='lightgreen')
# plt.title('Distribution of Cars by Number of Owners')
# plt.xlabel('Number of Previous Owners')
# plt.ylabel('Number of Listings')
# plt.xticks(rotation=0)

# # Adding labels on top of each bar
# for i, count in enumerate(ownership_counts):
#     ax.text(i, count + 5, str(count), ha='center', va='bottom', fontsize=10)

# plt.tight_layout()
# plt.show()

# Group by Model Name and count unique ownership values
model_ownership_groups = df.groupby('Model Name')['Ownership'].nunique()

# Filter models that appear under at least 2 ownership counts
multi_owner_models = model_ownership_groups[model_ownership_groups > 1].index

# Filter original dataframe for only those models
df_multi_owner = df[df['Model Name'].isin(multi_owner_models)]

avg_price_by_ownership = df_multi_owner.groupby(['Model Name', 'Ownership'])['Price'].mean().reset_index()
 # Pick top 3 models by frequency among multi-owner ones
top_models = df_multi_owner['Model Name'].value_counts().head(8).index

# Filter to just those
df_top_models = avg_price_by_ownership[avg_price_by_ownership['Model Name'].isin(top_models)]

# Plot using seaborn
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
sns.lineplot(data=df_top_models, x='Ownership', y='Price', hue='Model Name', marker='o')
plt.title('Price vs. Ownership Count for Top Models')
plt.xlabel('Number of Previous Owners')
plt.ylabel('Average Price')
plt.grid(True)
plt.tight_layout()
plt.show()

