project(CategoryData NONE)

file(GLOB_RECURSE SCRIPT_FILES
    ./*.category
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
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".category" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/categorydata.txt"
    COMMENT "Merging categories to ${DATA_PACK_OUTPUT_DIR}/Script/categorydata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -c ./ -o ./
    COMMENT "Compiling categorydata.txt"
    VERBATIM
)

