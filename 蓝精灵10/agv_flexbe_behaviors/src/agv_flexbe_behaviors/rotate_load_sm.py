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
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: ouiyeah
'''
class rotate_loadSM(Behavior):
	'''
	rotate_load
	'''


	def __init__(self):
		super(rotate_loadSM, self).__init__()
		self.name = 'rotate_load'

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
			# x:203 y:41
			OperatableStateMachine.add('rotate_load_pos',
										string_pub(topic="drive_request", data="rotate_load_pos"),
										transitions={'done': 'rotate_state_request'},
										autonomy={'done': Autonomy.Off})

			# x:419 y:60
			OperatableStateMachine.add('rotate_state_request',
										string_pub(topic="drive_request", data="state_rotate"),
										transitions={'done': 'rotate_state_response'},
										autonomy={'done': Autonomy.Off})

			# x:196 y:226
			OperatableStateMachine.add('rotate_state_response',
										diagnostic_array_sub(topic="state_rotate", key="pos_stop", value="1", hardware_id="", timeout=1.0),
										transitions={'done': 'finished', 'failed': 'rotate_load_pos'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
