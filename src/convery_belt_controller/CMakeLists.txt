cmake_minimum_required(VERSION 3.8)
project(convery_belt_controller)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(convery_belt_controller src/convery_belt_controller.cpp)
ament_target_dependencies(convery_belt_controller rclcpp std_msgs)

install(TARGETS
  convery_belt_controller
  DESTINATION lib/${PROJECT_NAME})

ament_package()
