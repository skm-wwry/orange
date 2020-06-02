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
Created on Wed Apr 22 2020
@author: ouiyeah
'''
class lift_bias_posSM(Behavior):
	'''
	lift_bias_pos
	'''


	def __init__(self):
		super(lift_bias_posSM, self).__init__()
		self.name = 'lift_bias_pos'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:321
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:149 y:93
			OperatableStateMachine.add('lift_bias_pos',
										string_pub(topic="drive_request", data="lift_bias_pos"),
										transitions={'done': 'lift_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:370 y:108
			OperatableStateMachine.add('lift_state_request',
										string_pub(topic="drive_request", data="state_lift"),
										transitions={'done': 'lift_state_response'},
										autonomy={'done': Autonomy.Off})

			# x:333 y:251
			OperatableStateMachine.add('lift_state_response',
										diagnostic_array_sub(topic="state_lift", key="pos_real", value=">=0.002", hardware_id="", timeout=1.0),
										transitions={'done': 'finished', 'failed': 'wait_100ms'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})

			# x:244 y:174
			OperatableStateMachine.add('wait_100ms',
										WaitState(wait_time=0.1),
										transitions={'done': 'lift_bias_pos'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
