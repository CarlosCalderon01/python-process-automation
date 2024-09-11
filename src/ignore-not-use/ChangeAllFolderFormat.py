import os
import time 
from PIL import Image

def change_format_and_delete(folder_path):
    for main_path, sub_folders, files in os.walk(folder_path):
        for name_file in files:
            # Verificar si el archivo es una imagen y no es JPEG
            if name_file.lower().endswith(('.jpg', '.png', '.bmp', '.webp')) and not name_file.lower().endswith(('.jpeg', '.gif')):
                path_file = os.path.join(main_path, name_file)

                try:
                    # Intentar abrir la imagen
                    image = Image.open(path_file)

                    # Obtener el nombre del archivo sin extensión
                    name_without_extensión, _ = os.path.splitext(name_file)

                    # Convertir la imagen al modo RGB
                    image = image.convert('RGB')

                    # Crear nueva ruta con extensión JPEG
                    new_path_file = os.path.join(main_path, f"{name_without_extensión}.jpeg")

                    # Guardar la imagen en formato JPEG
                    image.save(new_path_file, "JPEG")
                    
                    # Mostrar mensaje indicando el cambio de formato
                    #print(f"Convertido: {name_file} a {name_without_extensión}.jpeg")

                    # Borrar el archivo original
                    os.remove(path_file)
                    #print(f"Borrado: {name_file}")

                except Exception as e:
                    # Imprimir un mensaje si no se puede abrir la imagen
                    print(f"Error opening image {name_file}: {e}")

                # Agregar retraso entre iteraciones
                # time.sleep(time_delay)

# Ruta del directorio que contiene las imágenes
# number_time_delay = 1

if __name__ == "__main__":
    original_folder_path = input("Enter the path of the original folder: ")
    change_format_and_delete(original_folder_path)

