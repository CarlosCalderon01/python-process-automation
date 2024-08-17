@echo off
:menu
cls
echo ================================
echo Seleccione el comando que desea ejecutar:
echo ================================
echo 0. Salir
echo 1. Eliminar imágenes repetidas en todas las subcarpetas
echo 2. Cambiar formato de imágenes en todas las subcarpetas (GIF, JPEG)
echo 3. Renombrar todos los archivos según sus carpetas
echo 4. Renombrar todos los archivos usando contador
echo 5. Mover archivos repetidos a una carpeta
echo 6. [Placeholder para un futuro comando]
echo ================================
set /p opcion="Ingrese el número del comando: "

if "%opcion%"=="0" (
    echo Saliendo...
    exit /b
) else if "%opcion%"=="1" (
    python src\delete-repeat-all-subfolders.py
) else if "%opcion%"=="2" (
    python src\change-format-all-subfolders.py
) else if "%opcion%"=="3" (
    python src\change-name-all-subfolders.py
) else if "%opcion%"=="4" (
    python src\change-name-all-subfolders-using-counter.py
) else if "%opcion%"=="5" (
    python src\move-repeat-in-folder.py
) else if "%opcion%"=="6" (
    echo Opción 6 seleccionada.
) else (
    echo Comando no reconocido, por favor intente nuevamente.
    pause
    goto menu
)
