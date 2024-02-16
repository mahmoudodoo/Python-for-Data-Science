
import tensorflow as tf
from tensorflow.keras import layers

# Define a simple sequential model
def create_model():
    model = tf.keras.Sequential([
        layers.Dense(512, activation='relu', input_shape=(784,)),
        layers.Dropout(0.2),
        layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Create a model instance
model = create_model()

# Model summary
model.summary()
