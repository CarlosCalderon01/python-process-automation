@echo off
:menu
cls
echo ================================
echo Seleccione el comando que desea ejecutar:
echo ================================
echo 0. Salir
echo 1. Delete repeat in all sub folders - Picture
echo 2. Delete repeat in all sub folders - Video
echo 3. Change format in all sub folders - Picture
echo 4. Change format in all sub folders - Video
echo 5. Detect repeat in all sub folders - Picture (percentage)
echo 6. Detect (folders, Sub folders, Files).
echo 7. Detect (folders, Sub folders).
echo 8. Change format in all sub folders - Picture (JPG)
echo 9. Charge All files (.py) in (.exe)

echo ================================
set /p opcion="Ingrese el número del comando:"

if "%opcion%"=="0" (
    echo Saliendo...
    exit /b
) else if "%opcion%"=="1" (
    python src\apps\Delete_Repeat_Picture.py
) else if "%opcion%"=="2" (
    python src\apps\Delete_Repeat_Video.py
) else if "%opcion%"=="3" (
    python src\apps\Change_Format_Picture.py
) else if "%opcion%"=="4" (
    python src\apps\Change_Format_Video.py
) else if "%opcion%"=="5" (
    python src\apps\Detect_Repeat_Images_By_Percentage.py
) else if "%opcion%"=="6" (
    python src\apps\Draw_Folder_Layout_Files.py
) else if "%opcion%"=="7" (
    python src\apps\Draw_Folder_Layout.py
) else if "%opcion%"=="8" (
    python src\apps\Change_Format_Picture_JPG.py
) else if "%opcion%"=="9" (
    python Create_Executables.py
) else (
    echo Comando no reconocido, por favor intente nuevamente.
    pause
    goto menu
)
