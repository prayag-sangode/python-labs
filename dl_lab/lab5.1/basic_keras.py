# Lab : Basic Neural Network with Keras

import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("data.csv")
X = df[["Hours", "Marks"]]   # Features
y = df["Passed"]             # Target

# Step 2: Normalize the input
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

# Step 4: Build the neural network
model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(2,)))  # Input + hidden layer
model.add(Dense(1, activation='sigmoid'))                 # Output layer for binary classification

# Step 5: Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Step 6: Train the model
model.fit(X_train, y_train, epochs=50, verbose=0)

# Step 7: Evaluate
loss, acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {acc:.2f}")

# Step 8: Predict a new student
new_student = scaler.transform([[6, 60]])  # 6 hrs, 60 marks
prediction = model.predict(new_student)[0][0]
print("Predicted probability of passing:", round(prediction, 2))
