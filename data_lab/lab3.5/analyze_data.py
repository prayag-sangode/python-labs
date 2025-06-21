# Lab: Analyze Data - Mean, Median, Count, GroupBy

import pandas as pd

# Load data
df = pd.read_csv("analyze_data.csv")

# Show raw data
print("=== Raw Data ===")
print(df)

# Mean salary and experience
print("\n=== Overall Statistics ===")
print("Average Salary:", df["Salary"].mean())
print("Median Salary:", df["Salary"].median())
print("Total Employees:", df["Name"].count())

# Group by department and analyze
print("\n=== Grouped by Department ===")
grouped = df.groupby("Department")[["Salary", "Experience"]].mean()
print(grouped)

# Count per department
print("\n=== Employee Count per Department ===")
print(df["Department"].value_counts())
