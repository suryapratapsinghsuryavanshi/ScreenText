from PIL import Image
import cv2
import pytesseract

def ocrs(image_path: str):
    no_noise = image_path
    img = Image.open(no_noise)
    ocr_result = pytesseract.image_to_string(img)
    print(ocr_result)
    
