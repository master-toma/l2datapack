project(NpcData NONE)

file(GLOB_RECURSE NPC_FILES
    ./*.npc
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${NPC_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${CMAKE_BINARY_DIR}/install/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".npc" --join_lines --id_column 3 --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/Script/npcdata.txt"
    COMMENT "Merging npcs to ${CMAKE_BINARY_DIR}/install/Script/npcdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${CMAKE_BINARY_DIR}/install/Script/npcdata.txt" "${CMAKE_BINARY_DIR}/install/CachedScript/npcdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -n ./ -o ./
    COMMENT "Compiling npcdata.txt to ${CMAKE_BINARY_DIR}/install/Script/npc*_pch.txt"
    VERBATIM
)
