# Lab: Handwritten Digit Classification using MNIST

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Step 1: Load MNIST dataset (auto-downloads)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Step 2: Normalize pixel values (0-255 → 0-1)
x_train = x_train / 255.0
x_test = x_test / 255.0

# Step 3: Convert labels to one-hot encoding
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

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
model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)

# Step 7: Evaluate
loss, acc = model.evaluate(x_test, y_test)
print(f"Test Accuracy: {acc:.2f}")
