#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.reconfigure_state import ReconfigureState
from agv_flexbe_states.turn_left import TurnLeft
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: zenglei
'''
class turn_leftSM(Behavior):
	'''
	turn left 90 degree
	'''


	def __init__(self):
		super(turn_leftSM, self).__init__()
		self.name = 'turn_left'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:183 y:390
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:145 y:74
			OperatableStateMachine.add('cmd_vel_rectifier',
										ReconfigureState(client="cmd_vel_rectifier", parameter="carrier_enabled", value=True),
										transitions={'done': 'turn_left_90'},
										autonomy={'done': Autonomy.Off})

			# x:357 y:174
			OperatableStateMachine.add('log',
										LogState(text="failed to turn left", severity=Logger.REPORT_HINT),
										transitions={'done': 'turn_left_90'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:174
			OperatableStateMachine.add('turn_left_90',
										TurnLeft(),
										transitions={'succeeded': 'carrier_enabled', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:146 y:274
			OperatableStateMachine.add('carrier_enabled',
										ReconfigureState(client="cmd_vel_rectifier", parameter="carrier_enabled", value=False),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
