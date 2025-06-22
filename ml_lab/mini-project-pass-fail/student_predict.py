# ML Mini Project: Predict Student Pass/Fail

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
df = pd.read_csv("students.csv")

# Step 2: Features and Target
X = df[["StudyHours", "Attendance", "HomeworkScore"]]
y = df["Result"]

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Evaluate the model
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.2f}")

# Step 6: Predict new student result using a DataFrame
new_student = pd.DataFrame([[6, 85, 70]], columns=["StudyHours", "Attendance", "HomeworkScore"])
prediction = model.predict(new_student)
print("Prediction for [6 hrs study, 85% attendance, 70 HW]:", "Pass" if prediction[0]==1 else "Fail")
