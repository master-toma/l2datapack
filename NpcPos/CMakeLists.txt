project(NpcPos)

file(GLOB_RECURSE SOURCES
    ./*.pos
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SOURCES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".pos" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/Script/npcpos.txt"
    COMMENT "Encoding npcpos.txt to ${CMAKE_BINARY_DIR}/install/Script/npcpos.txt"
    VERBATIM
)


