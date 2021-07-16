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
from agv_flexbe_states.turn_right import TurnRight
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: zenglei
'''
class turn_rightSM(Behavior):
	'''
	turn right 90 degree
	'''


	def __init__(self):
		super(turn_rightSM, self).__init__()
		self.name = 'turn_right'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:233 y:440
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:185 y:124
			OperatableStateMachine.add('open_carrier_enabled',
										ReconfigureState(client="cmd_vel_rectifier", parameter="carrier_enabled", value=True),
										transitions={'done': 'turn_right_90'},
										autonomy={'done': Autonomy.Off})

			# x:407 y:224
			OperatableStateMachine.add('log',
										LogState(text="failed to turn right", severity=Logger.REPORT_HINT),
										transitions={'done': 'turn_right_90'},
										autonomy={'done': Autonomy.Off})

			# x:196 y:224
			OperatableStateMachine.add('turn_right_90',
										TurnRight(),
										transitions={'succeeded': 'close_carrier_enabled', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:184 y:324
			OperatableStateMachine.add('close_carrier_enabled',
										ReconfigureState(client="cmd_vel_rectifier", parameter="carrier_enabled", value=False),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
