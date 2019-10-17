project(L2DataPack)
cmake_minimum_required(VERSION 3.5)

set(LINEAGE_2_ROOT_DIR ${CMAKE_CURRENT_SOURCE_DIR}/..)

set(SCRIPT_L2CC_PATH ${CMAKE_BINARY_DIR}/install/L2CC/l2cc.exe CACHE FILEPATH "Path to l2cc.exe")
set(SCRIPT_MERGE_SCRIPT_PATH ${LINEAGE_2_ROOT_DIR}/tools/merge_files.py CACHE FILEPATH "Path to merge_files.py")

add_subdirectory(AIScripts)
add_subdirectory(AreaData)
add_subdirectory(data)
add_subdirectory(MultiSell)
add_subdirectory(NpcData)
add_subdirectory(PcParameters)
add_subdirectory(PetData)
add_subdirectory(Recipes)
add_subdirectory(Settings)
add_subdirectory(SkillData)
