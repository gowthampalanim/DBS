# Capla DBS - Build Guide
### For execution with Claude Code after June 17

---

## Overview

Capla DBS is a fully branded Deep Brain Stimulation planning application
built on 3D Slicer using the SlicerCustomAppTemplate framework.

The output is a standalone `CaplaDBs.exe` — no "3D Slicer" branding visible anywhere.

---

## Prerequisites (one-time setup)

Run `scripts/install_prerequisites.bat` as Administrator, then restart.

Requires:
- Windows 10/11 64-bit
- ~50GB free disk space (Slicer source + build)
- 16GB RAM minimum (32GB recommended)
- Git, CMake 3.16+, Visual Studio 2022 Build Tools
- Python 3.x (for cookiecutter)

---

## Folder Structure

```
CaplaDBs/
├── CMakeLists.txt              # Main build config
├── README.md                   # This file
├── branding/
│   ├── CaplaDBs.ico            # Windows icon (replace with real Capla logo)
│   ├── CaplaDBs.icns           # macOS icon
│   └── CaplaDBs_logo.png       # App logo shown in UI
├── modules/
│   ├── Home/                   # Custom Capla DBS landing screen
│   │   ├── CMakeLists.txt
│   │   ├── Home.py
│   │   └── Resources/Icons/Home.png
│   ├── anatomicalLandmarks/    # Copy from trajectoryGuideModules
│   ├── dataImport/
│   ├── dataView/
│   ├── frameDetect/
│   ├── helpers/
│   ├── intraopPlanning/
│   ├── postopLocalization/
│   ├── postopProgramming/
│   ├── preopPlanning/
│   ├── registration/
│   └── settingsPanel/
└── scripts/
    ├── install_prerequisites.bat
    └── build.bat
```

---

## Build Steps

### Step 1 — Prepare branding assets
Replace placeholder files in `branding/` with real Capla logo:
- `CaplaDBs_logo.png` — 300x300px PNG, transparent background
- `CaplaDBs.ico` — convert PNG using https://convertio.co/png-ico/

### Step 2 — Copy trajectoryGuide modules
Copy all module folders from:
`S:\Softwares\Slicer\trajectoryGuide-portable\modules\`
Into:
`S:\Softwares\DBS\CaplaDBS-project\modules\`

### Step 3 — Run build
```
scripts\build.bat
```
This will:
1. Clone Slicer source (~5GB)
2. Build Slicer (~4-8 hours)
3. Build Capla DBS on top (~30 min)

### Step 4 — Output
Executable at: `S:\Softwares\Slicer\CaplaDBs-build\Release\CaplaDBs.exe`

---

## Customization

### Window title / app name
Edit `CMakeLists.txt`:
```cmake
set(SlicerApp_APPLICATION_DISPLAY_NAME "Capla DBS")
```

### Startup disclaimer
```cmake
set(SlicerApp_DISCLAIMER_AT_STARTUP "For clinical investigation use only.")
```

### Home screen
Edit `modules/Home/Home.py` — full Qt UI, customize colors, buttons, layout freely.

### Qt stylesheet (global UI skin)
Add a `CaplaDBs.qss` file and reference it in CMakeLists to restyle the entire UI.

---

## Notes for Claude Code

When running with Claude Code:
1. Start with `install_prerequisites.bat`
2. Restart machine
3. Run `build.bat` — monitor for errors
4. Common errors:
   - "Cannot find compiler" → VS Build Tools not installed correctly
   - "Qt not found" → add `-DQt5_DIR` to cmake command
   - Out of memory → close other apps, increase page file
