import os

def get_new_filename(directory, base_name, extension):
    counter = 1
    new_name = f"{base_name}_{counter}{extension}"
    new_path = os.path.join(directory, new_name)
    while os.path.exists(new_path):
        counter += 1
        new_name = f"IMG_{counter}{extension}"
        new_path = os.path.join(directory, new_name)
    return new_name

def rename_images(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
            print(f"Processing directory: {dir_path}")
            for file_name in dir_files:
                file_extension = os.path.splitext(file_name)[1]
                new_name = get_new_filename(dir_path, dir_name, file_extension)
                old_path = os.path.join(dir_path, file_name)
                new_path = os.path.join(dir_path, new_name)
                print(f"Renaming {old_path} to {new_path}")
                os.rename(old_path, new_path)

if __name__ == "__main__":
    folder_path = input("Enter the path of the folder containing images: ")
    if os.path.isdir(folder_path):
        rename_images(folder_path)
        print("Renaming completed.")
    else:
        print("The provided path is not a valid directory.")
