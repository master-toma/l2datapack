project(Quests NONE)

set(SCRIPT_FILES
    quest_pch.txt quest_pch2.txt
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SCRIPT_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/quest_pch.txt" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/quest_pch.txt"
    COMMENT "Encoding quest files to ${DATA_PACK_OUTPUT_DIR}/Script/quest_pch.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/quest_pch2.txt" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/quest_pch2.txt"
    COMMENT "Encoding quest files to ${DATA_PACK_OUTPUT_DIR}/Script/quest_pch2.txt"
    VERBATIM
)
