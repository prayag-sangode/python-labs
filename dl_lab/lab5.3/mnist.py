# Lab: CNN with MNIST + HTML Report

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import matplotlib.pyplot as plt
import os

# Step 1: Load Data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Reshape and Normalize
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255

# Step 3: One-hot encode labels
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Step 4: Build CNN Model
model = Sequential([
    Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D(pool_size=(2,2)),
    Flatten(),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])

# Step 5: Compile Model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 6: Train
model.fit(x_train, y_train, epochs=5, batch_size=64, verbose=1)

# Step 7: Evaluate
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

# Step 8: Predict and Save Top 5 Images
predictions = model.predict(x_test[:5])
os.makedirs("images", exist_ok=True)
html_content = ["<h2>MNIST Predictions</h2>"]

for i in range(5):
    image_array = x_test[i].reshape(28, 28)
    label = np.argmax(predictions[i])
    filename = f"images/img_{i}_pred_{label}.png"

    plt.imshow(image_array, cmap='gray')
    plt.axis('off')
    plt.title(f"Predicted: {label}")
    plt.savefig(filename)
    plt.close()

    html_content.append(f"<div><p>Prediction: {label}</p><img src='{filename}' width='100'></div>")

# Step 9: Generate HTML Report
with open("output.html", "w") as f:
    f.write("<html><body>" + "\n".join(html_content) + "</body></html>")

print("📁 Saved predictions to 'images/' and report to 'output.html'")
