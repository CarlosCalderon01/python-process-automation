import os
import time

def cambiar_nombres_carpeta(ruta_carpeta):
    for ruta_principal, carpetas, archivos in os.walk(ruta_carpeta):
        contador = 1  # Re start counter in from folder
        for nombre_archivo in archivos:
            nombre, formato = os.path.splitext(nombre_archivo)
            ruta_antiguo = os.path.join(ruta_principal, nombre_archivo)
            #nombre_nuevo = f"{formato[1:]}_{contador}{formato}"
            nombre_nuevo = f"IMG ({contador}){formato}"
            ruta_nuevo = os.path.join(ruta_principal, nombre_nuevo)

            os.rename(ruta_antiguo, ruta_nuevo)
            print(f"Renombrado: {nombre_archivo} a {nombre_nuevo}")

            contador += 1

            # time.sleep(0.2)

if __name__ == "__main__":
    ruta_carpeta = input("Introduce la ruta de la carpeta: ")
    cambiar_nombres_carpeta(ruta_carpeta)

"""
    
    - 
        - Cambiar nombres bajo este formato  "IMG (X)"

"""