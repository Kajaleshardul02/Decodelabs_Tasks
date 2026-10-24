# DecodeLabs AI Internship
## Project 4: OCR Text Recognition

### 📌 Project Overview

OCR Text Recognition is a Python-based project that extracts text from images using **Optical Character Recognition (OCR)**. The project uses OpenCV for image preprocessing and Tesseract OCR to recognize words and calculate their confidence scores.

The system converts images to grayscale, applies Gaussian blur and adaptive thresholding, identifies text in the processed image, and highlights words with a confidence score of 80% or higher.

It also saves the recognized text and confidence scores in a text file and generates an annotated image showing high-confidence words.

### 🎯 Objectives

- Load and process an image using OpenCV.
- Convert the image to grayscale.
- Apply Gaussian blur and adaptive thresholding.
- Extract text using Tesseract OCR.
- Obtain word-level confidence scores.
- Filter words with confidence scores of 80% or higher.
- Draw bounding boxes around high-confidence words.
- Save the annotated image and extracted text results.

### ✨ Features

- **Image Loading:** Reads an input image from the project folder.
- **Grayscale Conversion:** Converts the image into grayscale for preprocessing.
- **Gaussian Blur:** Reduces noise before text recognition.
- **Adaptive Thresholding:** Enhances text visibility against the background.
- **Tesseract OCR:** Extracts text from the processed image.
- **Confidence Analysis:** Records confidence scores for individual recognized words.
- **Word Filtering:** Identifies words with confidence scores of at least 80%.
- **Image Annotation:** Draws green bounding boxes and labels around high-confidence words.
- **Text Export:** Saves all detected words and high-confidence words to a text file.
- **Error Handling:** Handles missing images, OCR errors, and file-related errors.

### 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Image Processing Library:** OpenCV
- **OCR Engine:** Tesseract OCR
- **Python Package:** Pytesseract
- **Standard Library:** `pathlib`

### 📂 Project Structure

```text
DecodeLabs-AI-Internship/
│
├── text_recognition.py
├── sample_image.png
├── ocr_annotated.png
├── ocr_results.txt
└── README.md
```

**File descriptions:**

- `text_recognition.py` — Main Python program.
- `sample_image.png` — Input image containing readable text.
- `ocr_annotated.png` — Output image with bounding boxes around high-confidence words.
- `ocr_results.txt` — Output file containing detected words and confidence scores.
- `README.md` — Project documentation.

The two output files are generated when the program runs successfully.

### ⚙️ Installation and Setup

#### Step 1: Install Python

Download Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

#### Step 2: Install Required Python Libraries

Open Command Prompt or your terminal and run:

```bash
pip install opencv-python pytesseract
```

#### Step 3: Install Tesseract OCR

Pytesseract is a Python wrapper; the separate Tesseract OCR application must also be installed.

For Windows, download the installer from the Tesseract OCR project's installation documentation:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, check that the executable exists at:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The Python code is configured to use this path. If Tesseract is installed elsewhere, update `pytesseract.pytesseract.tesseract_cmd` in the script.

#### Step 4: Add the Input Image

Place an image containing clear, readable text in the same folder as `text_recognition.py`.

Name the image exactly:

```text
sample_image.png
```

The program expects a PNG image with this filename. If you use a JPG image instead, update `IMAGE_PATH` in the Python code accordingly.

#### Step 5: Run the Project

Open the terminal in the project folder and execute:

```bash
python text_recognition.py
```

If your Python file has a different name, replace `text_recognition.py` with the correct filename.

### 🧠 How the Project Works

1. **Load the Image:** OpenCV loads `sample_image.png` from the project directory.
2. **Convert to Grayscale:** `cv2.cvtColor()` converts the image to grayscale.
3. **Apply Gaussian Blur:** `cv2.GaussianBlur()` reduces noise that could interfere with text recognition.
4. **Apply Adaptive Thresholding:** `cv2.adaptiveThreshold()` converts the grayscale image into a binary image to improve text contrast.
5. **Extract Text:** Tesseract OCR recognizes words and returns their bounding-box coordinates and confidence scores.
6. **Filter Results:** The program identifies words with confidence scores of 80% or higher.
7. **Annotate the Image:** OpenCV draws green rectangles and word labels around qualifying words.
8. **Save Results:** The program saves the annotated image as `ocr_annotated.png` and the text report as `ocr_results.txt`.
9. **Display the Summary:** The terminal shows the recognized text, the total number of detected words, and the number of high-confidence words.

