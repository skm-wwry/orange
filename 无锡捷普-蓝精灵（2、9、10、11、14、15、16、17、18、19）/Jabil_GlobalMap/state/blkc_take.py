#!/usr/bin/env python

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxySubscriberCached, ProxyActionClient, ProxyPublisher
from actionlib_msgs.msg import GoalStatus, GoalID
from move_base_msgs.msg import *
from geometry_msgs.msg import Quaternion
import tf
import actionlib
from std_msgs.msg import Header, String
import time
import yaml
import getpass
import rospy
import json
'''
Created on 28.05.2020
@author: lei.zeng@tu-dortmund.de
'''


class BlkcTake(EventState):
    '''
    navigate to blkc take site
    '''

    def __init__(self):
        super(BlkcTake, self).__init__(outcomes=['arrived', 'canceled', 'failed'],
                                       input_keys=['to_site'])
        self._site_name = 'none'
        self._update_pub = ProxyPublisher({'flexbe/behavior_updating': String})
        self._action_topic = "move_base"
        self._client = ProxyActionClient({self._action_topic: MoveBaseAction})
        self._res = None

        yaml_path = rospy.get_param(
            "~waypoints_path", "~/catkin_ws/dbparam/flexbe_waypoints.yaml")
        if yaml_path != "":
            if yaml_path[0] == '~':
                absolute_path = '/home/' + getpass.getuser() + yaml_path[1:]
            with open(absolute_path) as f:
                self._waypoints = yaml.safe_load(f)

    def execute(self, userdata):
        if self._client.has_result(self._action_topic):
            status = self._client.get_state(self._action_topic)
            if status == GoalStatus.SUCCEEDED:
                return 'arrived'
            elif status in [GoalStatus.PREEMPTED]:
                Logger.logwarn('navigation canceled: %s' % str(status))
                return 'canceled'
            elif status in [
                    GoalStatus.REJECTED, GoalStatus.RECALLED,
                    GoalStatus.ABORTED
            ]:
                Logger.logwarn('navigation failed: %s' % str(status))
                return 'failed'

    def on_enter(self, userdata):
        to_site = userdata.to_site
        self._site_name = to_site[:6]+"take"
        self._nav_site = self._waypoints[self._site_name]

        update_msg = String()
        update_msg.data = self._site_name
        self._update_pub.publish('flexbe/behavior_updating', update_msg)

        mv_goal = MoveBaseActionGoal()
        mv_goal.goal.target_pose.header.stamp = rospy.Time.now()
        mv_goal.goal.target_pose.header.frame_id = self._nav_site['frame_id']
        mv_goal.goal.target_pose.pose.position.x = self._nav_site['pose'][
            'position']['x']
        mv_goal.goal.target_pose.pose.position.y = self._nav_site['pose'][
            'position']['y']
        mv_goal.goal.target_pose.pose.position.z = self._nav_site['pose'][
            'position']['z']
        mv_goal.goal.target_pose.pose.orientation = Quaternion(
            self._nav_site['pose']['orientation']['x'],
            self._nav_site['pose']['orientation']['y'],
            self._nav_site['pose']['orientation']['z'],
            self._nav_site['pose']['orientation']['w'])
        try:
            self._client.send_goal(self._action_topic, mv_goal.goal)
            Logger.loginfo("navigation goal: %s" % self._site_name)
            Logger.loginfo(
                "send navigation goal with position:({0}, {1}, {2}) and  orientation: ({3}, {4}, {5}, {6})"
                .format(self._nav_site['pose']['position']['x'],
                        self._nav_site['pose']['position']['y'],
                        self._nav_site['pose']['position']['z'],
                        self._nav_site['pose']['orientation']['x'],
                        self._nav_site['pose']['orientation']['y'],
                        self._nav_site['pose']['orientation']['z'],
                        self._nav_site['pose']['orientation']['w']))
        except Exception as e:
            Logger.logwarn('Failed to connect to movebase server')

    def cancel_active_goals(self):
        if self._client.is_available(self._action_topic):
            if self._client.is_active(self._action_topic):
                if not self._client.has_result(self._action_topic):
                    self._client.cancel(self._action_topic)
                    Logger.loginfo('Canceling navigation active goal.')

    def on_exit(self, userdata):
        self.cancel_active_goals()

    def on_pause(self):
        self.cancel_active_goals()
