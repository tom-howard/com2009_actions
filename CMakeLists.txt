cmake_minimum_required(VERSION 3.0.2)
project(com2009_actions)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  actionlib
  geometry_msgs
  nav_msgs
  rospy
  sensor_msgs
  std_msgs
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate actions in the 'action' folder
add_action_files(
  FILES
  CameraSweep.action
  Search.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  geometry_msgs nav_msgs sensor_msgs std_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
 CATKIN_DEPENDS rospy
)

###########
## Build ##
###########
include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
