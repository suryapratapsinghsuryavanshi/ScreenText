import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--name=ScreenText',
    '--onefile',
    '--windowed',
    '--add-binary', 'C:/Program Files/Tesseract-OCR/tesseract.exe;Tesseract-OCR',
    '--add-binary', 'C:/Program Files/Tesseract-OCR/tessdata;Tesseract-OCR/tessdata'
])
