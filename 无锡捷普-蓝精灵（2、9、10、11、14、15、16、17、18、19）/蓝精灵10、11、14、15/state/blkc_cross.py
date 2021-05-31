#!/usr/bin/env python

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from std_msgs.msg import String
import rospy
'''
Created on 2021-5-13
@author: lei.zeng@tu-dortmund.de
'''


class BlkcCross(EventState):
    '''
    blkc cross
    '''

    def __init__(self):
        super(BlkcCross, self).__init__(outcomes=['1_5', '2_3_4_6'],  input_keys=['to_site'])
        self._update_pub = ProxyPublisher({'flexbe/behavior_updating': String})

    def on_enter(self, userdata):
        update_msg = String()
        update_msg.data = self.name
        self._update_pub.publish('flexbe/behavior_updating', update_msg)

    def execute(self, userdata):
        site_name = userdata.to_site
        if site_name[4:6] in ['02', '03', '04', '06']:
            return '2_3_4_6'
        elif site_name[4:6] in ['01', '05']:
            return '1_5'
        else:
            Logger.logwarn('to site name is invalid for BlckCross')
