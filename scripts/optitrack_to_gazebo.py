#!/usr/bin/env python
import os
import rospy
import rospkg

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState



class optitrack_to_gazebo:

    def __init__(self):

        self.rigidbody_name = rospy.get_param("~rigidbody_name")
        self.turtlebot_base_to_optitrack_marker_translation = rospy.get_param("~turtlebot_base_to_optitrack_marker_translation")
        self.state_msg = None
        self.mocap_sub = rospy.Subscriber("pose_stamped", PoseStamped, self.mocap_callback)


    def mocap_callback(self, msg):
        self.state_msg = ModelState()
        self.state_msg.model_name = self.rigidbody_name
        self.state_msg.pose.position.x = msg.pose.position.x -  self.turtlebot_base_to_optitrack_marker_translation[0]
        self.state_msg.pose.position.y = msg.pose.position.y - self.turtlebot_base_to_optitrack_marker_translation[1]
        self.state_msg.pose.position.z = msg.pose.position.z - self.turtlebot_base_to_optitrack_marker_translation[2]
        self.state_msg.pose.orientation.x = msg.pose.orientation.x
        self.state_msg.pose.orientation.y = msg.pose.orientation.y
        self.state_msg.pose.orientation.z = msg.pose.orientation.z
        self.state_msg.pose.orientation.w = msg.pose.orientation.w


    def spin(self):
        if self.state_msg != None:
            rospy.wait_for_service('/gazebo/set_model_state')
            try:
                set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
                resp = set_state(self.state_msg)
            except rospy.ServiceException:
                print("Service call failed /gazebo/set_model_state: for " + str(self.rigidbody_name))


