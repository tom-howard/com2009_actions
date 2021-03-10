#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

class TB3Scan(object):
    def scan_cb(self, scan_data):
        # From the front of the robot, obtain a 20 degree 
        # arc of scan data either side of the x-axis 
        left = scan_data.ranges[0:20]
        right = scan_data.ranges[-21:]
        # combine the left and right data arrays, flip them so that 
        # the data is arranged from left (-20 degrees) to right (+20 degrees)
        # then convert to a numpy array
        scan_arc = np.array(left[::-1] + right[::-1])

        # Create another numpy array which repreents the angles 
        # (in degrees) associated with each of the datapoints in 
        # the "scan_arc" array above:
        angles = np.arange(-20, 21)

        # Obtain the minimum distance measurement within the "scan_arc" array,
        # determine the associated angle and broadcast this across the class 
        self.min_distance = scan_arc.min()
        self.object_angle = angles[np.argmin(scan_arc)]
    
    def __init__(self):
        self.subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_cb)
