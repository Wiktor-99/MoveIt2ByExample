cmake_minimum_required(VERSION 3.5)

project(gazebo_model_spawner)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
endif()

find_package(std_msgs REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(${PROJECT_NAME} src/gazebo_model_spawner.cpp)
ament_target_dependencies(${PROJECT_NAME}
  rclcpp
  std_msgs
)

install(TARGETS
  ${PROJECT_NAME}
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
