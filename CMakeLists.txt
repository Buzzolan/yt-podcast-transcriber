cmake_minimum_required(VERSION 3.19)
project(GUI-yt-transcriber LANGUAGES CXX)

find_package(Qt6 6.5 REQUIRED COMPONENTS Core Widgets)

qt_standard_project_setup()

qt_add_executable(GUI-yt-transcriber
    WIN32 MACOSX_BUNDLE
    main.cpp
    mainwindow.cpp
    mainwindow.h
    mainwindow.ui
)

target_link_libraries(GUI-yt-transcriber
    PRIVATE
        Qt::Core
        Qt::Widgets
)

include(GNUInstallDirs)

install(TARGETS GUI-yt-transcriber
    BUNDLE  DESTINATION .
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

qt_generate_deploy_app_script(
    TARGET GUI-yt-transcriber
    OUTPUT_SCRIPT deploy_script
    NO_UNSUPPORTED_PLATFORM_ERROR
)
install(SCRIPT ${deploy_script})

# ------------------------------------------------------------
# Post-build: copy required Qt DLLs to executable folder
# ------------------------------------------------------------

if(WIN32)
    set(QT_BIN_DIR "C:/Qt/6.9.3/msvc2022_64/bin") # path to your Qt DLLs

    set(QT_MODULES Core Gui Widgets)

    foreach(MODULE ${QT_MODULES})
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
            "${QT_BIN_DIR}/Qt6${MODULE}d.dll"  # source: Qt installation folder
            "$<TARGET_FILE_DIR:${PROJECT_NAME}>"  # destination: build folder
        )
    endforeach()

    # Copy platforms plugin folder
    add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
        "${QT_BIN_DIR}/../plugins/platforms"
        "$<TARGET_FILE_DIR:${PROJECT_NAME}>/platforms"
    )
endif()