### 🔍 Key Functions and Libraries

| Function or Library | Purpose |
|---|---|
| `cv2.imread()` | Loads the input image |
| `cv2.cvtColor()` | Converts the image to grayscale |
| `cv2.GaussianBlur()` | Reduces image noise |
| `cv2.adaptiveThreshold()` | Enhances text-background contrast |
| `pytesseract.image_to_data()` | Extracts words, coordinates, and confidence scores |
| `cv2.rectangle()` | Draws bounding boxes around words |
| `cv2.putText()` | Adds recognized word labels to the image |
| `cv2.imwrite()` | Saves the annotated image |
| `Path` | Manages file paths |

### 📊 Confidence Score Filtering

The project uses the following threshold:

```python
CONFIDENCE_THRESHOLD = 80.0
```

Words with confidence scores of **80% or higher** are included in the high-confidence results and annotated image.

For example:

| Recognized Word | Confidence | Included in High-Confidence Results? |
|---|---:|---|
| DECODELABS | 96.50% | Yes |
| Python | 85.20% | Yes |
| OCR | 72.40% | No |
| Example | 55.00% | No |

*These values are illustrative examples, not actual results from your input image.*

A confidence score indicates how confident Tesseract is in its recognition. It does not guarantee that the recognized word is correct.

### 💻 Expected Output

After running the program successfully, the terminal displays information similar to the following:

```text
==================================================
       DECODELABS - PROJECT 4: OCR RECOGNITION
==================================================

Image: sample_image.png
Total words detected: [calculated count]
Words with confidence >= 80%: [calculated count]

Recognized text:
[Text extracted from the input image]

High-confidence words:
[Words with confidence scores >= 80%]

Annotated image: [path to ocr_annotated.png]
Text results: [path to ocr_results.txt]

OCR processing completed successfully.
```

The actual recognized text and confidence scores depend on the input image.

### 📁 Generated Output Files

**1. `ocr_annotated.png`**

Contains the original image with green bounding boxes and labels around words whose confidence scores meet the 80% threshold.

**2. `ocr_results.txt`**

Contains two sections:
- All detected words and their confidence scores.
- Words with confidence scores of 80% or higher.

### ⚠️ Limitations

- OCR accuracy depends on image quality, resolution, lighting, and text clarity.
- Blurry, rotated, handwritten, or distorted text may not be recognized correctly.
- The configured Tesseract executable path is specific to the current Windows setup.
- The program uses a fixed confidence threshold of 80%.
- The current implementation processes one image at a time.
- Confidence scores are estimates and do not guarantee correctness.

### 🚀 Future Improvements

- Support multiple image formats and batch image processing.
- Add support for multiple languages.
- Implement automatic image rotation and perspective correction.
- Create a graphical user interface (GUI).
- Export recognized text to PDF, CSV, or Word documents.
- Improve preprocessing for low-quality images.
- Add paragraph and line-level text extraction.

### 📚 Learning Outcomes

Through this project, I learned how to preprocess images using OpenCV, integrate Tesseract OCR with Python, extract word-level text and confidence scores, filter recognition results, annotate images, and save extracted data to files.

### 👨‍💻 Project Information

- **Organization:** DecodeLabs
- **Internship:** Artificial Intelligence Internship
- **Project Number:** 4
- **Project Title:** OCR Text Recognition
- **Programming Language:** Python
- **Libraries:** OpenCV and Pytesseract
- **OCR Engine:** Tesseract OCR

### 📄 License

This project is intended for educational and internship purposes. Add an appropriate open-source license if you plan to distribute the project publicly.

---

**Developed as part of the DecodeLabs AI Internship.**