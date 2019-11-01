project(WatchList NONE)

add_custom_target(${PROJECT_NAME}
    SOURCES watch_list.txt
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/watch_list.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/watch_list.txt"
    COMMENT "Encoding watch_list to ${CMAKE_BINARY_DIR}/install/Script/watch_list.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${CMAKE_BINARY_DIR}/install/Script/watch_list.txt" "${CMAKE_BINARY_DIR}/install/CachedScript/watch_list.txt"
    VERBATIM
)
