import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_csv("Street_Centerline.csv")

# Fill missing numeric values
df = df.fillna(df.mean(numeric_only=True))

# ----------------------------------------
# 📈 CORRELATION ANALYSIS
# ----------------------------------------

# Select important numeric columns
cols = ['LENGTH', 'Shape__Length', 'L_T_ADD', 'R_T_ADD']
correlation = df[cols].corr()

print("----- CORRELATION MATRIX -----")
print(correlation)

# ----------------------------------------
# 🧪 Z-TEST: Compare LENGTH of 'B' vs 'TF'
# ----------------------------------------

group_B = df[df['ONEWAY'] == 'B']['LENGTH']
group_TF = df[df['ONEWAY'] == 'TF']['LENGTH']

# Perform Z-test (Welch's t-test for unequal variances)
z_stat, p_val = stats.ttest_ind(group_B, group_TF, equal_var=False)

print("\n----- Z-TEST: LENGTH of ONEWAY 'B' vs 'TF' -----")
print(f"Z-statistic: {z_stat:.4f}")
print(f"P-value    : {p_val:.6f}")

# Interpretation hint
if p_val < 0.05:
    print("Conclusion: Significant difference in LENGTH between 'B' and 'TF' roads.")
else:
    print("Conclusion: No significant difference found.")
