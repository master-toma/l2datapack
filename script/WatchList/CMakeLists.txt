project(WatchList NONE)

add_custom_target(${PROJECT_NAME}
    SOURCES watch_list.txt
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/watch_list.txt" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/watch_list.txt"
    COMMENT "Encoding watch_list to ${DATA_PACK_OUTPUT_DIR}/Script/watch_list.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${DATA_PACK_OUTPUT_DIR}/Script/watch_list.txt" "${DATA_PACK_OUTPUT_DIR}/CachedScript/watch_list.txt"
    VERBATIM
)
