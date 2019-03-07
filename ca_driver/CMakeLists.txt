cmake_minimum_required(VERSION 3.5)
project(ca_driver)

find_package(libcreate REQUIRED)

find_package(ca_msgs REQUIRED)
find_package(diagnostic_msgs REQUIRED)
find_package(diagnostic_updater REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_cpplint REQUIRED)
find_package(ament_cmake_cppcheck REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)

ament_cpplint()
ament_cppcheck()

include_directories(
  include
  ${libcreate_INCLUDE_DIRS}
  ${ca_msgs_INCLUDE_DIRS}
  ${nav_msgs_INCLUDE_DIRS}
  ${std_msgs_INCLUDE_DIRS}
  ${geometry_msgs_INCLUDE_DIRS}
  ${sensor_msgs_INCLUDE_DIRS}
  ${diagnostic_updater_INCLUDE_DIRS}
  ${rclcpp_INCLUDE_DIRS}
  ${tf2_INCLUDE_DIRS}
  ${tf2_ros_INCLUDE_DIRS}
  ${tf2_geometry_msgs_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME} src/create_driver.cpp)

target_link_libraries(${PROJECT_NAME}
  ${libcreate_LIBRARIES}
  ${std_msgs_LIBRARIES}
  ${nav_msgs_LIBRARIES}
  ${sensor_msgs_LIBRARIES}
  ${geometry_msgs_LIBRARIES}
  ${ca_msgs_LIBRARIES}
  ${diagnostic_updater_LIBRARIES}
  ${rclcpp_LIBRARIES}
  ${tf2_LIBRARIES}
  ${tf2_ros_LIBRARIES}
  ${tf2_geometry_msgs_LIBRARIES}
)

install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(DIRECTORY include
  DESTINATION include
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE
)

install(DIRECTORY launch
	DESTINATION "share/${PROJECT_NAME}/"
)

install(DIRECTORY config
	DESTINATION "share/${PROJECT_NAME}/"
)

install(TARGETS ${PROJECT_NAME}
	DESTINATION lib/${PROJECT_NAME}
)

ament_package()
