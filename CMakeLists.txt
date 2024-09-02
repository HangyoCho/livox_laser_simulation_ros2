cmake_minimum_required(VERSION 3.5)
project(livox_laser_simulation_ros2)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(PCL REQUIRED)
find_package(pcl_msgs REQUIRED)
find_package(pcl_conversions REQUIRED)
find_package(rosidl_typesupport_cpp REQUIRED)
find_package(livox_ros_driver2 REQUIRED) 

include_directories(
  include
  ${PCL_INCLUDE_DIRS}
  ${GAZEBO_INCLUDE_DIRS}
  ${CMAKE_BINARY_DIR}/rosidl_generator_cpp
)

link_directories(${GAZEBO_LIBRARY_DIRS})

# Create a shared library with a unique name
add_library(livox_laser_simulation_plugin SHARED src/livox_points_plugin.cpp src/livox_ode_multiray_shape.cpp)
ament_target_dependencies(livox_laser_simulation_plugin 
  rclcpp 
  tf2_ros 
  sensor_msgs 
  std_msgs 
  gazebo_ros 
  PCL 
  pcl_msgs 
  pcl_conversions 
  rosidl_typesupport_cpp 
  livox_ros_driver2   
)

target_link_libraries(livox_laser_simulation_plugin 
  RayPlugin 
  libprotobuf.so 
  ${gazebo_ros_LIBRARIES} 
  ${rosidl_typesupport_cpp_LIBRARIES}
)

# Install the library
install(TARGETS livox_laser_simulation_plugin
  EXPORT export_livox_laser_simulation_plugin
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

# Install include directories
install(DIRECTORY include/
  DESTINATION include/
)

# Install models, worlds, and rviz configuration files
install(DIRECTORY models/
  DESTINATION share/${PROJECT_NAME}/models/
)

install(DIRECTORY worlds/
  DESTINATION share/${PROJECT_NAME}/worlds/
)

install(DIRECTORY rviz/
  DESTINATION share/${PROJECT_NAME}/rviz/
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch/
)

ament_export_include_directories(include)
ament_export_libraries(livox_laser_simulation_plugin)
ament_package()
