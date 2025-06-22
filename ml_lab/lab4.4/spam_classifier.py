# Lab 4.3: Spam Classification using Logistic Regression

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the data
df = pd.read_csv("spam_data.csv")

# Step 2: Convert text to features (Bag of Words)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["EmailText"])
y = df["Label"]

# Step 3: Encode labels
y = y.map({"not spam": 0, "spam": 1})

# Step 4: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 7: Predict new emails
new_emails = ["Congratulations! You’ve won a prize", "Let's meet for lunch tomorrow"]
new_X = vectorizer.transform(new_emails)
predictions = model.predict(new_X)

print("\nNew Email Predictions:")
for email, label in zip(new_emails, predictions):
    print(f"{email} --> {'SPAM' if label == 1 else 'NOT SPAM'}")
