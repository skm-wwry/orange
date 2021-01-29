#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.diagnostic_array_sub import diagnostic_array_sub
from agv_flexbe_states.string_pub import string_pub
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: ouiyeah
'''
class wheel_rotate_rightSM(Behavior):
	'''
	wheel_rotate_right
	'''


	def __init__(self):
		super(wheel_rotate_rightSM, self).__init__()
		self.name = 'wheel_rotate_right'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:586
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:129 y:94
			OperatableStateMachine.add('wheel_rotate_right',
										string_pub(topic="drive_request", data="wheel_rotate_right"),
										transitions={'done': 'left_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:375 y:189
			OperatableStateMachine.add('left_state_response',
										diagnostic_array_sub(topic="state_left", key="pos_stop", value="1", hardware_id="", timeout=1.0),
										transitions={'done': 'right_state_request', 'failed': 'wait_100ms_left'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:540 y:123
			OperatableStateMachine.add('right_state_request',
										string_pub(topic="drive_request", data="state_right"),
										transitions={'done': 'right_state_response'},
										autonomy={'done': Autonomy.Off})

			# x:518 y:235
			OperatableStateMachine.add('right_state_response',
										diagnostic_array_sub(topic="state_right", key="pos_stop", value="1", hardware_id="", timeout=1.0),
										transitions={'done': 'rotate_state_request', 'failed': 'wait_100ms_right'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:315 y:362
			OperatableStateMachine.add('rotate_state_request',
										string_pub(topic="drive_request", data="state_rotate"),
										transitions={'done': 'rotate_state_response'},
										autonomy={'done': Autonomy.Off})

			# x:303 y:465
			OperatableStateMachine.add('rotate_state_response',
										diagnostic_array_sub(topic="state_rotate", key="pos_stop", value="1", hardware_id="", timeout=1.0),
										transitions={'done': 'finished', 'failed': 'wait_100ms_rotate'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:163 y:191
			OperatableStateMachine.add('wait_100ms_left',
										WaitState(wait_time=0.1),
										transitions={'done': 'left_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:692 y:161
			OperatableStateMachine.add('wait_100ms_right',
										WaitState(wait_time=0.1),
										transitions={'done': 'right_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:114 y:396
			OperatableStateMachine.add('wait_100ms_rotate',
										WaitState(wait_time=0.1),
										transitions={'done': 'rotate_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:385 y:56
			OperatableStateMachine.add('left_state_request',
										string_pub(topic="drive_request", data="state_left"),
										transitions={'done': 'left_state_response'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
