project(L2DataPack)
cmake_minimum_required(VERSION 3.5)

set(SCRIPT_L2CC_PATH ${CMAKE_BINARY_DIR}/install/L2CC/l2cc.exe CACHE FILEPATH "Path to l2cc.exe")
set(SCRIPT_MERGE_SCRIPT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/merge_files.py CACHE FILEPATH "Path to merge_files.py")

add_subdirectory(AgitData)
add_subdirectory(AIScripts)
add_subdirectory(AreaData)
add_subdirectory(BuilderAliases)
add_subdirectory(CategoryData)
add_subdirectory(DoorData)
add_subdirectory(FString)
add_subdirectory(Manual)
add_subdirectory(MultiSell)
add_subdirectory(NpcData)
add_subdirectory(NpcPos)
add_subdirectory(PcParameters)
add_subdirectory(PetData)
add_subdirectory(Recipes)
add_subdirectory(Settings)
add_subdirectory(SkillAcquire)
add_subdirectory(SkillData)
add_subdirectory(VehicleData)

add_custom_target(${PROJECT_NAME}-1-basics
    DEPENDS AgitData AreaData BuilderAliases CategoryData DoorData FString Manual MultiSell PcParameters PetData Settings VehicleData
)

add_custom_target(${PROJECT_NAME}-2-complex
    DEPENDS NpcData NpcPos Recipes SkillAcquire SkillData
)

add_custom_target(${PROJECT_NAME}-3-ai
    DEPENDS AIScripts
)

add_custom_target(${PROJECT_NAME}-0-all
    DEPENDS ${PROJECT_NAME}-1-basics ${PROJECT_NAME}-2-complex ${PROJECT_NAME}-3-ai
)
