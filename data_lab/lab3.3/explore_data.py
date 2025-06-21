# Lab: Explore Data with Pandas

import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# View first few rows
print("=== Head (Top 5 Rows) ===")
print(df.head())  # default is 5

# View last few rows
print("\n=== Tail (Last 3 Rows) ===")
print(df.tail(3))  # last 3 rows

# View structure and column info
print("\n=== Info ===")
df.info()

# View summary statistics
print("\n=== Describe ===")
print(df.describe())
