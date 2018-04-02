cmake_minimum_required(VERSION 3.9)

function(get_pelican_plugins)
    set(options)
    set(oneValueArgs GIT_TAG)
    set(multiValueArgs)
    cmake_parse_arguments(ARGS "${options}" "${oneValueArgs}" "${multiValueArgs}" ${ARGN} )

    # Set defaults for unprovided arguments
    if(NOT ARG_GIT_TAG)
        set(ARG_GIT_TAG "master")
    endif()


    set(PROJECT_NAME pelican-plugins)

    set(EXTERNAL_PROJ_NAME external_proj_${PROJECT_NAME})
    include(ExternalProject)

    ExternalProject_Add(
        ${EXTERNAL_PROJ_NAME}
        GIT_REPOSITORY https://github.com/getpelican/pelican-plugins
        GIT_TAG ${ARG_GIT_TAG}
        GIT_SHALLOW 1
        SOURCE_DIR ${CMAKE_BINARY_DIR}/${PROJECT_NAME}
        CONFIGURE_COMMAND ""
        BUILD_COMMAND ""
        INSTALL_COMMAND ""
    )
endfunction()

get_pelican_plugins(GIT_TAG ee3792e)
