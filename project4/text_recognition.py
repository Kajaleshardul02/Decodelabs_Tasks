
"""
DecodeLabs AI Internship
Project 4: OCR Text Recognition

Features:
- OpenCV image preprocessing
- Grayscale conversion
- Gaussian blur and adaptive thresholding
- Tesseract OCR
- Word-level confidence scores
- Filter words with confidence >= 80%
- Save annotated image and text results
"""

from pathlib import Path

import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# Use an image in the same folder as this Python file.
BASE_DIR = Path(__file__).resolve().parent
IMAGE_PATH = BASE_DIR / "sample_image.png"

ANNOTATED_PATH = BASE_DIR / "ocr_annotated.png"
RESULTS_PATH = BASE_DIR / "ocr_results.txt"

CONFIDENCE_THRESHOLD = 80.0

# If Tesseract is not detected automatically on Windows,
# uncomment the next line and check the installation path.
# pytesseract.pytesseract.tesseract_cmd = (
#     r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# )


def preprocess_image(image):
    """Prepare an image for OCR."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresholded = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        11
    )

    return thresholded


def extract_text(processed_image):
    """Extract words and their confidence scores."""
    data = pytesseract.image_to_data(
        processed_image,
        output_type=Output.DICT,
        config="--psm 6"
    )

    results = []

    for i, text in enumerate(data["text"]):
        text = text.strip()

        try:
            confidence = float(data["conf"][i])
        except (ValueError, TypeError):
            continue

        if text and confidence >= 0:
            results.append({
                "text": text,
                "confidence": confidence,
                "left": data["left"][i],
                "top": data["top"][i],
                "width": data["width"][i],
                "height": data["height"][i]
            })

    return results


def save_annotated_image(image, results):
    """Draw boxes around words with confidence >= 80%."""
    annotated = image.copy()

    for item in results:
        if item["confidence"] < CONFIDENCE_THRESHOLD:
            continue

        x = item["left"]
        y = item["top"]
        w = item["width"]
        h = item["height"]

        cv2.rectangle(
            annotated,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated,
            item["text"],
            (x, max(y - 5, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 128, 0),
            1
        )

    if not cv2.imwrite(str(ANNOTATED_PATH), annotated):
        raise OSError("Could not save the annotated image.")


def save_results(results):
    """Save all words and confidence scores to a text file."""
    with open(RESULTS_PATH, "w", encoding="utf-8") as file:
        file.write("DECODELABS - OCR RECOGNITION RESULTS\n")
        file.write("=" * 45 + "\n\n")

        file.write("ALL DETECTED WORDS\n")
        for item in results:
            file.write(
                f"{item['text']} - "
                f"{item['confidence']:.2f}% confidence\n"
            )

        file.write("\nWORDS WITH CONFIDENCE >= 80%\n")
        for item in results:
            if item["confidence"] >= CONFIDENCE_THRESHOLD:
                file.write(
                    f"{item['text']} - "
                    f"{item['confidence']:.2f}%\n"
                )


def main():
    print("=" * 50)
    print("       DECODELABS - PROJECT 4: OCR RECOGNITION")
    print("=" * 50)

    # No input() call: the image path is configured above.
    if not IMAGE_PATH.is_file():
        print("\nERROR: Image file not found.")
        print(f"Expected image location:\n{IMAGE_PATH}")
        print("\nPlace an image named sample_image.png in this folder.")
        return

    image = cv2.imread(str(IMAGE_PATH))

    if image is None:
        print("ERROR: The image exists but could not be opened.")
        print("Try using a valid JPG or PNG image.")
        return

    try:
        processed = preprocess_image(image)
        results = extract_text(processed)

        save_annotated_image(image, results)
        save_results(results)

    except pytesseract.TesseractNotFoundError:
        print("\nERROR: Tesseract OCR was not found.")
        print("Install the Tesseract OCR application.")
        print("If necessary, set its executable path near the imports.")
        return

    except pytesseract.TesseractError as error:
        print(f"\nTesseract OCR failed: {error}")
        return

    except OSError as error:
        print(f"\nFile error: {error}")
        return

    high_confidence = [
        item for item in results
        if item["confidence"] >= CONFIDENCE_THRESHOLD
    ]

    print(f"\nImage: {IMAGE_PATH.name}")
    print(f"Total words detected: {len(results)}")
    print(f"Words with confidence >= 80%: {len(high_confidence)}")

    print("\nRecognized text:")
    if results:
        print(" ".join(item["text"] for item in results))
    else:
        print("No text detected. Try a clearer image.")

    print("\nHigh-confidence words:")
    if high_confidence:
        for item in high_confidence:
            print(
                f"{item['text']} "
                f"({item['confidence']:.2f}%)"
            )
    else:
        print("No words met the 80% confidence threshold.")

    print(f"\nAnnotated image: {ANNOTATED_PATH}")
    print(f"Text results: {RESULTS_PATH}")
    print("\nOCR processing completed successfully.")


if __name__ == "__main__":
    main()
