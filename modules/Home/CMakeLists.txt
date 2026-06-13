cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(Home)

set(MODULE_NAME Home)

find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

set(MODULE_PYTHON_SCRIPTS
  Home.py
)

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/Home.png
)

slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
)
