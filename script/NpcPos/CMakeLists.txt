project(NpcPos NONE)

file(GLOB_RECURSE SOURCES
    ./*.pos
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SOURCES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".pos" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/npcpos.txt"
    COMMENT "Encoding npcpos.txt to ${DATA_PACK_OUTPUT_DIR}/Script/npcpos.txt"
    VERBATIM
)


