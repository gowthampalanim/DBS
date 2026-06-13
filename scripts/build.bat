@echo off
title Capla DBS - Build Script
echo ================================================
echo   Capla DBS - Full Build Script
echo   This will take 4-8 hours on first run
echo ================================================
echo.

SET BUILD_DIR=S:\Softwares\DBS\CaplaDBs-build
SET SOURCE_DIR=S:\Softwares\DBS\CaplaDBS-project
SET SLICER_BUILD=S:\Softwares\DBS\Slicer-build

:: -------------------------------------------------------
:: STEP 1 - Check prerequisites
:: -------------------------------------------------------
echo [STEP 1] Checking prerequisites...

where cmake >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] CMake not found. Install from https://cmake.org/download/
    pause & exit /b 1
)

where git >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git not found. Install from https://git-scm.com/
    pause & exit /b 1
)

where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python not found. Install from https://python.org
    pause & exit /b 1
)

echo [OK] Prerequisites found.
echo.

:: -------------------------------------------------------
:: STEP 2 - Install cookiecutter if needed
:: -------------------------------------------------------
echo [STEP 2] Installing cookiecutter...
pip install cookiecutter jinja2-github --quiet
echo [OK] cookiecutter ready.
echo.

:: -------------------------------------------------------
:: STEP 3 - Clone Slicer source if not present
:: -------------------------------------------------------
echo [STEP 3] Checking Slicer source...
IF NOT EXIST "%SLICER_BUILD%\..\Slicer-source" (
    echo Cloning Slicer source (~5GB, this will take a while)...
    git clone https://github.com/Slicer/Slicer.git S:\Softwares\DBS\Slicer-source
) ELSE (
    echo [OK] Slicer source already present.
)
echo.

:: -------------------------------------------------------
:: STEP 4 - Create build directories
:: -------------------------------------------------------
echo [STEP 4] Creating build directories...
mkdir "%SLICER_BUILD%" 2>nul
mkdir "%BUILD_DIR%" 2>nul
echo [OK] Directories ready.
echo.

:: -------------------------------------------------------
:: STEP 5 - Configure Slicer build
:: -------------------------------------------------------
echo [STEP 5] Configuring Slicer build...
cd /d "%SLICER_BUILD%"
cmake -G "Visual Studio 17 2022" -A x64 ^
  -DSlicer_RELEASE_TYPE:STRING=Stable ^
  -DCMAKE_BUILD_TYPE:STRING=Release ^
  S:\Softwares\DBS\Slicer-source

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Slicer CMake configuration failed.
    echo Try Visual Studio 2019: change "Visual Studio 17 2022" to "Visual Studio 16 2019"
    pause & exit /b 1
)
echo [OK] Slicer configured.
echo.

:: -------------------------------------------------------
:: STEP 6 - Build Slicer (this is the long step)
:: -------------------------------------------------------
echo [STEP 6] Building Slicer... (4-8 hours)
echo You can minimize this window. It will beep when done.
cmake --build . --config Release -- /maxcpucount

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Slicer build failed. Check error above.
    pause & exit /b 1
)
echo [OK] Slicer built successfully.
echo.

:: -------------------------------------------------------
:: STEP 7 - Configure Capla DBS app
:: -------------------------------------------------------
echo [STEP 7] Configuring Capla DBS...
cd /d "%BUILD_DIR%"
cmake -G "Visual Studio 17 2022" -A x64 ^
  -DSlicer_DIR:PATH="%SLICER_BUILD%\Slicer-build" ^
  -DCMAKE_BUILD_TYPE:STRING=Release ^
  "%SOURCE_DIR%"

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Capla DBS CMake configuration failed.
    pause & exit /b 1
)
echo [OK] Capla DBS configured.
echo.

:: -------------------------------------------------------
:: STEP 8 - Build Capla DBS
:: -------------------------------------------------------
echo [STEP 8] Building Capla DBS...
cmake --build . --config Release -- /maxcpucount

IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Capla DBS build failed.
    pause & exit /b 1
)

echo.
echo ================================================
echo   BUILD COMPLETE!
echo   Capla DBS executable at:
echo   %BUILD_DIR%\Release\CaplaDBs.exe
echo ================================================
pause
