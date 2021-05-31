#!/usr/bin/env python

# import roslaunch
import rospy
# import rosgraph
# import actionlib
import time
import sys
# import socket
# import subprocess
# import psutil
import math
from math import radians
# from geometry_msgs.msg import Twist
import os

import json
from std_msgs.msg import String
import numpy as np 


def scaledDistanceRatio(x, y, beta):
    # to do
    cos_phi = x / np.sqrt(x**2 + y**2)
    # cos_phi = abs(cos_phi)
    ratio = (1 - beta * cos_phi) / (1 - beta)
    return ratio


def scaledRatio(x, y, beta):
    # to do
    cos_phi = x / np.sqrt(x**2 + y**2)
    # cos_phi = abs(cos_phi)
    ratio = (1 - beta * cos_phi) 
    return ratio

def scaledDistanceRatio2(x, y, beta):
    # to do
    k=x/y
    # cos_phi = abs(cos_phi)
    ratio =np.sqrt((1+k**2)/(k**2+(1-beta)**2 ))
    return ratio


def main(argv):
    # x=-0.7
    # y=0.6
    # b=0.75
    # print scaledDistanceRatio(x,y,b), scaledDistanceRatio2(x,y,b), scaledRatio(x,y,b)

    # a=[0]
    # if a:
    #     print '11'
    # else:
    #     print '22'

    rospy.init_node('test_node')
    taskSwitchPub = rospy.Publisher('task_request', String, queue_size=10)

    # TASK_CANCEL  , TASK_CREATE, TASK_FORCE_FINISH"
    task_msg = String()
    task_msg.data = """{
    "CEID":"1",
    "LINE_ID":"F1-A",
    "AGV_ID": "",
	"DISPATCH_ID": "16",
    "FROM": "2F_21",
    "DESTINATION": "2F_13",
    "TODO": "TASK_CREATE",
    "SLOT_INFO": "9"
}"""

    print json.loads(task_msg.data)
    print task_msg.data
    time.sleep(3)
    taskSwitchPub.publish(task_msg)


if __name__ == '__main__':
    main(sys.argv)
