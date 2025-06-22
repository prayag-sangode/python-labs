# Lab: Handwritten Digit Classification using MNIST + HTML Output

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
import numpy as np
import os

# Step 1: Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Normalize pixel values (0-255 → 0-1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 3: Convert labels to one-hot encoding
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# Step 4: Build the model
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))         # Flatten 28x28 image to 784
model.add(Dense(128, activation='relu'))         # Hidden layer
model.add(Dense(10, activation='softmax'))       # Output layer (10 classes)

# Step 5: Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Step 6: Train the model
model.fit(x_train, y_train_cat, epochs=5, batch_size=32, verbose=1)

# Step 7: Evaluate
loss, acc = model.evaluate(x_test, y_test_cat)
print(f"Test Accuracy: {acc:.2f}")

# Step 8: Predict on first 5 test images
predictions = model.predict(x_test[:5])
os.makedirs("images", exist_ok=True)
html_content = ["<h2>MNIST Dense NN Predictions</h2>"]

for i in range(5):
    img = x_test[i]
    label = np.argmax(predictions[i])
    filename = f"images/dense_img_{i}_pred_{label}.png"

    plt.imshow(img, cmap='gray')
    plt.title(f"Prediction: {label}")
    plt.axis('off')
    plt.savefig(filename)
    plt.close()

    html_content.append(f"<div><p>Prediction: {label}</p><img src='{filename}' width='100'></div>")

# Step 9: Save HTML report
with open("output_dense.html", "w") as f:
    f.write("<html><body>" + "\n".join(html_content) + "</body></html>")

print("📁 Predictions saved to 'images/' and 'output_dense.html'")
