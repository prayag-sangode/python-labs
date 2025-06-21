# Lab 1.5: Create Graphs with Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("employees_data.csv")

# Bar Chart: Salary by Employee
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Salary"], color='skyblue')
plt.title("Salary by Employee")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_salary_by_employee.png")
plt.close()

# Line Chart: Experience by Employee
plt.figure(figsize=(8,5))
plt.plot(df["Name"], df["Experience"], marker='o', linestyle='-', color='green')
plt.title("Experience by Employee")
plt.xlabel("Employee Name")
plt.ylabel("Years of Experience")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_experience_by_employee.png")
plt.close()

# Pie Chart: Department Distribution
dept_counts = df["Department"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Employee Distribution by Department")
plt.tight_layout()
plt.savefig("pie_department_distribution.png")
plt.close()

print("Graphs created: bar_salary_by_employee.png, line_experience_by_employee.png, pie_department_distribution.png")
