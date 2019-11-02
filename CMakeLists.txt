project(L2DataPack NONE)

cmake_minimum_required(VERSION 3.5)

set(SCRIPT_L2CC_PATH ${CMAKE_BINARY_DIR}/install/L2CC/l2cc.exe CACHE FILEPATH "Path to l2cc.exe")
set(SCRIPT_MERGE_SCRIPT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/merge_files.py CACHE FILEPATH "Path to merge_files.py")
set(DATA_PACK_OUTPUT_DIR ${CMAKE_BINARY_DIR}/install/ CACHE PATH "Output directory for compiled scripts")

option(USE_HTML "Include html files" OFF)

add_subdirectory(script)

if(USE_HTML)
    message(STATUS "USE_HTML set to ${USE_HTML}. Project generation might take some time")
    add_subdirectory(html)
else()
    message(STATUS "USE_HTML unset. To have it included in project, use -DUSE_HTML=ON during cmake")
endif()
