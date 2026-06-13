cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(CaplaDBs)

# -----------------------------------------------------------------------
# Capla DBS - Custom 3D Slicer Application
# Built on SlicerCustomAppTemplate
# -----------------------------------------------------------------------

# --- Application Identity ---
set(SlicerApp_APPLICATION_NAME "CaplaDBs")
set(SlicerApp_APPLICATION_DISPLAY_NAME "Capla DBS")
set(SlicerApp_APPLICATION_VERSION_MAJOR 1)
set(SlicerApp_APPLICATION_VERSION_MINOR 0)
set(SlicerApp_APPLICATION_VERSION_PATCH 0)
set(SlicerApp_DISCLAIMER_AT_STARTUP "For clinical investigation use only. Not for diagnostic use.")

# --- Organization ---
set(SlicerApp_ORGANIZATION_NAME "Capla Medical")
set(SlicerApp_ORGANIZATION_DOMAIN "capla.in")

# --- Branding ---
set(SlicerApp_APPLICATION_LOGO "${CMAKE_CURRENT_SOURCE_DIR}/branding/CaplaDBs_logo.png")
set(SlicerApp_APPLE_ICON "${CMAKE_CURRENT_SOURCE_DIR}/branding/CaplaDBs.icns")
set(SlicerApp_WIN_ICON "${CMAKE_CURRENT_SOURCE_DIR}/branding/CaplaDBs.ico")
set(SlicerApp_DESCRIPTION_SUMMARY "Capla DBS - Deep Brain Stimulation Planning System")
set(SlicerApp_DESCRIPTION_FILE "${CMAKE_CURRENT_SOURCE_DIR}/README.md")

# --- Slicer Source (set this to where you cloned Slicer) ---
set(Slicer_DIR "" CACHE PATH "Path to Slicer build directory")

# -----------------------------------------------------------------------
# Features - keep only what DBS planning needs
# -----------------------------------------------------------------------
set(Slicer_BUILD_DICOM_SUPPORT                ON  CACHE BOOL "")
set(Slicer_BUILD_DIFFUSION_SUPPORT            OFF CACHE BOOL "")
set(Slicer_BUILD_EXTENSIONMANAGER_SUPPORT     OFF CACHE BOOL "")
set(Slicer_BUILD_APPLICATIONUPDATE_SUPPORT    OFF CACHE BOOL "")
set(Slicer_BUILD_MULTIVOLUME_SUPPORT          OFF CACHE BOOL "")
set(Slicer_BUILD_PARAMETERSERIALIZER_SUPPORT  OFF CACHE BOOL "")
set(Slicer_USE_PYTHONQT                       ON  CACHE BOOL "")
set(Slicer_USE_QtTesting                      OFF CACHE BOOL "")
set(Slicer_USE_SimpleITK                      ON  CACHE BOOL "")
set(Slicer_BUILD_BRAINSTOOLS                  OFF CACHE BOOL "")
set(Slicer_BUILD_DataStore                    OFF CACHE BOOL "")
set(Slicer_BUILD_CompareVolumes               OFF CACHE BOOL "")
set(Slicer_BUILD_LandmarkRegistration         OFF CACHE BOOL "")
set(Slicer_BUILD_SurfaceToolbox               OFF CACHE BOOL "")

# -----------------------------------------------------------------------
# Modules - include trajectoryGuide modules
# -----------------------------------------------------------------------
set(Slicer_EXTENSION_SOURCE_DIRS
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/anatomicalLandmarks
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/dataImport
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/dataView
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/frameDetect
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/intraopPlanning
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/postopLocalization
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/postopProgramming
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/preopPlanning
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/registration
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/settingsPanel
  ${CMAKE_CURRENT_SOURCE_DIR}/modules/helpers
)

# -----------------------------------------------------------------------
# Find Slicer and build
# -----------------------------------------------------------------------
find_package(Slicer COMPONENTS ConfigurePrerequisites REQUIRED)
project(CaplaDBs)
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

# Add Home module (custom landing screen)
add_subdirectory(modules/Home)

include(${Slicer_EXTENSION_CPACK})
