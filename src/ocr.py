from PIL import Image
import cv2
import os
import sys
import pytesseract
import pyperclip

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # sets the sys.frozen attribute and the executable path is in sys._MEIPASS
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = os.path.join(base_path, 'Tesseract-OCR', 'tesseract.exe')

def ocrs(image_path: str):
    no_noise = image_path
    img = Image.open(no_noise)
    ocr_result = pytesseract.image_to_string(img)
    pyperclip.copy(ocr_result)   
    # print(ocr_result)
