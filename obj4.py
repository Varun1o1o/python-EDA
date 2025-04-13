import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Street_Centerline.csv")

# Fill missing numeric values
df = df.fillna(df.mean(numeric_only=True))

# ---------------------------
# 1️⃣ Bar Chart: Count of Street Classes
# ---------------------------
plt.figure()
sns.countplot(data=df, x='CLASS')
plt.title("Count of Different Street Classes")
plt.xlabel("Street Class")
plt.ylabel("Count")
plt.show()

# ---------------------------
# 2️⃣ Pie Chart: Road Segments by Responsible Agency
# ---------------------------
agency_counts = df['RESPONSIBL'].value_counts()

plt.figure(figsize=(7,7))
plt.pie(agency_counts, labels=agency_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Distribution of Road Segments by Responsible Agency")
plt.axis('equal')  # Keeps the pie chart circular
plt.tight_layout()
plt.show()

# ---------------------------
# 3️⃣ Bar Chart: Average Length per ZIP Code (Left Side)
# ---------------------------
zip_group = df.groupby('ZIP_LEFT')['LENGTH'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
zip_group.plot(kind='bar', color='skyblue')
plt.title("Top 10 ZIP Codes by Average Road Length (Left)")
plt.xlabel("ZIP Code (Left)")
plt.ylabel("Average Road Length (meters)")
plt.tight_layout()
plt.show()
