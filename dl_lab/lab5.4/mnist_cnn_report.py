# Lab: CNN for MNIST + HTML Report with Image Previews

import numpy as np
import os
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])

# Compile and train
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(x_train, y_train_cat, epochs=3, verbose=1)

# Evaluate
loss, acc = model.evaluate(x_test, y_test_cat, verbose=0)
print(f" Test Accuracy: {acc:.2f}")

# Predict
predictions = model.predict(x_test)

# Create output folders
os.makedirs("html_images", exist_ok=True)

# Generate HTML Report
html = "<html><body><h1>MNIST Predictions</h1><table border='1' cellpadding='5'>"
html += "<tr><th>Index</th><th>Image</th><th>Actual</th><th>Predicted</th><th>Status</th></tr>"

for i in range(50):  # You can increase the number
    actual = y_test[i]
    predicted = np.argmax(predictions[i])
    status = "" if actual == predicted else "❌"

    # Save image
    img_path = f"html_images/img_{i}.png"
    plt.imsave(img_path, x_test[i].reshape(28, 28), cmap="gray")

    # Add row to HTML
    html += f"""
    <tr>
        <td>{i}</td>
        <td><img src='{img_path}' width='28'/></td>
        <td>{actual}</td>
        <td>{predicted}</td>
        <td>{status}</td>
    </tr>
    """

html += "</table></body></html>"

# Save HTML
with open("mnist_report.html", "w") as f:
    f.write(html)

print("HTML report generated: mnist_report.html")
