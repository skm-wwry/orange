#!/usr/bin/env python

import json
from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher
from flexbe_core.proxy import ProxySubscriberCached
from std_msgs.msg import String
import rospy

class driver(EventState):
    '''
    Publish & Subscribe json topic

    -- topic        	stirng  topic name, [topic]_request / [topic]_response
    -- pub              dictionary or json string, publish params
    -- sub              dictionary or json string, subscribe params
    -- timeoff          double  time to repeat writing
    -- timeout          double  time to reading failed

    <= done             publishing done
    <= failed           publishing failed
    '''

    def __init__(self, topic, pub, sub, timeoff=1.0, timeout=0.0):
        super(driver, self).__init__(outcomes=['done', 'failed'])
        self._update_pub = ProxyPublisher({'flexbe/behavior_updating': String})

        self._pub_topic = topic + "_request"
        self._sub_topic = topic + "_respense"
        self._pub = ProxyPublisher({self._pub_topic: String})
        self._sub = ProxySubscriberCached({self._sub_topic: String})

        if isinstance(pub, dict):
            self._pub_dict = pub
        elif isinstance(pub, str):
            try:
                self._pub_dict = json.loads(pub)
            except Exception as e:
                rospy.logerr('[flexbe_driver] pub json style mismatch')
        if 'ns' not in self._pub_dict:
            self._pub_dict['ns'] = rospy.get_namespace().strip('/')

        if isinstance(sub, dict):
            self._sub_dict = sub
        elif isinstance(sub, str):
            try:
                self._sub_dict = json.loads(sub)
            except Exception as e:
                rospy.logerr('[flexbe_driver] sub json style mismatch')

        self._timeoff = timeoff
        self._timeout = timeout
        self._time_publish = rospy.Time.now()
        self._time_enter = self._time_publish

    def execute(self, userdata):
        if not bool(self._sub_dict):
            return 'done'

        self._time_execute = rospy.Time.now()
        if self._timeout > 0.0:
            if (self._time_execute - self._time_enter) >= rospy.Duration(self._timeout):
                return 'failed'

        if self._timeoff > 0.0:
            if (self._time_execute - self._time_publish) >= rospy.Duration(self._timeoff):
                msg = String()
                msg.data = json.dumps(self._pub_dict)
                self._pub.publish(self._pub_topic, msg)
                self._time_publish = rospy.Time.now()

        if self._sub.has_msg(self._sub_topic):
            msg = self._sub.get_last_msg(self._sub_topic)
            self._sub.remove_last_msg(self._sub_topic)
            try:
                msg_data = json.loads(msg.data)
            except Exception as e:
                rospy.logerr('[flexbe_driver] msg json style mismatch')
            for key in self._sub_dict:
                if key in msg_data:
                    if msg_data[key] == self._sub_dict[key]:
                        return 'done'
                    elif self._sub_dict[0:1] == "=":
                        if float(msg_data[key]) == float(self._sub_dict[1:]):
                            return 'done'
                    elif self._sub_dict[0:2] == "~=":
                        digits = 10**len(self._sub_dict.split('.')[1])
                        if round(float(msg_data[key]) * digits) \
                        == round(float(self._sub_dict[2:]) * digits):
                            return 'done'
                    elif self._sub_dict[0:2] == "!=":
                        if float(msg_data[key]) != float(self._sub_dict[2:]):
                            return 'done'
                    elif self._sub_dict[0:2] == ">=" or self._sub_dict[0:2] == "=>":
                        if float(msg_data[key]) >= float(self._sub_dict[2:]):
                            return 'done'
                    elif self._sub_dict[0:2] == "<=" or self._sub_dict[0:2] == "=<":
                        if float(msg_data[key]) <= float(self._sub_dict[2:]):
                            return 'done'
                    elif self._sub_dict[0:1] == ">":
                        if float(msg_data[key]) > float(self._sub_dict[2:]):
                            return 'done'
                    elif self._sub_dict[0:1] == "<":
                        if float(msg_data[key]) < float(self._sub_dict[2:]):
                            return 'done'

    def on_enter(self, userdata):
        update_msg = String()
        update_msg.data = self.name
        self._update_pub.publish('flexbe/behavior_updating', update_msg)

        msg = String()
        msg.data = json.dumps(self._pub_dict)
        self._pub.publish(self._pub_topic, msg)
        self._time_publish = rospy.Time.now()

        self._sub.enable_buffer(self._sub_topic)
        self._time_enter = rospy.Time.now()

    def on_exit(self, userdata):
        self._sub.disable_buffer(self._sub_topic)
