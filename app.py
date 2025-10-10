# Import necessary libraries and modules
from flask import Flask, request, redirect, url_for, render_template
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model when the application starts
model = load_model("model/image_classify_model.keras")

# Define label mapping for predictions
labels = {0: "Cat", 1: "Dog"}

# Route for the home page
@app.route("/")
def index():
    """
    Render the index.html template as the homepage.
    """
    return render_template("index.html")

# Route to handle file uploads and classification results
@app.route("/result", methods=["POST"])
def upload_file():
    """
    Handles file uploads, processes the image, makes predictions,
    and returns the classification result with confidence level.
    """
    try:
        # Access the uploaded file
        file = request.files["file"]

        # Open the image using PIL
        img = Image.open(io.BytesIO(file.read()))

        # Preprocess the image
        img = img.resize((150, 150))  # Resize to match model's input size
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make predictions using the model
        predictions = model.predict(img_array)
        predicted_category_index = np.argmax(predictions, axis=1)[0]
        accuracy = max(predictions[0])  # Extract the highest prediction score
        acc_percentage = round(accuracy * 100)  # Convert to percentage

    except Exception as e:
        # Handle any errors and redirect to the homepage
        print(f"Error: {e}")
        return redirect(url_for("index"))

    # Render the result.html template with classification results
    return render_template(
        "result.html",
        result=f"{labels[predicted_category_index]}",
        confidence=f"{acc_percentage}%",
    )

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
