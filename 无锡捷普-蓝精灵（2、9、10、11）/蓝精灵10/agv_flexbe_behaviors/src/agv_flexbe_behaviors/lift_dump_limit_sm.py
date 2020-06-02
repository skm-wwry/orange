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
from agv_flexbe_states.twist_pub import twist_pub
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: ouiyeah
'''
class lift_dump_limitSM(Behavior):
	'''
	lift_dump_limit
	'''


	def __init__(self):
		super(lift_dump_limitSM, self).__init__()
		self.name = 'lift_dump_limit'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:347
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:92 y:47
			OperatableStateMachine.add('lift_down_vel',
										twist_pub(topic="cmd_vel_carried", linear_x=0.0, linear_y=0.0, linear_z=-0.0041666, angular_x=0.0, angular_y=0.0, angular_z=0.0),
										transitions={'done': 'lift_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:265 y:100
			OperatableStateMachine.add('lift_state_request',
										string_pub(topic="drive_request", data="state_lift"),
										transitions={'done': 'lift_state_response'},
										autonomy={'done': Autonomy.Off})

			# x:259 y:257
			OperatableStateMachine.add('lift_state_response',
										diagnostic_array_sub(topic="state_lift", key="estop", value="2", hardware_id="", timeout=1.0),
										transitions={'done': 'lift_stop_vel', 'failed': 'wait_100ms'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:76 y:242
			OperatableStateMachine.add('lift_stop_vel',
										twist_pub(topic="cmd_vel_carried", linear_x=0.0, linear_y=0.0, linear_z=0.0, angular_x=0.0, angular_y=0.0, angular_z=0.0),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:178 y:150
			OperatableStateMachine.add('wait_100ms',
										WaitState(wait_time=0.1),
										transitions={'done': 'lift_down_vel'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
