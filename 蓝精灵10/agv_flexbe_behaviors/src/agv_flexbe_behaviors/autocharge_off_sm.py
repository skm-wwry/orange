#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.agv_footprint import AgvFootprint
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.joy_operation import JoyOperation
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 15 2020
@author: zenglei
'''
class autocharge_offSM(Behavior):
	'''
	autocharge off
	'''


	def __init__(self):
		super(autocharge_offSM, self).__init__()
		self.name = 'autocharge_off'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:206 y:439, x:344 y:315
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:170 y:47
			OperatableStateMachine.add('joy_start_0',
										JoyOperation(topic="joy_feedback_array", idd=7, intensity=0, typee=1),
										transitions={'done': 'agv_footprint'},
										autonomy={'done': Autonomy.Off})

			# x:164 y:306
			OperatableStateMachine.add('goal_forward',
										HomingControl(target_frame="base_link", target_x=0.15, target_y=0, target_yaw=0),
										transitions={'succeeded': 'finished', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:167 y:155
			OperatableStateMachine.add('agv_footprint',
										AgvFootprint(),
										transitions={'done': 'goal_forward'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
