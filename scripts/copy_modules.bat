@echo off
title Capla DBS - Copy Modules

SET SRC=S:\Softwares\Slicer\trajectoryGuide-portable\modules
SET DST=S:\Softwares\DBS\CaplaDBS-project\modules

echo ================================================
echo   Copying trajectoryGuide modules into CaplaDBS
echo ================================================
echo.

IF NOT EXIST "%SRC%" (
    echo [ERROR] Source modules not found at: %SRC%
    pause & exit /b 1
)

echo Copying modules...

for %%M in (anatomicalLandmarks dataImport dataView frameDetect helpers intraopPlanning postopLocalization postopProgramming preopPlanning registration settingsPanel resources) do (
    IF EXIST "%SRC%\%%M" (
        xcopy /E /I /Y /Q "%SRC%\%%M" "%DST%\%%M"
        echo [OK] %%M
    ) ELSE (
        echo [SKIP] %%M - not found in source
    )
)

echo.
echo ================================================
echo   Modules copied successfully!
echo   Next: run scripts\install_prerequisites.bat
echo ================================================
pause
