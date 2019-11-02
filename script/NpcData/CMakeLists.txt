project(NpcData NONE)

file(GLOB_RECURSE NPC_FILES
    ./*.npc
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${NPC_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".npc" --join_lines --id_column 3 --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/npcdata.txt"
    COMMENT "Merging npcs to ${DATA_PACK_OUTPUT_DIR}/Script/npcdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${DATA_PACK_OUTPUT_DIR}/Script/npcdata.txt" "${DATA_PACK_OUTPUT_DIR}/CachedScript/npcdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -n ./ -o ./
    COMMENT "Compiling npcdata.txt to ${DATA_PACK_OUTPUT_DIR}/Script/npc*_pch.txt"
    VERBATIM
)
