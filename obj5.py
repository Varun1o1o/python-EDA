import pandas as pd

# Load the dataset
df = pd.read_csv("Street_Centerline.csv")

# Fill missing values in numeric columns
df = df.fillna(df.mean(numeric_only=True))

# IQR Method for 'LENGTH'
Q1 = df['LENGTH'].quantile(0.25)
Q3 = df['LENGTH'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df['LENGTH'] < lower_bound) | (df['LENGTH'] > upper_bound)]

print("Outliers in LENGTH column:")
print(outliers[['LENGTH']].head())
