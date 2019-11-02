project(AIScripts NONE)

file(GLOB_RECURSE SCRIPT_SOURCES
    ./*.ais
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SCRIPT_SOURCES}
)

set(SCRIPT_AI_MERGER_PATH ${CMAKE_BINARY_DIR}/install/NASC/Merger.exe CACHE FILEPATH "Path to program, which will merge separated *.ais files " )
set(SCRIPT_AI_COMPILER_PATH ${CMAKE_BINARY_DIR}/install/NASC/NASC.exe CACHE FILEPATH "Path to AIS compiler")

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${SCRIPT_AI_MERGER_PATH} ${CMAKE_CURRENT_LIST_DIR} "${DATA_PACK_OUTPUT_DIR}/Script/ai.txt"
    COMMENT "Merging *.ais files: ${SCRIPT_AI_MERGER_PATH} ${CMAKE_CURRENT_LIST_DIR} ${DATA_PACK_OUTPUT_DIR}/Script/ai.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_AI_COMPILER_PATH} "${DATA_PACK_OUTPUT_DIR}/Script/ai.txt"
    COMMENT "Compiling ai.txt: ${SCRIPT_AI_COMPILER_PATH} ${DATA_PACK_OUTPUT_DIR}/Script/ai.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E remove_directory "${DATA_PACK_OUTPUT_DIR}/Script/log/"
    VERBATIM
)
