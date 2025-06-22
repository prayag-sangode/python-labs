# ML: Group Customers using K-Means Clustering

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the dataset
df = pd.read_csv("customers.csv")

# Step 2: Select features (Annual Income and Spending Score)
X = df[["AnnualIncome", "SpendingScore"]]

# Step 3: Fit the KMeans model
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# Step 4: Print clustered data
print("=== Clustered Customers ===")
print(df)

# Step 5: Plot the clusters
colors = ["red", "green", "blue"]
plt.figure(figsize=(6, 6))
for i in range(3):
    cluster = df[df["Cluster"] == i]
    plt.scatter(cluster["AnnualIncome"], cluster["SpendingScore"], 
                c=colors[i], label=f"Cluster {i}")

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation (K-Means)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("customer_clusters.png")  # Save the plot
print("\nPlot saved as customer_clusters.png")
