project(PetData NONE)

file(GLOB_RECURSE SCRIPT_FILES
    ./*.pet
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
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".pet" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/petdata.txt"
    COMMENT "Merging pets to ${DATA_PACK_OUTPUT_DIR}/Script/petdata.txt"
    VERBATIM
)
