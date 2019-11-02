project(Recipes NONE)

file(GLOB_RECURSE RECIPES_FILES
    ./*.recipe
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${RECIPES_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".recipe" --join_lines --id_column 3 --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/recipe.txt"
    COMMENT "Merging recipes to ${DATA_PACK_OUTPUT_DIR}/Script/recipe.txt"
    VERBATIM
)
