project(Scripts NONE)

cmake_minimum_required(VERSION 3.5)

add_subdirectory(AgitData)
add_subdirectory(AIScripts)
add_subdirectory(AreaData)
add_subdirectory(BuilderAliases)
add_subdirectory(CategoryData)
add_subdirectory(DoorData)
add_subdirectory(FString)
add_subdirectory(ItemData)
add_subdirectory(Manual)
add_subdirectory(MultiSell)
add_subdirectory(NpcData)
add_subdirectory(NpcPos)
add_subdirectory(PcParameters)
add_subdirectory(PetData)
add_subdirectory(Quests)
add_subdirectory(Recipes)
add_subdirectory(Setting)
add_subdirectory(SkillAcquire)
add_subdirectory(SkillData)
add_subdirectory(VehicleData)
add_subdirectory(WatchList)

# Target dependencies
add_dependencies(AIScripts CategoryData FString Manual NpcData SkillData ItemData Quests)

add_custom_target(${PROJECT_NAME}-build-basics
    DEPENDS AgitData AreaData BuilderAliases CategoryData DoorData FString Manual MultiSell PcParameters PetData Recipes Setting VehicleData Quests WatchList
)

add_custom_target(${PROJECT_NAME}-build-complex
    DEPENDS NpcPos NpcData SkillAcquire SkillData ItemData
)

add_custom_target(${PROJECT_NAME}-build-ai
    DEPENDS AIScripts
)

add_custom_target(${PROJECT_NAME}-build-all
    DEPENDS ${PROJECT_NAME}-build-basics ${PROJECT_NAME}-build-complex ${PROJECT_NAME}-build-ai
)

add_custom_target(${PROJECT_NAME}-clean-all ALL
    COMMAND echo "Removing ${DATA_PACK_OUTPUT_DIR}/Script/ and ${DATA_PACK_OUTPUT_DIR}/CachedScript/"
)

add_custom_command(
    TARGET  ${PROJECT_NAME}-clean-all
    COMMAND ${CMAKE_COMMAND} -E remove_directory "${DATA_PACK_OUTPUT_DIR}/Script/"
    VERBATIM
)

add_custom_command(
    TARGET  ${PROJECT_NAME}-clean-all
    COMMAND ${CMAKE_COMMAND} -E remove_directory "${DATA_PACK_OUTPUT_DIR}/CachedScript/"
    VERBATIM
)
