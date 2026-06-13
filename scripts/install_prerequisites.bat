@echo off
title Capla DBS - Install Prerequisites
echo ================================================
echo   Capla DBS - Prerequisites Installer
echo   Run this ONCE before building
echo ================================================
echo.

:: Check winget
where winget >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] winget not found. Update Windows or install App Installer from Microsoft Store.
    pause & exit /b 1
)

echo [1/4] Installing Git...
winget install --id Git.Git -e --silent
echo.

echo [2/4] Installing CMake...
winget install --id Kitware.CMake -e --silent
echo.

echo [3/4] Installing Visual Studio 2022 Build Tools...
echo This is ~4GB and will take several minutes...
winget install --id Microsoft.VisualStudio.2022.BuildTools -e --silent ^
  --override "--wait --quiet --add Microsoft.VisualStudio.Workload.VCTools ^
  --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 ^
  --add Microsoft.VisualStudio.Component.Windows10SDK.19041"
echo.

echo [4/4] Installing Python packages...
pip install cookiecutter jinja2-github
echo.

echo ================================================
echo   Prerequisites installed!
echo   RESTART your machine before running build.bat
echo ================================================
pause
