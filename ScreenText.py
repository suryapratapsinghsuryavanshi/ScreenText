import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--name=ScreenText',
    '--onefile',
    '--windowed',
    "-i",
    './logo.ico'
])
