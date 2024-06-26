import os
import PyInstaller.__main__

tessdata_directory = '/opt/homebrew/Cellar/tesseract/5.3.4_1/share/tessdata'

if os.name == 'nt':  # Windows
    binaries = [
        'C:/Program Files/Tesseract-OCR/tesseract.exe;Tesseract-OCR',
        'C:/Program Files/Tesseract-OCR/tessdata;Tesseract-OCR/tessdata'
    ]
elif os.name == 'posix':
    if os.uname().sysname == 'Darwin':  # macOS
        binaries = [
            '/opt/homebrew/bin/tesseract:tesseract',
            '/opt/homebrew/Cellar/tesseract/5.3.4_1/share/tessdata:tessdata'
        ]
        tessdata_directory = '/opt/homebrew/Cellar/tesseract/5.3.4_1/share/tessdata'
    else:  # Linux
        binaries = [
            '/usr/bin/tesseract:tesseract',
            '/usr/share/tesseract-ocr/4.00/tessdata:tessdata'
        ]
else:
    raise RuntimeError(f"Unsupported OS: {os.name}")

PyInstaller.__main__.run([
    'main.py',
    '--name=ScreenText',
    '--onefile',
    '--windowed',
    '--add-binary', binaries[0],
    '--exclude', f'{tessdata_directory}/configs' if os.name == 'posix' and os.uname().sysname == 'Darwin' else '',
    '--add-binary', binaries[1]
])
