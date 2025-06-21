# Mini Project: Analyze Student Marks

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("student_marks.csv")

# Step 1: Calculate Total and Average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Step 2: Find Topper
topper = df.loc[df["Total"].idxmax()]

# Step 3: Print Summary
print("=== Student Marks Summary ===")
print(df[["Name", "Maths", "Science", "English", "Total", "Average"]])
print(f"\n Topper: {topper['Name']} with {topper['Total']} marks")

# Step 4: Bar Chart - Total Marks
plt.figure(figsize=(8,5))
sns.barplot(x="Name", y="Total", data=df, palette="viridis")
plt.title("Total Marks of Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("student_total_marks.png")
plt.close()

# Step 5: Line Chart - Subject Performance
plt.figure(figsize=(8,5))
for subject in ["Maths", "Science", "English"]:
    plt.plot(df["Name"], df[subject], marker='o', label=subject)

plt.title("Subject-wise Marks Comparison")
plt.ylabel("Marks")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("subject_wise_comparison.png")
plt.close()

print("\n Charts generated:")
print("- student_total_marks.png")
print("- subject_wise_comparison.png")
