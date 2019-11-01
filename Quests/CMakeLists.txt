project(Quests)

set(SCRIPT_FILES
    quest_pch.txt quest_pch2.txt
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SCRIPT_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/quest_pch.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/quest_pch.txt"
    COMMENT "Encoding quest files to ${CMAKE_BINARY_DIR}/install/Script/quest_pch.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/quest_pch2.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/quest_pch2.txt"
    COMMENT "Encoding quest files to ${CMAKE_BINARY_DIR}/install/Script/quest_pch2.txt"
    VERBATIM
)
