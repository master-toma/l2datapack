project(SkillData)

file(GLOB_RECURSE SKILL_FILES
    ./*.skill
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${SKILL_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".skill" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/Script/skilldata.txt"
    COMMENT "Merging skills to ${CMAKE_BINARY_DIR}/install/Script/skilldata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} -e ".skill" --root_dir "${CMAKE_CURRENT_LIST_DIR}" --out_name "${CMAKE_BINARY_DIR}/install/CachedScript/skilldata.txt"
    COMMENT "Merging skills to ${CMAKE_BINARY_DIR}/install/CachedScript/skilldata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -s ./ -o ./
    COMMENT "Compiling skilldata.txt to ${CMAKE_BINARY_DIR}/install/Script/skill*_pch.txt"
    VERBATIM
)
