import os
import subprocess

ruta_carpeta = r'C:\Users\carlo\Documents\python-process-automation\src\apps'

for archivo in os.listdir(ruta_carpeta):
    if archivo.endswith('.py'):
        ruta_archivo = os.path.join(ruta_carpeta, archivo)
        subprocess.run(['pyinstaller', '--onefile', '--windowed', ruta_archivo])
