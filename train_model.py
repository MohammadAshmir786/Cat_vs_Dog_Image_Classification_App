# Import necessary libraries and modules
import os
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
from keras.regularizers import l2
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
from tensorflow.keras.models import save_model

# Function to define the CNN architecture
def create_cnn_model(input_shape, num_classes):
    """
    Builds and returns a Convolutional Neural Network (CNN) model.

    Parameters:
        input_shape (tuple): Shape of the input images (height, width, channels).
        num_classes (int): Number of classes for classification.

    Returns:
        model (Sequential): Compiled CNN model.
    """
    model = models.Sequential()

    # First convolutional block
    model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=input_shape))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))

    # Second convolutional block
    model.add(layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))

    # Third convolutional block
    model.add(layers.Conv2D(128, (3, 3), activation="relu"))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D((2, 2)))

    # Fully connected layers
    model.add(layers.Flatten())
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dropout(0.6))  # Dropout for regularization
    model.add(layers.Dense(num_classes, activation="softmax"))  # Output layer

    return model

# Function to load and preprocess the data
def load_data(data_dir, img_size, batch_size):
    """
    Loads and preprocesses the training and validation data.

    Parameters:
        data_dir (str): Directory containing the dataset.
        img_size (tuple): Target size of the images.
        batch_size (int): Number of samples per batch.

    Returns:
        train_generator: Generator for training data.
        validation_generator: Generator for validation data.
    """
    # Data augmentation configuration
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest",
        validation_split=0.2  # Reserve a portion for validation
    )

    # Training data generator
    train_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="training"
    )

    # Validation data generator
    validation_generator = datagen.flow_from_directory(
        data_dir,
        target_size=img_size,
        batch_size=batch_size,
        class_mode="categorical",
        subset="validation"
    )

    return train_generator, validation_generator

# Function to train the CNN model
def train_model(data_dir):
    """
    Trains the CNN model using the provided dataset.

    Parameters:
        data_dir (str): Directory containing the dataset.
    """
    # Configuration
    img_size = (150, 150)
    batch_size = 32
    epochs = 20  # Number of training epochs

    # Load the data
    train_data, val_data = load_data(data_dir, img_size, batch_size)

    # Create the CNN model
    model = create_cnn_model(
        input_shape=(150, 150, 3), num_classes=len(train_data.class_indices)
    )

    # Compile the model
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Train the model
    history = model.fit(train_data, validation_data=val_data, epochs=epochs)

    # Save the trained model
<<<<<<< HEAD
    save_model(model, "model/image_classify_model.keras")
=======
    save_model(model, "model/model_weights.keras")
>>>>>>> db8dc800d6016b4f63961a52d1aecc66998b3943

    # Optional: Plot the training and validation accuracy
    plt.plot(history.history["accuracy"], label="Training Accuracy")
    plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.title("Training and Validation Accuracy")
    plt.show()

# Entry point for the script
if __name__ == "__main__":
    data_dir = "data"  # Directory containing the dataset
    train_model(data_dir)
