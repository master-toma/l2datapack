project(L2DataPack NONE)

cmake_minimum_required(VERSION 3.5)

set(SCRIPT_L2CC_PATH ${CMAKE_BINARY_DIR}/install/L2CC/l2cc.exe CACHE FILEPATH "Path to l2cc.exe")
set(SCRIPT_MERGE_SCRIPT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/merge_files.py CACHE FILEPATH "Path to merge_files.py")

add_subdirectory(script)
