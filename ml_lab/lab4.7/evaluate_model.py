# ML: Evaluate Classification Model with Accuracy and Confusion Matrix

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

# Step 1: Load dataset
df = pd.read_csv("diabetes.csv")
X = df[["Age", "BMI", "Glucose"]]
y = df["Outcome"]

# Step 2: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 3: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 4: Make predictions
y_pred = model.predict(X_test)

# Step 5: Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", round(acc, 2))

# Step 6: Confusion Matrix
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print("\n Confusion Matrix:")
print("TN  FP")
print(f"{cm[0][0]:<3} {cm[0][1]}")
print("FN  TP")
print(f"{cm[1][0]:<3} {cm[1][1]}")
