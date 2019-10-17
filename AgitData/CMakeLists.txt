project(AgitData)

file(GLOB_RECURSE SCRIPT_FILES
    ./*.agit
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SCRIPT_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${CMAKE_BINARY_DIR}/install/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".agit" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/Script/castledata.txt"
    COMMENT "Merging agits to ${CMAKE_BINARY_DIR}/install/Script/castledata.txt"
    VERBATIM
)
