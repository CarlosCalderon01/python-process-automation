import os
import time

def get_counter(path_file):
    try:
        with open(path_file, 'r') as file:
            return int(file.read())
    except FileNotFoundError:
        return 1
    except ValueError:
        return 1
    
def save_counter(path_file, counter):
    with open(path_file, 'w') as file:
        file.write(str(counter))

def change_name_alls_files(original_folder, path_save, num_counter):
    func_counter = num_counter
    for main_path, sub_folders, files in os.walk(original_folder):
        for name_file in files:
            name, format = os.path.splitext(name_file)
            old_path = os.path.join(main_path, name_file)
            new_name = f"{format[1:]}_{func_counter}{format}"
            new_path = os.path.join(main_path, new_name)

            os.rename(old_path, new_path)
            print(f"Re_Name: {name_file} a {new_name}")

            func_counter += 1
            time.sleep(0.2)

    save_counter(path_save, func_counter)


# Obtener la ubicación del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construir la ruta relativa
path_counter = os.path.join(script_dir, "z-counter.txt")

if __name__ == "__main__":
    folders_original_path = input("Enter the path of the original folder: ")
    change_name_alls_files(folders_original_path, path_counter, get_counter(path_counter))

"""

- Explicacion Codigo:

    - Cambiador de nombres con contador por fuera

"""
