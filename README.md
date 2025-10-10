# 🐱🐶 Cat and Dog Image Classification Using CNN

This repository provides a simple Flask-based web application to classify images of cats 🐱 and dogs 🐶 using a ***Convolutional Neural Network (CNN)***. The application utilizes a pre-trained model ( *trained by train_model.py* ) stored in the `model` folder delivers an accuracy of **99.99%** 🎯, ensuring reliable predictions for uploaded images.

<br>

✨ Features
----------

-   **🔥 High Accuracy:** Achieves an impressive accuracy of **99.99%** on the dataset.
-   **🌟 User-Friendly Interface:** Easily upload an image and get instant results.
-   **🧠 Pre-Trained Model:** Leverages a powerful CNN for efficient binary classification ( *trained by train_model.py* ).
-   **⚡ Lightweight Flask Application:** A simple yet powerful backend for seamless operation.
-   **📂 Dataset Management:** Includes a script for automated dataset download and organization.
-   **🚀 Future-Ready:** Designed for scalability with plans for enhancements like multi-class classification and real-time predictions.

<br>

🚀 Getting Started
---------------

### ✅ Prerequisites

-   🐍 Python 3.7 or higher
-   📦 `pip` for managing Python packages

### ⚙️ Installation

1. **Clone the Repository**
   ```bash
    git clone https://github.com/MohammadAshmir786/Cat_vs_Dog_Image_Classification_App.git
    cd Cat_vs_Dog_Image_Classification_App.git
   ```

2. **Install the required libraries:**
   ```bash
    pip install -r requirements.txt

3. **Install `kagglehub` to download the dataset:**
   ```bash
    pip install kagglehub
   ```
<br>


🖼️ Usage
---------

### Step 1: Download the Dataset

📥 Download the dataset using the following command:
   ```bash
    python download_dataset.py
   ```

This script will download the dataset and print the path to the downloaded folder. Create a folder named `data` in the repository and move the dataset into it.

### Step 2: Run the Application

1.  ✅ Ensure the pre-trained model file is present in the `model` folder.
2.  ▶️ Start the Flask application:
    ```bash
    python app.py
    ```

3.  🌐 Open your web browser and navigate to `http://localhost:5000/`.

4.  📤 Upload an image of a cat 🐱 or dog 🐶 to the application.

5.  🎉 View the predicted class along with the probability score.

<br>

🤝 Contribution
---------

Contributions to this project are welcome! Follow the steps below to contribute:

1.  **Fork the Repository:**
    ```bash
    git clone https://github.com/your-username/cat-dog-classification.git
    ```
3.  **Create a new branch for your feature or bug fix:**
    ```bash
    git checkout -b feature-name
    ```
4.  **Commit your changes:**
    ```bash
    git commit -m "Description of your changes"
    ```
5.  **Push the branch to your fork:**
    ```bash
    git push origin feature-name
    ```

6.  **Submit a Pull Request** on the original repository.

<br>

🛠️ Troubleshooting
----------------

### Common Issues and Solutions

1.  **❌ Flask Application Not Starting**

    -   Ensure all dependencies are installed using `requirements.txt`.
    -   Verify Python version compatibility (Python 3.7 or higher).
2.  **📂 Dataset Not Found**

    -   Run the `download_dataset.py` script to download the dataset.
    -   Place the dataset in the `data` folder.
3.  **⚠️ Model File Missing**

    -   Ensure the pre-trained model file is available in the `model` folder.
4.  **🔧 KaggleHub Installation Issue**

    -   Reinstall KaggleHub using:
        ```bash
        pip install kagglehub
        ```
<br>

🚀 Future Enhancements
----------------------

1.  **🔍 Enhanced Model Performance:**

    -   Further train the model with augmented datasets.
    -   Explore advanced architectures like ResNet, VGG, or EfficientNet.
2.  **🎨 UI Improvements:**

    -   Add drag-and-drop functionality for uploading images.
    -   Improve visualization and user interaction.
3.  **☁️ Deployment:**

    -   Deploy the application on platforms like AWS, Google Cloud, or Heroku.
4.  **🐾 Multi-Class Classification:**

    -   Expand the model to classify additional animal species beyond cats 🐱 and dogs 🐶.
5.  **📹 Real-Time Classification:**

    -   Integrate live webcam support for real-time image predictions.

<br>

🙌 Acknowledgments
------------------
-   **💻 [Flask](https://flask.palletsprojects.com/en/2.2.x/) :** For providing a lightweight and efficient web framework.
-   **📊 [kagglehub](https://kaggle.com/datasets) :** For facilitating easy access to datasets.

<br>

📜 License
----------
This project is licensed under the [MIT License ↗️](https://github.com/MohammadAshmir786/Cat_vs_Dog_Image_Classification_App/blob/main/LICENSE)

<br>

📒 Contact
----------
If you have any questions or feedback, please feel free to [contact me ↗️](mailto:moashmir7003@gmail.com).

<br>

<h3 align="center">
   🎉 Experience the **99.99%** accuracy and bring the power of deep learning 🧠 to your fingertips! 🫵
</h3> 

