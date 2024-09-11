import os

def get_new_filename(directory, base_name, extension):
    # Inicializa el contador para crear nombres únicos
    counter = 1
    new_name = f"{base_name}_{counter}{extension}"
    new_path = os.path.join(directory, new_name)
    
    # Incrementa el contador hasta encontrar un nombre único
    while os.path.exists(new_path):
        counter += 1
        new_name = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(directory, new_name)
    
    return new_name

def rename_files_in_directory(directory, debug=False):
    # Verifica si el directorio proporcionado es válido
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a valid directory.")
        return

    # Lista todos los elementos en el directorio
    all_items = os.listdir(directory)
    
    if debug:
        print(f"Processing directory: {directory}")
        print(f"All items found: {all_items}")
    
    # Recorre los subdirectorios y archivos del directorio
    for root, dirs, files in os.walk(directory):
        subdirectory_name = os.path.basename(root)  # Nombre del subdirectorio actual
        
        # Procesa cada archivo en el subdirectorio
        for file_name in files:
            file_extension = os.path.splitext(file_name)[1]  # Obtiene la extensión del archivo
            new_name = get_new_filename(root, subdirectory_name, file_extension)  # Genera el nuevo nombre
            old_path = os.path.join(root, file_name)  # Ruta del archivo original
            new_path = os.path.join(root, new_name)  # Ruta con el nuevo nombre
            
            if debug:
                print(f"Renaming {old_path} to {new_path}")
            
            # Intenta renombrar el archivo y captura errores si ocurren
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(f"Error renaming {old_path} to {new_path}: {e}")

if __name__ == "__main__":
    # Solicita al usuario la ruta de la carpeta
    folder_path = input("Enter the path of the folder containing files: ")
    rename_files_in_directory(folder_path, debug=True)  # Ejecuta la función de renombrado
    print("Renaming completed.")
