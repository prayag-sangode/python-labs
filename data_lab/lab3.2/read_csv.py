# Lab 1.1: Read CSV with Pandas

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("employees.csv")

# Print full DataFrame
print("=== Full Data ===")
print(df)

# Show first 3 rows
print("\n=== Top 3 Rows ===")
print(df.head(3))

# Show column-wise info
print("\n=== Info ===")
df.info()

# Summary stats for numeric columns
print("\n=== Summary ===")
print(df.describe())
