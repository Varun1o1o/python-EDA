import pandas as pd

# Load data
df = pd.read_csv("Street_Centerline.csv")

# Drop columns with all missing values
df = df.dropna(axis=1, how='all')

# Fill missing values in numeric columns with mean
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Convert date columns to datetime format
df["UPDATE_"] = pd.to_datetime(df["UPDATE_"], errors='coerce')
if "NEWSEGDATE" in df.columns:
    df["NEWSEGDATE"] = pd.to_datetime(df["NEWSEGDATE"], errors='coerce')

# Check cleaned data
print(df.info())
print(df.describe())
