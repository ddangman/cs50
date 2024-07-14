# environment variable to disable oneDNN optimizations
# must be set before importing tensorflow
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# To enable the following instructions: AVX2 AVX512F AVX512_VNNI AVX512_BF16 FMA, 
# in other operations, rebuild TensorFlow with the appropriate compiler flags.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

import tensorflow as tf
from sklearn.model_selection import train_test_split
import csv
import numpy as np


# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": 1 if row[4] == "0" else 0
        })

# Separate data into training and testing groups
evidence = [row["evidence"] for row in data]
labels = [row["label"] for row in data]
# convert to numpy arrays
evidence = np.array(evidence)
labels = np.array(labels)
X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size=0.4
)

# Create a sequential (1 layer after another) neural network
model = tf.keras.models.Sequential()

# Add a hidden layer with 8 units, with ReLU activation
# Dense means fully connected. Each unit in the layer is connected to each unit in the previous layer
model.add(tf.keras.Input(shape=(4,)))
model.add(tf.keras.layers.Dense(8, activation="relu"))

# Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Train neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
# epochs is the number of training iterations
model.fit(X_training, y_training, epochs=20)

# Evaluate how well model performs
model.evaluate(X_testing, y_testing, verbose=2)

