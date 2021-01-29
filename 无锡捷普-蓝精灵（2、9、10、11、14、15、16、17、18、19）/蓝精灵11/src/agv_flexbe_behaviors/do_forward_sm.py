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
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: zenglei
'''
class do_forwardSM(Behavior):
	'''
	do forward 100cm
	'''


	def __init__(self):
		super(do_forwardSM, self).__init__()
		self.name = 'do_forward'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:342
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:127 y:103
			OperatableStateMachine.add('do_forward_100cm',
										HomingControl(target_frame="base_link", target_x=1, target_y=0, target_yaw=0),
										transitions={'succeeded': 'finished', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:424 y:99
			OperatableStateMachine.add('log',
										LogState(text="failed to do forward", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_forward_100cm'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
