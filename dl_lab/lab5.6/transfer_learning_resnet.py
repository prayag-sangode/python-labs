# Lab: Transfer Learning using Pretrained ResNet50

import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import matplotlib.pyplot as plt

# Step 1: Load Pretrained ResNet50
model = ResNet50(weights='imagenet')  # Use pretrained ImageNet weights

# Step 2: Load and Preprocess a Test Image
img_path = "dog.jpg"  # <-- You can use any image
img = image.load_img(img_path, target_size=(224, 224))

plt.imshow(img)
plt.axis('off')
plt.title("Input Image")
plt.savefig("input_image.png")  # Save preview
plt.show()

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)  # Preprocessing required by ResNet50

# Step 3: Predict
preds = model.predict(x)

# Step 4: Decode Results
decoded = decode_predictions(preds, top=3)[0]
for i, (imagenetID, label, prob) in enumerate(decoded):
    print(f"{i+1}. {label}: {round(prob * 100, 2)}%")

# Step 5: Save as HTML
html_content = f"""
<html>
<head><title>ResNet50 Prediction</title></head>
<body>
    <h2>Prediction Result (ResNet50)</h2>
    <img src='input_image.png' width='300'><br>
    <ul>
        <li>{decoded[0][1]} - {round(decoded[0][2]*100, 2)}%</li>
        <li>{decoded[1][1]} - {round(decoded[1][2]*100, 2)}%</li>
        <li>{decoded[2][1]} - {round(decoded[2][2]*100, 2)}%</li>
    </ul>
</body>
</html>
"""

with open("resnet_output.html", "w") as f:
    f.write(html_content)

print("Prediction saved to resnet_output.html")
