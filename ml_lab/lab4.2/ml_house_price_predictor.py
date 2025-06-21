# ML: Predict House Prices using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Load the dataset
df = pd.read_csv("house_prices.csv")
X = df[["Area", "Bedrooms"]]  # Features
y = df["Price"]               # Target

# Step 2: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 3: Predict new house prices
new_houses = [[1500, 3], [1800, 4], [2500, 5]]
predictions = model.predict(new_houses)

print("Predicted House Prices:")
for i, features in enumerate(new_houses):
    print(f"Area: {features[0]} sq.ft, Bedrooms: {features[1]} → Price: ${round(predictions[i], 2)}")

# Step 4: Model coefficients
print(f"\n Coefficients: Area = {model.coef_[0]:.2f}, Bedrooms = {model.coef_[1]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")
