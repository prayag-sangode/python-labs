# Lab 1.6: Beautiful Charts with Seaborn

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("employees_seaborn.csv")

# Set Seaborn style
sns.set(style="whitegrid")

# Barplot: Average Salary by Department
plt.figure(figsize=(8,5))
sns.barplot(x="Department", y="Salary", data=df, estimator=sum, ci=None, palette="pastel")
plt.title("Total Salary by Department")
plt.tight_layout()
plt.savefig("sns_bar_salary_by_dept.png")
plt.close()

# Scatterplot: Salary vs Experience
plt.figure(figsize=(8,5))
sns.scatterplot(x="Experience", y="Salary", hue="Department", data=df, palette="deep", s=100)
plt.title("Salary vs Experience (Colored by Department)")
plt.tight_layout()
plt.savefig("sns_scatter_salary_vs_experience.png")
plt.close()

# Boxplot: Salary Distribution by Department
plt.figure(figsize=(8,5))
sns.boxplot(x="Department", y="Salary", data=df, palette="Set2")
plt.title("Salary Distribution by Department")
plt.tight_layout()
plt.savefig("sns_box_salary_by_dept.png")
plt.close()

print(" Seaborn charts saved:")
print("- sns_bar_salary_by_dept.png")
print("- sns_scatter_salary_vs_experience.png")
print("- sns_box_salary_by_dept.png")
