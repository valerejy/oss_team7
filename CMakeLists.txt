cmake_minimum_required(VERSION 3.0.2)
project(team7)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy std_msgs
)

catkin_install_python(PROGRAMS
   node/straight.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

 install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_DESTINATION}
 )
