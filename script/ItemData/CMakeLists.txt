project(ItemData NONE)

file(GLOB_RECURSE SCRIPT_FILES
    ./*.item
)

file(GLOB_RECURSE SET_SCRIPT_FILES
    ./sets/*.set
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SCRIPT_FILES} ${SET_SCRIPT_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".item" --join_lines --id_column 3 --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/itemdata.txt"
    COMMENT "Merging item data to ${DATA_PACK_OUTPUT_DIR}/Script/itemdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".set" --join_lines --append 1 --id_column 2 --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/itemdata.txt"
    COMMENT "Merging sets to ${DATA_PACK_OUTPUT_DIR}/Script/itemdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${DATA_PACK_OUTPUT_DIR}/Script/itemdata.txt" "${DATA_PACK_OUTPUT_DIR}/CachedScript/itemdata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -i ./ -o ./
    COMMENT "Compiling itemdata.txt to ${DATA_PACK_OUTPUT_DIR}/Script/item*_pch.txt"
    VERBATIM
)
