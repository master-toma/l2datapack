project(AreaData NONE)

file(GLOB_RECURSE SCRIPT_FILES
    ./*.area
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
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".area" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/areadata.txt"
    COMMENT "Merging areas to ${DATA_PACK_OUTPUT_DIR}/Script/areadata.txt"
    VERBATIM
)
