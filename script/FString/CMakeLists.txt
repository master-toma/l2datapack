project(FString NONE)

set(PCH_FILES
    ${CMAKE_CURRENT_LIST_DIR}/fstring.txt
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${PCH_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/fstring.txt" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/fstring.txt"
    COMMENT "Encoding fstring.txt to ${DATA_PACK_OUTPUT_DIR}/Script/fstring.txt"
    VERBATIM
)
