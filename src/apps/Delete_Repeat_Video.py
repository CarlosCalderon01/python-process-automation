import os
from hashlib import md5

def calcular_hash_video(ruta_archivo, bloque_size=65536):
    """Calcula el hash MD5 de un archivo de video en bloques."""
    hash_md5 = md5()
    try:
        with open(ruta_archivo, "rb") as f:
            for bloque in iter(lambda: f.read(bloque_size), b""):
                hash_md5.update(bloque)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Error al procesar {ruta_archivo}: {e}")
        return None

def buscar_videos_duplicados(ruta_carpeta):
    hashes = {}
    duplicados = []

    # Recorrer la carpeta y subcarpetas
    for root, dirs, files in os.walk(ruta_carpeta):
        for archivo in files:
            if archivo.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm')):
                ruta_archivo = os.path.join(root, archivo)
                video_hash = calcular_hash_video(ruta_archivo)
                
                if video_hash:
                    if video_hash in hashes:
                        duplicados.append((ruta_archivo, hashes[video_hash]))
                    else:
                        hashes[video_hash] = ruta_archivo

    return duplicados

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    videos_duplicados = buscar_videos_duplicados(ruta_carpeta)

    if videos_duplicados:
        print("Se encontraron videos duplicados:")
        for video1, video2 in videos_duplicados:
            print(f"  - {video1} es una copia de {video2}")
            os.remove(video1)  # Elimina el video duplicado
            print(f"    - Se ha borrado: {video1}")
    else:
        print("No se encontraron videos duplicados en la carpeta.")
