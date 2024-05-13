make_minimum_required(VERSION 3.5)

project(gazebo_model_spawner)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -Wpedantic")
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

find_package(gz_math_vendor REQUIRED)
find_package(gz-math REQUIRED)

find_package(gz_transport_vendor REQUIRED)
find_package(gz-transport REQUIRED)

find_package(gz_msgs_vendor REQUIRED)
find_package(gz-msgs REQUIRED)

find_package(gz_sim_vendor REQUIRED)
find_package(gz-sim REQUIRED)

gz_find_package(gflags
    REQUIRED
    PKGCONFIG gflags)
find_package(std_msgs REQUIRED)

add_executable(${PROJECT_NAME} src/gazebo_model_spawner.cpp)
ament_target_dependencies(${PROJECT_NAME}
  rclcpp
  std_msgs
)

target_link_libraries(${PROJECT_NAME}
  gflags
  gz-math::core
  gz-msgs::core
  gz-transport::core
)

install(TARGETS
  create
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
