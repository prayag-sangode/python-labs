# ML: Tune LogisticRegression with GridSearchCV

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

# Step 1: Load data
df = pd.read_csv("diabetes.csv")
X = df[["Age", "BMI", "Glucose"]]
y = df["Outcome"]

# Step 2: Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Step 3: Define the model and hyperparameter grid
model = LogisticRegression()

param_grid = {
    'C': [0.01, 0.1, 1, 10, 100],           # Regularization strength
    'solver': ['liblinear', 'lbfgs']        # Optimization algorithm
}

# Step 4: Use GridSearchCV
grid = GridSearchCV(model, param_grid, cv=5)
grid.fit(X_train, y_train)

# Step 5: Best parameters
print("Best Hyperparameters:")
print(grid.best_params_)

# Step 6: Test accuracy
y_pred = grid.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"\n Accuracy with Best Params: {acc:.2f}")
