import os

def generate_folder_structure(dir_path, prefix=''):
    # Inicializa la variable para almacenar la estructura
    structure = ''
    # Lista los elementos dentro del directorio
    items = os.listdir(dir_path)

    # Recorre los elementos del directorio
    for index, item in enumerate(items):
        item_path = os.path.join(dir_path, item)
        is_last_item = index == len(items) - 1  # Verifica si es el último elemento
        connector = '└── ' if is_last_item else '├── '  # Define el conector gráfico

        # Añade el nombre del archivo o carpeta a la estructura
        structure += f'{prefix}{connector}{item}\n'

        # Si es un directorio, llama a la función de forma recursiva
        if os.path.isdir(item_path):
            new_prefix = prefix + ('    ' if is_last_item else '│   ')
            structure += generate_folder_structure(item_path, new_prefix)

    return structure

def write_structure_to_file(dir_path, output_file):
    # Genera la estructura de carpetas
    structure = generate_folder_structure(dir_path)
    # Escribe la estructura en un archivo
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(structure)
    print(f'Estructura de carpetas guardada en: {output_file}')

# Ruta del proyecto
project_root = os.path.join(os.getcwd(), 'src')
# Ruta para guardar el archivo de salida
output_file_path = os.path.join('temp', 'folder_structure.txt')

# Crea la carpeta 'temp' si no existe
os.makedirs('temp', exist_ok=True)

# Escribe la estructura de carpetas en el archivo de salida
write_structure_to_file(project_root, output_file_path)
