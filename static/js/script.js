// Google Search Functionality
document.addEventListener("DOMContentLoaded", () => {
    const searchButton = document.getElementById("searchButton");
    const searchQuery = document.getElementById("searchQuery");

    // Enable the search button only when input is provided
    searchQuery.addEventListener("input", () => {
        searchButton.disabled = !searchQuery.value;
    });

    /**
     * Perform the search operation by opening a Google Search URL
     * with the user-provided query in a new tab.
     */
    function performSearch() {
        const query = searchQuery.value;
        if (query) {
            window.open(
                `https://www.google.com/search?tbm=isch&q=${query}`,
                "_blank"
            );
        }
    }

    // Execute the search on button click
    searchButton.onclick = performSearch;

    // Execute the search when the Enter key is pressed
    searchQuery.addEventListener("keypress", (event) => {
        if (event.key === "Enter") {
            performSearch();
        }
    });
});

// Drag-and-Drop or Select to Upload Image
const dropArea = document.getElementById("uploadArea");
const dropAreaText = document.getElementById("uploadAreaText");
const fileInput = document.getElementById("fileInput");
const browseFile = document.getElementById("clickToUpload");
const classifyBtn = document.getElementById("uploadButton");
const validImage = document.getElementById("upload_area_img");

/**
 * Reads and processes the uploaded file.
 * Stores the image in localStorage and updates the UI with a success message.
 * @param {File} file - The uploaded image file.
 */
function readAndStore(file) {
    if (file) {
        const reader = new FileReader();

        reader.onload = function (e) {
            e.preventDefault();
            localStorage.setItem("inputImage", e.target.result);
            dropArea.style.cssText = `height: auto; padding: 1rem !important;`;

            // Update the drop area with a success message
            const successTemplate = `
            <div class="row align-items-center">
                <div class="col-md-5 text-center">
                    <h2 class="text-success">Ready To Classify......!</h2>
                </div>
                <div class="col-md-7 text-end">
                    <img src="/static/images/success.gif" class="upload-area-img" alt="cat and dog waiting for upload" height="180px">
                </div>
            </div>`;
            dropArea.innerHTML = successTemplate;
            validImage.src = "/static/images/success.gif";
        };
        reader.readAsDataURL(file);
    }
}

// Handle drag-over event
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("dragover");
});

// Handle drag-leave event
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("dragover");
});

// Handle file drop event
dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropArea.classList.remove("dragover");

    const files = event.dataTransfer.files;
    if (files.length > 0) {
        const file = files[0];
        if (file.type.startsWith("image/")) {
            fileInput.files = files;
            readAndStore(file);
        }
    }
});

// Trigger file input click on button click
browseFile.addEventListener("click", () => {
    fileInput.click();
});

// Process the selected file
fileInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    readAndStore(file);
});

// Handle form submission
classifyBtn.addEventListener("click", (event) => {
    if (fileInput.files.length === 0) {
        dropAreaText.classList.add("glow", "error-effect");
        validImage.src = "/static/images/upload_error.png";
        validImage.setAttribute("height", "80px");

        // Reset UI after showing error
        setTimeout(() => {
            dropAreaText.classList.remove("glow", "error-effect");
            validImage.src = "/static/images/upload_waiting.png";
            validImage.setAttribute("height", "110px");
        }, 1500);
        event.preventDefault();
    }
});

// Display Results
window.onload = function () {
    if (window.location.href.includes("result")) {
        const uploadedImage = document.getElementById("uploadedImage");
        const inputImage = localStorage.getItem("inputImage");
        const resultLabel = document.getElementById("resultLabel").innerText;
        const resultGIF = document.getElementById("resultLabelImg");

        // Preview the uploaded image
        if (inputImage) {
            uploadedImage.src = inputImage;
        }

        // Display the appropriate result GIF
        if (resultLabel === "Cat") {
            resultGIF.src =
                "https://www.google.com/logos/fnbx/animal_paws/cat_kp_lm.gif";
        } else {
            resultGIF.src =
                "https://www.google.com/logos/fnbx/westminster_dog_show/westminster_kp_lm.gif";
        }
    }
};
