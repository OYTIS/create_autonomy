cmake_minimum_required(VERSION 3.5)
project(ca_description)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch meshes urdf
	DESTINATION share/${PROJECT_NAME}
  PATTERN ".svn" EXCLUDE
)

ament_package()
