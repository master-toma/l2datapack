project(FString)

set(PCH_FILES
    ${CMAKE_CURRENT_LIST_DIR}/fstring.txt
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${PCH_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/fstring.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/fstring.txt"
    COMMENT "Encoding fstring.txt to ${CMAKE_BINARY_DIR}/install/Script/fstring.txt"
    VERBATIM
)
