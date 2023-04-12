from PIL import Image
import cv2
import pytesseract

def ocrs():
    no_noise = "test_data\semple_text.png"
    img = Image.open(no_noise)
    ocr_result = pytesseract.image_to_string(img)
    print(ocr_result)
    
