#!/usr/bin/env python

"""
subscribe to topic: /raw_obstacles (Great appreciation for Mateusz Przybyla's work)
privide tf:         base_link -> charging_pile_current
                    odom -> base_charging_pile

Author: lei.zeng@tu-dortmund.de
"""


import rospy
import time
import math
import tf
import tf2_ros
import operator
import numpy
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from obstacle_detector.msg import Obstacles


class ChargingPileDetect():
    def __init__(self):
        self._namespace = rospy.get_namespace()[1:]
        self._namespace = ''
        self.sub_shelf = rospy.Subscriber("raw_obstacles", Obstacles,
                                          self.detectChargingPileCallback, queue_size=1)
        self.__pile_radius = rospy.get_param(
            "~charging_pile_radius", 0.0625)

        self.view_start = rospy.get_param(
            "~view_start", 1.05)
        self.view_end = rospy.get_param(
            "~view_end", 2.09)
        self.y_drift_error = rospy.get_param(
            "~consider_side_range", 0.5)
        self.xpos_drift_error = rospy.get_param(
            "~consider_front_range", 3.0)
        self.consider_back_range = rospy.get_param(
            "~consider_back_range", 0)
        self.raius_error = rospy.get_param(
            "~raius_error", 0.01)
        self.timeout = 10

        self.__last_px = 0
        self.__last_py = 0
        self.__last_pyaw = 0
        self.__time_start = time.time()

    def pointRadRobot(self, y, x):
        # (-pi, pi]
        return math.atan2(y, x)

    def ChargingPileTFBroadcaster(self, tx, ty, tyaw):
        quat = tf.transformations.quaternion_from_euler(
            0, 0, 0)
        br = tf.TransformBroadcaster()
        br.sendTransform((tx, ty, 0.0),
                         quat,
                         rospy.Time.now(),
                         self._namespace + "charging_pile_current",
                         self._namespace+"base_link")

    def detectChargingPileCallback(self, obstaclesMsg):
        circle_obstacles = list(obstaclesMsg.circles)
        circle_obstacles = filter(lambda c:
                                  self.view_start < self.pointRadRobot(
                                      c.center.x, c.center.y) < self.view_end
                                  and self.consider_back_range < c.center.x < self.xpos_drift_error
                                  and abs(c.center.y) < self.y_drift_error
                                  and abs(c.true_radius - self.__pile_radius) < self.raius_error, circle_obstacles)
        if len(circle_obstacles) == 1:
            cpile = circle_obstacles[0]
            # rospy.loginfo('ChargingPile is localized')
        elif len(circle_obstacles) > 1:
            rospy.logwarn('[ChargingPile] multi targets')
            return
        else:
            rospy.logwarn('[ChargingPile] no target')
            return

        px = cpile.center.x
        py = cpile.center.y
        pyaw = self.pointRadRobot(py, px)
        pdelta = numpy.sqrt((px - self.__last_px)**2 +
                            (py - self.__last_py)**2)
        if pow(self.__last_px, 2) + pow(self.__last_py, 2)+pow(self.__last_pyaw, 2) == 0 or\
                pdelta < 0.1 or \
                (time.time() - self.__time_start) > self.timeout:

            self.ChargingPileTFBroadcaster(px, py, pyaw)
            self.__time_start = time.time()
            self.__last_px = px
            self.__last_py = py
            self.__last_pyaw = pyaw


def medianFilterBasePosition(tf_list):
    tf_x_list = map(lambda f: f.transform.translation.x, tf_list)
    tf_y_list = map(lambda f: f.transform.translation.y, tf_list)

    tf_mx = numpy.median(tf_x_list)
    tf_my = numpy.median(tf_y_list)

    return (tf_mx, tf_my)


def main():
    rospy.init_node('charging_pile_detector')

    median_filter_group = rospy.get_param(
        "~median_filter_group", 20)
    publish_rate = rospy.get_param(
        "~publish_rate", 20)
    sleep_time = 1.0 / publish_rate

    namespace = rospy.get_namespace()[1:]
    namespace = ''

    x_list = []
    y_list = []
    qx_list = []
    qy_list = []
    qz_list = []
    qw_list = []
    tf_list = []

    ChargingPile = ChargingPileDetect()

    buf = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buf)
    while not rospy.is_shutdown():
        time.sleep(sleep_time)
        try:
            tform = buf.lookup_transform(
                namespace+"odom", namespace+"charging_pile_current", rospy.Time(0), timeout=rospy.Duration(0.1))
            tf_list.append(tform)

            if len(tf_list) == 1:
                x_list.append(tform.transform.translation.x)
                y_list.append(tform.transform.translation.y)

                qz_list.append(tform.transform.rotation.z)
                qw_list.append(tform.transform.rotation.w)
            elif len(tf_list) > median_filter_group:
                tf_list.pop(0)
                x_y_median = medianFilterBasePosition(tf_list)
                if len(x_list) > 10:
                    drift_to_mean = numpy.sqrt((x_y_median[0] - x_mean)**2
                                               + (x_y_median[0] - y_mean)**2)
                    if drift_to_mean < 0.08:
                        x_list.append(x_y_median[0])
                        y_list.append(x_y_median[1])
                else:
                    x_list.append(x_y_median[0])
                    y_list.append(x_y_median[1])

        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
            print e

        if len(x_list) >= 10:
            x_mean = numpy.mean(x_list)
            y_mean = numpy.mean(y_list)
            qz_mean = numpy.mean(qz_list)
            qw_mean = numpy.mean(qw_list)
            br = tf.TransformBroadcaster()
            br.sendTransform((x_mean, y_mean, 0),
                             (0, 0, qz_mean, qw_mean),
                             rospy.Time.now(),
                             namespace+"base_shelf",
                             namespace+"odom")

    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down"


if __name__ == '__main__':
    main()
