project(AreaData)

file(GLOB_RECURSE MULTISELL_FILES
    ./*.area
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${MULTISELL_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${CMAKE_BINARY_DIR}/install/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".area" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/Script/areadata.txt"
    COMMENT "Merging areas to ${CMAKE_BINARY_DIR}/install/Script/areadata.txt"
    VERBATIM
)
