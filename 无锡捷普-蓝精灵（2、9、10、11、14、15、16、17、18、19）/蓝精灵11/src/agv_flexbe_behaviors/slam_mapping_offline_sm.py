#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.kill_node import KillNode
from agv_flexbe_states.task_switch import TaskSwitch
from agv_flexbe_states.wait_time import WaitTime
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Sep 28 2020
@author: Zeng Lei
'''
class slam_mapping_offlineSM(Behavior):
	'''
	slam toolbox mapping
	'''


	def __init__(self):
		super(slam_mapping_offlineSM, self).__init__()
		self.name = 'slam_mapping_offline'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:333 y:40
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:91 y:174
			OperatableStateMachine.add('kill_map_publisher',
										KillNode(node="/map_stream"),
										transitions={'done': 'kill_ekf_global'},
										autonomy={'done': Autonomy.Off})

			# x:97 y:274
			OperatableStateMachine.add('kill_ekf_global',
										KillNode(node="/ekf_node_global"),
										transitions={'done': 'kill_amcl'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:174
			OperatableStateMachine.add('slam_alert',
										AlertPlay(sound_id=20, mode="single", wait_time=3, single_time=3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:289 y:374
			OperatableStateMachine.add('slam_offline_launch',
										TaskSwitch(seq=1, frame_id="launch_/home/hitrobot/catkin_ws/devel/share/slam_toolbox/offline.launch"),
										transitions={'done': 'wait2s'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:274
			OperatableStateMachine.add('wait2s',
										WaitTime(wait_time=1),
										transitions={'done': 'slam_alert'},
										autonomy={'done': Autonomy.Off})

			# x:97 y:374
			OperatableStateMachine.add('kill_amcl',
										KillNode(node="/amcl"),
										transitions={'done': 'slam_offline_launch'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
