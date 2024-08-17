import os

def get_new_filename(directory, base_name, extension):
    counter = 1
    new_name = f"{base_name}_{counter}{extension}"
    new_path = os.path.join(directory, new_name)
    while os.path.exists(new_path):
        counter += 1
        new_name = f"{base_name}_{counter}{extension}"
        new_path = os.path.join(directory, new_name)
    return new_name

def rename_files_in_directory(directory, debug=False):
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a valid directory.")
        return

    all_items = os.listdir(directory)
    
    if debug:
        print(f"Processing directory: {directory}")
        print(f"All items found: {all_items}")
    
    for root, dirs, files in os.walk(directory):
        subdirectory_name = os.path.basename(root)
        for file_name in files:
            file_extension = os.path.splitext(file_name)[1]
            new_name = get_new_filename(root, subdirectory_name, file_extension)
            old_path = os.path.join(root, file_name)
            new_path = os.path.join(root, new_name)
            
            if debug:
                print(f"Renaming {old_path} to {new_path}")
            
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                print(f"Error renaming {old_path} to {new_path}: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing files: ")
    rename_files_in_directory(folder_path, debug=True)
    print("Renaming completed.")

"""

    - Explicacion Codigo:

        - Cambia los nombres de todas las carpetas y subc carpetas.
        - Pone nombre de los archivos en base  a us carpeta contenedora.
        - Genera un contador de cero para cada sub carpeta

"""