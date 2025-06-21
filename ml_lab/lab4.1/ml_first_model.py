# ML: Predict Height from Age using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression

# Step 1: Load data
df = pd.read_csv("height_data.csv")
X = df[["Age"]]          # Features
y = df["Height"]         # Target

# Step 2: Train model
model = LinearRegression()
model.fit(X, y)

# Step 3: Make predictions
ages = [[6], [10], [14]]
predictions = model.predict(ages)

print(" Predictions:")
for i, age in enumerate(ages):
    print(f"Age {age[0]} → Predicted Height: {round(predictions[i], 2)} cm")

# Optional: Check slope and intercept
print(f"\n Slope (Growth/cm per year): {model.coef_[0]:.2f}")
print(f" Intercept (starting height): {model.intercept_:.2f}")
