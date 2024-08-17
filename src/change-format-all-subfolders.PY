import os
from PIL import Image

def change_format_and_delete(folder_path):
    for main_path, sub_folders, files in os.walk(folder_path):
        for name_file in files:
            # Verificar si el archivo es una imagen y no es JPEG ni GIF
            if name_file.lower().endswith(('.jpg', '.png', '.bmp', '.webp')) and not name_file.lower().endswith(('.jpeg', '.gif')):
                path_file = os.path.join(main_path, name_file)

                try:
                    # Intentar abrir la imagen
                    image = Image.open(path_file)

                    # Obtener el nombre del archivo sin extensión
                    name_without_extension, _ = os.path.splitext(name_file)

                    # Convertir la imagen al modo RGB
                    image = image.convert('RGB')

                    # Crear nueva ruta con extensión JPEG
                    new_path_file = os.path.join(main_path, f"{name_without_extension}.jpeg")

                    # Guardar la imagen en formato JPEG
                    image.save(new_path_file, "JPEG")
                    
                    # Mostrar mensaje indicando el cambio de formato
                    print(f"Convertido: {name_file} a {name_without_extension}.jpeg")

                    # Borrar el archivo original
                    os.remove(path_file)
                    print(f"Borrado: {name_file}")

                except (IOError, OSError) as e:
                    # Imprimir un mensaje si no se puede abrir la imagen
                    print(f"Error opening image {name_file}: {e}")

if __name__ == "__main__":
    original_folder_path = input("Enter the path of the original folder: ")
    change_format_and_delete(original_folder_path)

"""

    - Cambia el formato de todas las imagenes en carpetas y sub carpetas
    - ignora las imagenes que ya tienen el formato deseado, en este caso (jpeg)

"""
