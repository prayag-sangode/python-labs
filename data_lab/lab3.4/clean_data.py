# Lab 1.3: Clean Data - Remove Nulls, Rename Columns

import pandas as pd

# Read CSV
df = pd.read_csv("messy_data.csv")

print("=== Original Data ===")
print(df)

# Drop rows with any missing values
df_clean = df.dropna()

print("\n=== After Removing Nulls ===")
print(df_clean)

# Rename columns
df_clean.columns = ["Name", "Department", "Salary", "Experience"]

print("\n=== After Renaming Columns ===")
print(df_clean)

# Save cleaned version (optional)
df_clean.to_csv("cleaned_data.csv", index=False)
