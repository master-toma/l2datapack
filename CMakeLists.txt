project(L2DataPack NONE)

cmake_minimum_required(VERSION 3.5)

set(SCRIPT_L2CC_PATH ${CMAKE_BINARY_DIR}/install/L2CC/l2cc.exe CACHE FILEPATH "Path to l2cc.exe")
set(SCRIPT_MERGE_SCRIPT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/merge_files.py CACHE FILEPATH "Path to merge_files.py")
set(DATA_PACK_OUTPUT_DIR ${CMAKE_BINARY_DIR}/install/ CACHE PATH "Output directory for compiled scripts")

add_subdirectory(script)
