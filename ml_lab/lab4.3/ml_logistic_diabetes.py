# ML-03: Predict Diabetes using Logistic Regression

import pandas as pd
from sklearn.linear_model import LogisticRegression

# Step 1: Load data
df = pd.read_csv("diabetes_data.csv")
X = df[["Glucose", "BMI", "Age"]]  # Features
y = df["Outcome"]                  # Target (0 or 1)

# Step 2: Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Step 3: Predict new patient outcomes
new_patients = [[110, 30.0, 36], [145, 37.0, 55]]
predictions = model.predict(new_patients)
probabilities = model.predict_proba(new_patients)

print("Diabetes Prediction:")
for i, patient in enumerate(new_patients):
    label = "Diabetic" if predictions[i] == 1 else "Not Diabetic"
    confidence = round(probabilities[i][predictions[i]] * 100, 2)
    print(f"Patient {i+1}: Glucose={patient[0]}, BMI={patient[1]}, Age={patient[2]} → {label} ({confidence}% confident)")
