import os
from moviepy.editor import VideoFileClip

def convert_videos_to_mp4(folder_path):
    # Verifica si la ruta existe
    if not os.path.exists(folder_path):
        print(f"La ruta {folder_path} no existe.")
        return

    # Recorre la carpeta y subcarpetas
    for main_path, sub_folders, files in os.walk(folder_path):
        for name_file in files:
            # Verifica si el archivo es un video con extensiones comunes
            if name_file.lower().endswith(('.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm')) and not name_file.lower().endswith('.mp4'):
                path_file = os.path.join(main_path, name_file)

                try:
                    # Intenta abrir el video
                    video = VideoFileClip(path_file)

                    # Obtiene el nombre del archivo sin extensión
                    name_without_extension, _ = os.path.splitext(name_file)

                    # Crea nueva ruta con extensión MP4
                    new_path_file = os.path.join(main_path, f"{name_without_extension}.mp4")

                    # Convierte y guarda el video en formato MP4
                    video.write_videofile(new_path_file, codec="libx264")
                    
                    # Cierra el video para liberar recursos
                    video.close()

                    # Muestra un mensaje indicando la conversión
                    print(f"Convertido: {name_file} a {new_path_file}")

                    # Borra el archivo original
                    os.remove(path_file)
                    print(f"Borrado: {name_file}")

                except PermissionError:
                    # Muestra un mensaje si hay problemas de permisos y continúa
                    print(f"Permiso denegado para el archivo {name_file}. Se omite y continúa.")
                except Exception as e:
                    # Muestra un mensaje si hay otro tipo de error en la conversión
                    print(f"Error al convertir el video {name_file}: {e}")

if __name__ == "__main__":
    # Solicita al usuario la ruta de la carpeta original
    original_folder_path = input("Ingresa la ruta de la carpeta original: ")
    convert_videos_to_mp4(original_folder_path)
