#!/usr/bin/env python

import rospy
import time
import tf
import random
import numpy as np
import matplotlib.pyplot as plt
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import PoseWithCovarianceStamped


class ScanRecord(object):
    def __init__(self):
        self._scan_list = []
        self._angle_min = 0
        self._angle_max = 0
        self._angle_increment = 0
        self._monitor = False
        self._monitor_scan = []

        rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped,
                         self.amcl_cb, queue_size=10)
        rospy.Subscriber('scan', LaserScan,
                         self.scan_cb, queue_size=10)

    def scan_cb(self, scanMsg):
        if self._angle_max == 0:
            self._angle_min = scanMsg.angle_min
            self._angle_max = scanMsg.angle_max
            self._angle_increment = scanMsg.angle_increment
            self._rad_vector = np.linspace(scanMsg.angle_min,
                                           scanMsg.angle_max, len(scanMsg.ranges), endpoint=False)

        self._scan_list.append(scanMsg.ranges)
        if len(self._scan_list) > 15:
            self._scan_list.pop(0)

    def amcl_cb(self, amclMsg):
        uncertainty = amclMsg.pose.covariance[0] + \
            amclMsg.pose.covariance[7] + amclMsg.pose.covariance[-1]
        if uncertainty > 1:
            print 'acml monitored!!'
            print amclMsg.pose.covariance 
            self._monitor_scan = self._scan_list
            self._monitor = True


def main():
    rospy.init_node('scan_monitor')
    ts = time.time()
    Sc = ScanRecord()
    color = ['-k', '-r', '-c', '-m', '-g', '-y', '-b',
             'gold', 'lime', 'grey', 'tan', 'coral', 'olive', 'peru',
             'linen', 'beige','purple','pink','olive','-k', '-r', '-c', '-m', '-g', '-y', '-b',
             'gold', 'lime', 'grey', 'tan', 'coral', 'olive', 'peru',
             'linen', 'beige','purple','pink','olive','-k', '-r', '-c', '-m', '-g', '-y', '-b',
             'gold', 'lime', 'grey', 'tan', 'coral', 'olive', 'peru',
             'linen', 'beige','purple','pink','olive','-k', '-r', '-c', '-m', '-g', '-y', '-b',
             'gold', 'lime', 'grey', 'tan', 'coral', 'olive', 'peru',
             'linen', 'beige','purple','pink','olive']
    idx = 1

    while True:
        if Sc._monitor:
            co = 0
            for scan_msg in Sc._monitor_scan:
                ranges_vector = np.asarray(scan_msg)
                lx_vector = ranges_vector * np.cos(Sc._rad_vector)
                ly_vector = ranges_vector * np.sin(Sc._rad_vector)
                plt.plot(lx_vector, ly_vector, color[co], alpha=0.6)
                # plt.legend()
                co += 1
            Sc._monitor = False
            plt_name = str(idx)+'.png'
            idx += 1
            plt.savefig(plt_name)
            print plt_name, ' saved'
            # plt.pause(0.2)
            plt.close()

        time.sleep(0.1)

    try:
        rospy.spin()
    except:
        pass


if __name__ == '__main__':
    main()
