project(SkillData NONE)

file(GLOB_RECURSE SKILL_FILES
    ./*.skill
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SKILL_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E make_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".skill" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${DATA_PACK_OUTPUT_DIR}/Script/skilldata.txt"
    COMMENT "Merging skills to ${DATA_PACK_OUTPUT_DIR}/Script/skilldata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    COMMAND ${CMAKE_COMMAND} -E copy "${DATA_PACK_OUTPUT_DIR}/Script/skilldata.txt" "${DATA_PACK_OUTPUT_DIR}/CachedScript/skilldata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -s ./ -o ./
    COMMENT "Compiling skilldata.txt to ${DATA_PACK_OUTPUT_DIR}/Script/skill*_pch.txt"
    VERBATIM
)
