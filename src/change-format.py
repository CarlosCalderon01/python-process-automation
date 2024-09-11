import os
from PIL import Image

def change_format_and_delete(folder_path):
    # Recorre la carpeta y subcarpetas
    for main_path, sub_folders, files in os.walk(folder_path):
        for name_file in files:
            # Verifica si el archivo es una imagen y no es JPEG ni GIF
            if name_file.lower().endswith(('.jpg', '.png', '.bmp', '.webp')) and not name_file.lower().endswith(('.jpeg', '.gif')):
                path_file = os.path.join(main_path, name_file)

                try:
                    # Intenta abrir la imagen
                    image = Image.open(path_file)

                    # Obtiene el nombre del archivo sin extensión
                    name_without_extension, _ = os.path.splitext(name_file)

                    # Convierte la imagen al modo RGB
                    image = image.convert('RGB')

                    # Crea nueva ruta con extensión JPEG
                    new_path_file = os.path.join(main_path, f"{name_without_extension}.jpeg")

                    # Guarda la imagen en formato JPEG
                    image.save(new_path_file, "JPEG")
                    
                    # Muestra un mensaje indicando la conversión
                    print(f"Convertido: {name_file} a {name_without_extension}.jpeg")

                    # Borra el archivo original
                    os.remove(path_file)
                    print(f"Borrado: {name_file}")

                except (IOError, OSError) as e:
                    # Muestra un mensaje si no se puede abrir la imagen
                    print(f"Error opening image {name_file}: {e}")

if __name__ == "__main__":
    # Solicita al usuario la ruta de la carpeta original
    original_folder_path = input("Enter the path of the original folder: ")
    change_format_and_delete(original_folder_path)
