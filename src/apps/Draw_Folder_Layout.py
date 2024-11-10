import os

def generate_folder_structure(dir_path, prefix=''):
    structure = ''
    try:
        items = os.listdir(dir_path)
        directories = [item for item in items if os.path.isdir(os.path.join(dir_path, item))]

        for index, item in enumerate(directories):
            item_path = os.path.join(dir_path, item)
            is_last_item = index == len(directories) - 1
            connector = '└── ' if is_last_item else '├── '

            structure += f"{prefix}{connector}{item}\n"
            new_prefix = prefix + ('    ' if is_last_item else '│   ')
            structure += generate_folder_structure(item_path, new_prefix)

    except Exception as error:
        print(f"Error al generar la estructura: {error}")
    return structure

def write_structure_to_file(dir_path, output_file):
    try:
        structure = generate_folder_structure(dir_path)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(structure)
        print(f"Estructura de carpetas guardada en: {output_file}")
    except Exception as error:
        print(f"Error al escribir la estructura en archivo: {error}")

# Función principal para iniciar el programa
if __name__ == "__main__":
    # Solicita al usuario la ruta de la carpeta original
    original_folder_path = input("Ingresa la ruta de la carpeta original: ")

    # Especifica el archivo de salida
    output_file_path = os.path.join('temp', 'folder_structure.txt')

    # Crea la carpeta de salida si no existe
    os.makedirs('temp', exist_ok=True)

    # Genera y guarda la estructura de carpetas en un archivo
    write_structure_to_file(original_folder_path, output_file_path)
