import os
import time
import logging
from PIL import Image

def change_format_and_delete(folder_path, time_delay=0):
    for main_path, sub_folders, files in os.walk(folder_path):
        for name_file in files:
            if name_file.lower().endswith(('.jpg', '.png', '.bmp', '.webp')) and not name_file.lower().endswith(('.jpeg', '.gif')):
                path_file = os.path.join(main_path, name_file)

                try:
                    image = Image.open(path_file)
                    name_without_extensión, _ = os.path.splitext(name_file)
                    image = image.convert('RGB')
                    new_path_file = os.path.join(main_path, f"{name_without_extensión}.jpeg")
                    image.save(new_path_file, "JPEG")
                    os.remove(path_file)
                except Exception as e:
                    logging.error(f"Error opening image {name_file}: {e}")

                time.sleep(time_delay)

if __name__ == "__main__":
    logging.basicConfig(filename='conversion_errors.log', level=logging.ERROR)
    original_folder_path = input("Enter the path of the original folder: ")
    if not os.path.isdir(original_folder_path):
        print("La ruta proporcionada no es válida.")
    else:
        print("Iniciando la conversión de imágenes...")
        change_format_and_delete(original_folder_path)
        print("Conversión completada.")
