import os
import PyInstaller.__main__

if os.name == 'nt':  # Windows
    binaries = [
        'C:/Program Files/Tesseract-OCR/tesseract.exe;Tesseract-OCR',
        'C:/Program Files/Tesseract-OCR/tessdata;Tesseract-OCR/tessdata'
    ]
elif os.name == 'posix':
    if os.uname().sysname == 'Darwin':  # macOS
        binaries = [
            '/usr/local/bin/tesseract;tesseract',
            '/usr/local/share/tessdata;tessdata'
        ]
    else:  # Linux
        binaries = [
            '/usr/bin/tesseract;tesseract',
            '/usr/share/tesseract-ocr/4.00/tessdata;tessdata'
        ]
else:
    raise RuntimeError(f"Unsupported OS: {os.name}")

PyInstaller.__main__.run([
    'main.py',
    '--name=ScreenText',
    '--onefile',
    '--windowed',
    '--add-binary', binaries[0],
    '--add-binary', binaries[1]
])
