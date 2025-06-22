# Lab: Predict Titanic Survival using Decision Tree

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Step 1: Load dataset
df = pd.read_csv("titanic.csv")

# Step 2: Encode categorical data
df["Sex"] = LabelEncoder().fit_transform(df["Sex"])  # male=1, female=0

# Step 3: Define features and target
X = df[["Pclass", "Sex", "Age", "SibSp", "Parch"]]
y = df["Survived"]

# Step 4: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 5: Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 7: Predict new passengers
new_passengers = pd.DataFrame([
    [3, 1, 30, 0, 0],  # male, 3rd class
    [1, 0, 25, 1, 1]   # female, 1st class
], columns=["Pclass", "Sex", "Age", "SibSp", "Parch"])

predictions = model.predict(new_passengers)

print("\nPredictions for New Passengers:")
for i, p in enumerate(predictions):
    status = "Survived" if p == 1 else "Did not survive"
    print(f"Passenger {i+1}: {status}")
