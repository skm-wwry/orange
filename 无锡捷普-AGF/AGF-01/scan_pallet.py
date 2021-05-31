#!/usr/bin/env python

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from std_msgs.msg import String
from obstacle_detector.msg import *
import time
'''
Created on 2020-10-21
@author: lei.zeng@tu-dortmund.de
'''


class ScanPallet(EventState):
    '''
    judge existance of pallet
    -- range        tuple   (xmin xmax ymin ymax)

    <= occupied              pallet exists
    <= free             free space

    '''
    def __init__(self, ranges=[-1, 1, 1, 2]):
        super(ScanPallet, self).__init__(outcomes=['occupied', 'free'])
        self._update_pub = ProxyPublisher({'flexbe/behavior_updating': String})
        self._obstacles_sub = ProxySubscriberCached(
            {'raw_obstacles': Obstacles})
        self._range = ranges
        self._res = 'free'

    def on_enter(self, userdata):
        update_msg = String()
        update_msg.data = self.name
        self._update_pub.publish('flexbe/behavior_updating', update_msg)

        time.sleep(3.0)
        t_s = time.time()
        while time.time() - t_s <= 1:
            if self._obstacles_sub.has_msg('raw_obstacles'):
                msg = self._obstacles_sub.get_last_msg('raw_obstacles')
                c = filter(
                    lambda mc: self._range[0] < mc.center.x < self._range[1]
                    and self._range[2] < mc.center.y < self._range[3],
                    list(msg.circles))
                l = filter(
                    lambda ml: self._range[0] < ml.first_point.x < self._range[
                        1] and self._range[2] < ml.first_point.y < self._range[
                            3] and self._range[0] < ml.last_point.x < self.
                    _range[1] and self._range[
                        2] < ml.last_point.y < self._range[3],
                    list(msg.segments))

                if list(c + l) != []:
                    self._res = 'occupied'
            time.sleep(0.1)

    def execute(self, userdata):
        return self._res
