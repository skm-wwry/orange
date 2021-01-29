#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.initialization_ending import InitializationEnding
from agv_flexbe_states.judge_amcl import JudgeAMCL
from agv_flexbe_states.site_initialization import SiteInitialization
from agv_flexbe_states.task_switch import TaskSwitch
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 01 2020
@author: zenglei
'''
class initial_taskSM(Behavior):
	'''
	initialization: pose - alert
	'''


	def __init__(self):
		super(initial_taskSM, self).__init__()
		self.name = 'initial_task'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:633 y:240
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:346 y:24
			OperatableStateMachine.add('initial_pose',
										SiteInitialization(site_name="home"),
										transitions={'done': 'judge_amcl'},
										autonomy={'done': Autonomy.Off})

			# x:347 y:124
			OperatableStateMachine.add('judge_amcl',
										JudgeAMCL(),
										transitions={'true': 'realsense_rear', 'false': 'wait1s'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off})

			# x:138 y:198
			OperatableStateMachine.add('realsense_front',
										TaskSwitch(seq=1, frame_id="launch_~/catkin_ws/install/share/bringup/launch/camera_front.launch"),
										transitions={'done': 'wait10s'},
										autonomy={'done': Autonomy.Off})

			# x:347 y:424
			OperatableStateMachine.add('realsense_rear',
										TaskSwitch(seq=1, frame_id="launch_~/catkin_ws/install/share/bringup/launch/camera_rear.launch"),
										transitions={'done': 'wait15s'},
										autonomy={'done': Autonomy.Off})

			# x:597 y:524
			OperatableStateMachine.add('scan_merger',
										TaskSwitch(seq=1, frame_id="launch_~/catkin_ws/install/share/bringup/launch/scan_merger.launch"),
										transitions={'done': 'wait3s'},
										autonomy={'done': Autonomy.Off})

			# x:154 y:293
			OperatableStateMachine.add('wait10s',
										WaitState(wait_time=10),
										transitions={'done': 'realsense_rear'},
										autonomy={'done': Autonomy.Off})

			# x:358 y:524
			OperatableStateMachine.add('wait15s',
										WaitState(wait_time=10),
										transitions={'done': 'scan_merger'},
										autonomy={'done': Autonomy.Off})

			# x:608 y:24
			OperatableStateMachine.add('wait1s',
										WaitState(wait_time=1),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:608 y:424
			OperatableStateMachine.add('wait3s',
										WaitState(wait_time=3),
										transitions={'done': 'initial_music'},
										autonomy={'done': Autonomy.Off})

			# x:596 y:324
			OperatableStateMachine.add('initial_music',
										InitializationEnding(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
