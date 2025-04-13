import pandas as pd
import scipy.stats as stats

# Load dataset
df = pd.read_csv("Street_Centerline.csv")

# Drop rows with missing values in 'CLASS' and 'ONEWAY'
df_clean = df[['CLASS', 'ONEWAY']].dropna()

# Create a contingency table
contingency_table = pd.crosstab(df_clean['CLASS'], df_clean['ONEWAY'])

print("Contingency Table:")
print(contingency_table)

# Perform Chi-Square Test
chi2_stat, p_val, dof, expected = stats.chi2_contingency(contingency_table)

# Print results
print("\nChi-Square Test Results:")
print(f"Chi2 Statistic: {chi2_stat}")
print(f"Degrees of Freedom: {dof}")
print(f"P-Value: {p_val}")

# Interpretation
if p_val < 0.05:
    print("\nConclusion: There is a significant association between CLASS and ONEWAY.")
else:
    print("\nConclusion: No significant association between CLASS and ONEWAY.")
