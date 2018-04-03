#!/bin/bash
#Script to start the ros simulations 
xterm -geometry -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros inputs" &
xterm -geometry -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros light_node" & 
xterm -geometry -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros sensor_node" & 
xterm -geometry -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros base_node " &
xterm -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros mv_turtle.py"  &



#xterm -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros sensor_node.py"  &
sleep 1
xterm -geometry 80x10+3+3 -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros GUI_ROS.py" & 
sleep 1
xterm -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros GUI_SENSORS.py" & 
sleep 1
xterm -geometry 70x18+460+455 -bg white -fg black  -hold -e ". ~/catkin_ws/devel/setup.bash && roscd svg_ros/src/data/ && rosrun svg_ros motion_planner_ROS " &

#xterm -hold -e ". ~/catkin_ws/devel/setup.bash && 
#export TURTLEBOT_BASE=create && 
#export TURTLEBOT_STACKS=circles &&
#sudo chmod +777 /dev/ttyUSB0 && 
#export TURTLEBOT_SERIAL_PORT=/dev/ttyUSB0 &&
#roslaunch turtlebot_bringup minimal.launch --screen" 
