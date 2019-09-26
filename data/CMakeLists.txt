project(script_data)

set(PCH_FILES
    ${CMAKE_CURRENT_LIST_DIR}/categorydata.txt
    ${CMAKE_CURRENT_LIST_DIR}/fstring.txt
    ${CMAKE_CURRENT_LIST_DIR}/npcpos.txt
)

add_custom_target(${PROJECT_NAME}
    SOURCES ${PCH_FILES}
)

#install(FILES ${PCH_FILES} DESTINATION "${CMAKE_BINARY_DIR}/install/Script/")

#add_custom_command(
#    TARGET  ${PROJECT_NAME}
#    COMMAND ${CMAKE_COMMAND} -E copy_if_different ${PCH_FILES} "${CMAKE_BINARY_DIR}/install/Script"
#    COMMENT "Copying script files to ${CMAKE_BINARY_DIR}/install/Script"
#    VERBATIM
#)

set(SCRIPT_MERGE_SCRIPT_PATH ${LINEAGE_2_ROOT_DIR}/tools/merge_files.py CACHE FILEPATH "Path to merge_files.py")

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/fstring.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/fstring.txt"
    COMMENT "Encoding fstring.txt to ${CMAKE_BINARY_DIR}/install/Script/fstring.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/categorydata.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/categorydata.txt"
    COMMENT "Encoding categorydata.txt to ${CMAKE_BINARY_DIR}/install/Script/categorydata.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_MERGE_SCRIPT_PATH} --single_file "${CMAKE_CURRENT_LIST_DIR}/npcpos.txt" --out_name "${CMAKE_BINARY_DIR}/install/Script/npcpos.txt"
    COMMENT "Encoding npcpos.txt to ${CMAKE_BINARY_DIR}/install/Script/npcpos.txt"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${CMAKE_BINARY_DIR}/install/Script"
    COMMAND ${SCRIPT_L2CC_PATH} -c ./ -o ./
    COMMENT "Compiling categorydata.txt"
    VERBATIM
)



