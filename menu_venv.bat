@echo off
setlocal EnableDelayedExpansion

:menu
cls
echo ================================
echo Python Virtual Environment Manager
echo ================================
echo 0. Salir
echo 1. Crear un entorno virtual (myenv)
echo 2. Activar el entorno virtual
echo 3. Instalar dependencias desde requirements.txt
echo 4. Listar dependencias actuales
echo 5. Guardar dependencias actuales en requirements.txt
echo 6. Desactivar el entorno virtual
echo 7. Eliminar el entorno virtual
echo 8. Ejecutar Create_Executables.py
echo 9. Ejecutar Draw_Folder_Layout.py
echo ================================
set /p opcion="Ingrese el número del comando: "

set "command="

if "%opcion%"=="0" (
    echo Saliendo...
    exit /b
) else if "%opcion%"=="1" (
    set "command=python -m venv myenv"
) else if "%opcion%"=="2" (
    set "command=call myenv\Scripts\activate"
) else if "%opcion%"=="3" (
    set "command=pip install -r requirements.txt"
) else if "%opcion%"=="4" (
    set "command=pip list"
) else if "%opcion%"=="5" (
    set "command=pip freeze > requirements.txt"
) else if "%opcion%"=="6" (
    set "command=deactivate"
) else if "%opcion%"=="7" (
    set "command=rd /s /q myenv"
) else if "%opcion%"=="8" (
    set "command=python Create_Executables.py"
) else if "%opcion%"=="9" (
    set "command=python Draw_Folder_Layout.py"
) else (
    echo Comando no reconocido, por favor intente nuevamente.
    pause
    goto menu
)

if defined command (
    %command%
    if "%opcion%"=="2" (
        echo Entorno virtual activado. 
        echo Recuerda ejecutar "deactivate" para desactivarlo cuando termines.
    )
    pause
)

goto menu
