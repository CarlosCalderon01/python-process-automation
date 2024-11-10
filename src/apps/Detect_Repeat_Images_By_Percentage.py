import os
from PIL import Image
import numpy as np
import shutil

def calcular_histograma(imagen):
    histograma = imagen.histogram()
    histograma = np.array(histograma).astype(float)
    return histograma / np.sum(histograma)

def comparar_histogramas(hist1, hist2):
    distancia = np.linalg.norm(hist1 - hist2)
    # Se asume que 1.0 es la distancia máxima para normalizar el porcentaje de similitud
    similitud = max(0, 1 - distancia) * 100
    return similitud

def buscar_imagenes_similares(ruta_carpeta, umbral=90):
    imagenes = []
    similares = []

    for root, dirs, files in os.walk(ruta_carpeta):
        for archivo in files:
            ruta_archivo = os.path.join(root, archivo)
            try:
                with Image.open(ruta_archivo) as img:
                    img = img.convert('RGB')
                    histograma = calcular_histograma(img)
                    imagenes.append((ruta_archivo, histograma))
            except Exception as e:
                print(f"No se pudo procesar el archivo {ruta_archivo}: {e}")

    for i, (ruta1, hist1) in enumerate(imagenes):
        for j, (ruta2, hist2) in enumerate(imagenes[i+1:], i+1):
            similitud = comparar_histogramas(hist1, hist2)
            if similitud >= umbral:
                similares.append((ruta1, ruta2, similitud))

    return similares

def mover_imagenes_similares(similares, ruta_similares):
    if not os.path.exists(ruta_similares):
        os.makedirs(ruta_similares)
    
    for imagen1, imagen2, similitud in similares:
        base1 = os.path.basename(imagen1)
        base2 = os.path.basename(imagen2)
        
        destino1 = os.path.join(ruta_similares, base1)
        destino2 = os.path.join(ruta_similares, base2)
        
        if not os.path.exists(destino1):
            shutil.move(imagen1, destino1)
        if not os.path.exists(destino2):
            shutil.move(imagen2, destino2)

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    umbral = float(input("Introduce el umbral de similitud en porcentaje (por ejemplo, 90): "))
    ruta_similares = os.path.join(ruta_carpeta, "similares")
    
    imagenes_similares = buscar_imagenes_similares(ruta_carpeta, umbral)

    if imagenes_similares:
        print("Se encontraron imágenes similares:")
        for imagen1, imagen2, similitud in imagenes_similares:
            print(f"  - {imagen1} es similar a {imagen2} con una similitud del {similitud:.2f}%")
        
        mover_imagenes_similares(imagenes_similares, ruta_similares)
        print(f"Las imágenes similares se han movido a la carpeta: {ruta_similares}")
    else:
        print("No se encontraron imágenes similares en la carpeta.")
