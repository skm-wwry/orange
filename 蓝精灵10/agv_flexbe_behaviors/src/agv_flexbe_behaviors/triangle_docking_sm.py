#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.task_switch import TaskSwitch
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: zenglei
'''
class triangle_dockingSM(Behavior):
	'''
	triangle docking
	'''


	def __init__(self):
		super(triangle_dockingSM, self).__init__()
		self.name = 'triangle_docking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:172 y:570, x:492 y:545
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:119 y:66
			OperatableStateMachine.add('triangle_on',
										TaskSwitch(seq=1, frame_id="triangle"),
										transitions={'done': 'triangle_aiming'},
										autonomy={'done': Autonomy.Off})

			# x:120 y:166
			OperatableStateMachine.add('triangle_aiming',
										WaitState(wait_time=15),
										transitions={'done': 'triangle_homing'},
										autonomy={'done': Autonomy.Off})

			# x:127 y:262
			OperatableStateMachine.add('triangle_homing',
										HomingControl(target_frame="base_object", target_x=-0.5, target_y=0, target_yaw=0),
										transitions={'succeeded': 'triangle_off', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:122 y:388
			OperatableStateMachine.add('triangle_off',
										TaskSwitch(seq=0, frame_id="triangle"),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:369 y:260
			OperatableStateMachine.add('log',
										LogState(text="log", severity=Logger.REPORT_HINT),
										transitions={'done': 'triangle_homing'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
