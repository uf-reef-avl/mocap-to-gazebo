#!/usr/bin/env python
import rospy
from optitrack_to_gazebo import optitrack_to_gazebo

rospy.init_node("optitrack_to_gazebo_node",anonymous=False)
optitrack_to_gazebo = optitrack_to_gazebo()

loop_rate = rospy.Rate(5)

while not rospy.is_shutdown():
    optitrack_to_gazebo.spin()
    loop_rate.sleep()
