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

def rename_files_in_directory(directory):
    if not os.path.isdir(directory):
        print(f"The provided path '{directory}' is not a valid directory.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    base_name = os.path.basename(directory)
    print(f"Processing directory: {directory}")
    print(f"Files found: {files}")  # Mensaje de depuración para ver los archivos encontrados
    for file_name in files:
        file_extension = os.path.splitext(file_name)[1]
        new_name = get_new_filename(directory, base_name, file_extension)
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)
        # print(f"Renaming {old_path} to {new_path}")  # Mensaje de depuración para cada renombramiento
        os.rename(old_path, new_path)

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing images: ")
    rename_files_in_directory(folder_path)
    print("Renaming completed.")
