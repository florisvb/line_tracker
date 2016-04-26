#!/usr/bin/env python

# ROS Imports
import rospy
from std_msgs.msg import Int32MultiArray

# Standard Imports
from picamera.array import PiRGBArray
import time
import picamera
import os, sys
import cv2
import numpy as np
from gopigo import *

if __name__ == '__main__':

        # Set camera parameters
        camera = picamera.PiCamera()
        camera.resolution = (640,480)
        camera.framerate = 24
        time.sleep(2)
        rawCapture = PiRGBArray(camera, size=(640,480))
        time.sleep(1)
        led_off(0)
        led_off(1)

	# Insert Publisher Node Setup Here
        pub_m1 = rospy.Publisher('/gopigo/motor1', Int32MultiArray, queue_size=10)
        pub_m2 = rospy.Publisher('/gopigo/motor2', Int32MultiArray, queue_size=10)
	rospy.init_node('line_track', anonymous=True)
       	status_left = Int32MultiArray()
       	status_right = Int32MultiArray()


for frame in camera.capture_continuous(rawCapture,format="bgr", use_video_port=True):
	image = frame.array
	
	#cv2.imshow('original image',image)
	#cv2.waitKey(1)

	# add image processing to identify lines
	# use determined lines and associated parameters to determine the direction of motion correction
	# use proportional or PI gain to make decisions about the amount of correction required
	# differentially actuate left, right motors using the calculated correction

	key = cv2.waitKey(1) & 0XFF
	rawCapture.truncate(0)
