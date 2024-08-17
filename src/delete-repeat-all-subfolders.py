import os
from PIL import Image
from hashlib import md5

def buscar_imagenes_duplicadas(ruta_carpeta):
    hashes = {}
    duplicadas = []

    for root, dirs, files in os.walk(ruta_carpeta):
        for archivo in files:
            ruta_archivo = os.path.join(root, archivo)
            try:
                with Image.open(ruta_archivo) as img:
                    img_hash = md5(img.tobytes()).hexdigest()
                    if img_hash in hashes:
                        duplicadas.append((ruta_archivo, hashes[img_hash]))
                    else:
                        hashes[img_hash] = ruta_archivo
            except Exception as e:
                pass
    return duplicadas

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    imagenes_duplicadas = buscar_imagenes_duplicadas(ruta_carpeta)

    if imagenes_duplicadas:
        print("Se encontraron imágenes duplicadas:")
        for imagen1, imagen2 in imagenes_duplicadas:
            print(f"  - {imagen1} es una copia de {imagen2}")
            os.remove(imagen1)
            print(f"    - Se ha borrado: {imagen1}")
    else:
        print("No se encontraron imágenes duplicadas en la carpeta.")

"""

    - Eliminar las imagenes repetidas
    - En carpeta y sub carpetas (TENER CUIDADO)

"""