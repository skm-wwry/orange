#!/usr/bin/env python
import rospy, time
from flexbe_msgs.msg import BehaviorExecutionActionGoal
from std_msgs.msg import String


class TaskAssign:
    def __init__(self):
        self._flexbe_state = ""
        self._pub_task = rospy.Publisher('flexbe/execute_behavior/goal',
                                         BehaviorExecutionActionGoal,
                                         latch=True,
                                         queue_size=10)
        rospy.Subscriber("flexbe/behavior_updated",
                         String,
                         self.state_cb,
                         queue_size=1)

    def state_cb(self, state_msg):
        self._flexbe_state = state_msg.data


def main():
    rospy.init_node('task_assign')

    TaskAssigner = TaskAssign()
    task_period = rospy.get_param("~task_period", 120)
    counter = 1
    time.sleep(3)

    goal_msg = BehaviorExecutionActionGoal()
    goal_msg.goal.behavior_name = rospy.get_param("~task_name",
                                                  "turn_left")

    print time.localtime(time.time()).tm_min
    while time.localtime(time.time()).tm_min % 5 != 0:
        time.sleep(0.2)

    TaskAssigner._pub_task.publish(goal_msg)
    print time.strftime("%Y-%m-%d-%H-%M-%S: ", time.localtime()), str(counter)

    t_start = time.time()
    while True:
        if time.time(
        ) - t_start > task_period and TaskAssigner._flexbe_state == "behavior_exit":
            TaskAssigner._pub_task.publish(goal_msg)
            counter += 1
            print time.strftime("%Y-%m-%d-%H-%M-%S: ",
                                time.localtime()), str(counter)
            t_start = time.time()
        time.sleep(0.5)

    try:
        rospy.spin()
    except:
        pass


if __name__ == '__main__':
    main()
