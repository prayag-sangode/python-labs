# Lab : Basic Neural Network with Keras + HTML Output

import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import os

# Step 1: Load dataset
df = pd.read_csv("data.csv")
X = df[["Hours", "Marks"]]
y = df["Passed"]

# Step 2: Normalize input
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Step 4: Build model
model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(2,)))
model.add(Dense(1, activation='sigmoid'))

# Step 5: Compile
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 6: Train
model.fit(X_train, y_train, epochs=50, verbose=0)

# Step 7: Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.2f}")

# Step 8: Predict
new_input = [[6, 60]]
new_scaled = scaler.transform(new_input)
pred = model.predict(new_scaled)[0][0]
print("Predicted probability of passing:", round(pred, 2))

# Step 9: Save prediction chart
plt.figure()
plt.scatter(df["Hours"], df["Marks"], c=df["Passed"], cmap='coolwarm', label="Training Data")
plt.scatter(new_input[0][0], new_input[0][1], c='green', s=100, marker='x', label="New Student")
plt.title(f"Prediction: {round(pred, 2)} (Pass if > 0.5)")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend()
os.makedirs("images", exist_ok=True)
plt.savefig("images/student_prediction.png")
plt.close()

# Step 10: HTML Output
html = f"""
<html>
<head><title>Student Prediction</title></head>
<body>
    <h2>Prediction for New Student</h2>
    <p>Study Hours: 6, Marks: 60</p>
    <p><b>Predicted Probability of Passing: {round(pred, 2)}</b></p>
    <img src='images/student_prediction.png' width='400'>
</body>
</html>
"""

with open("output_student.html", "w") as f:
    f.write(html)

print("📁 Report generated: output_student.html")
