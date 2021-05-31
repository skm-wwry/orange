#!/usr/bin/env python

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from std_msgs.msg import Header, String
import rospy

'''
Created on 07.01.2019
@author: lei.zeng@tu-dortmund.de
'''


class PileOff(EventState):
    '''
    task_switch: charging pile off

    -- seq	         int       seq
    -- frame_id      string    frame_id

    <= done              publishing done

    '''

    def __init__(self):
        '''
        Constructor
        '''
        super(PileOff, self).__init__(outcomes=['done'])
        self._update_pub = ProxyPublisher({'flexbe/behavior_updating': String})
        self._topic = 'task_switch'
        self._pub = ProxyPublisher({self._topic: Header})

    def execute(self, userdata):
        return 'done'

    def on_enter(self, userdata):
        update_msg = String()
        update_msg.data = self.name
        self._update_pub.publish('flexbe/behavior_updating', update_msg)

        msg = Header()
        msg.seq = 0
        msg.frame_id = 'charging_pile'
        msg.stamp = rospy.Time.now()
        self._pub.publish(self._topic, msg)
