cmake_minimum_required(VERSION 3.5)
project(ca_msgs)

find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rosidl_default_runtime REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  msg/Bumper.msg
  msg/ChargingState.msg
  msg/DefineSong.msg
  msg/Mode.msg
  msg/PlaySong.msg

  DEPENDENCIES std_msgs
)

ament_package()
