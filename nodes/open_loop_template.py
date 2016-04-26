#!/usr/bin/env python

# ROS Imports
import rospy
from std_msgs.msg import Int32MultiArray

# Standard Imports
import time
import os, sys
import numpy as np
from gopigo import *

if __name__ == '__main__':

        led_off(0)
        led_off(1)

	# Publisher node setup
        pub_m1 = rospy.Publisher('/gopigo/motor1', Int32MultiArray, queue_size=10)
        pub_m2 = rospy.Publisher('/gopigo/motor2', Int32MultiArray, queue_size=10)
	rospy.init_node('open_loop_template', anonymous=True)
       	status_left = Int32MultiArray()
       	status_right = Int32MultiArray()

       	# Insert a rough motion plan algorithm for the given open-loop
       	# specifications. Vary the speeds on each motor along with specific
       	# time delays to achieve the necessary behavior
