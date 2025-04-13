import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Street_Centerline.csv")

# Fill missing numeric values (to avoid errors)
df = df.fillna(df.mean(numeric_only=True))

# Boxplot for LENGTH
plt.figure()
sns.boxplot(data=df, y='LENGTH')
plt.title("Box Plot of LENGTH")
plt.show()

# Heatmap of correlations
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Countplot for ONEWAY
plt.figure()
sns.countplot(data=df, x='ONEWAY')
plt.title("Count Plot of ONEWAY")
plt.show()

# Histogram for Shape__Length
plt.figure()
sns.histplot(df['Shape__Length'], bins=30, kde=True)
plt.title("Histogram of Shape__Length")
plt.show()
