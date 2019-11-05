project(Html NONE)

cmake_minimum_required(VERSION 3.5)

file(GLOB_RECURSE HTML_FILES
    ./*.htm
)

set(SCRIPT_ENCODE_HTMLS_SCRIPT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/encode_htmls.py CACHE FILEPATH "Path to encode_htmls.py")

add_custom_target(${PROJECT_NAME}
    SOURCES ${HTML_FILES}
)

add_custom_command(
    TARGET  ${PROJECT_NAME}
    WORKING_DIRECTORY "${DATA_PACK_OUTPUT_DIR}/"
    COMMAND ${SCRIPT_ENCODE_HTMLS_SCRIPT_PATH} -e ".htm" --root_dir "${CMAKE_CURRENT_LIST_DIR}/en" --out_dir "${DATA_PACK_OUTPUT_DIR}/html"
    COMMENT "Encoding htm files to ${DATA_PACK_OUTPUT_DIR}/html"
    VERBATIM
)

