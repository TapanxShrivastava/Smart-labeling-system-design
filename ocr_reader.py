#import easyocr
import easyocr
import cv2
import os

def read_label_image(image_path):
    if not os.path.exists(image_path):
        print(f"❌ ERROR: Image file does not exist at path: {image_path}")
        return []

    reader = easyocr.Reader(['en'])
    
    # ✅ Load image manually using OpenCV and check
    img = cv2.imread(image_path)

    if img is None:
        print(f"❌ ERROR: Failed to load image with OpenCV at: {image_path}")
        return []

    results = reader.readtext(img)

    print(f"\n🔍 OCR Results for: {image_path}")
    for (bbox, text, prob) in results:
        print(f" - Detected Text: {text} (Confidence: {prob:.2f})")
    
    return results
