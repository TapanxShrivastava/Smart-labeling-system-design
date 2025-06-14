# ocr_reader.py
import easyocr
import cv2

def read_label_image(image_path):
    reader = easyocr.Reader(['en'])  # Load English language model
    results = reader.readtext(image_path)

    print(f"\n🔍 OCR Results for: {image_path}")
    for (bbox, text, prob) in results:
        print(f" - Detected Text: {text} (Confidence: {prob:.2f})")
    
    return results

# Test the OCR with an existing label image
if __name__ == "__main__":
    test_image_path = "output_labels/label_test.png"  # replace with real file
    read_label_image(test_image_path)
