#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.homing_shelf import ShelfHoming
from agv_flexbe_states.shelf_leg_remove_true import ShelfLegRemoveTrue
from agv_flexbe_states.shelf_off import ShelfOff
from agv_flexbe_states.shelf_on import ShelfOn
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jan 08 2020
@author: Lei Zeng
'''
class shelf_dockingSM(Behavior):
	'''
	shelf docking sub-behavior
	'''


	def __init__(self):
		super(shelf_dockingSM, self).__init__()
		self.name = 'shelf_docking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:442 y:468, x:169 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('shelf_on',
										ShelfOn(),
										transitions={'done': 'shelf_aiming'},
										autonomy={'done': Autonomy.Off})

			# x:234 y:41
			OperatableStateMachine.add('shelf_aiming',
										WaitState(wait_time=5),
										transitions={'done': 'shelf_homing'},
										autonomy={'done': Autonomy.Off})

			# x:396 y:45
			OperatableStateMachine.add('shelf_homing',
										ShelfHoming(),
										transitions={'succeeded': 'shelf_off', 'failed': 'shelf_homing_resend'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:628 y:40
			OperatableStateMachine.add('shelf_homing_resend',
										LogState(text="resend shelf homing goal", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_homing'},
										autonomy={'done': Autonomy.Off})

			# x:393 y:216
			OperatableStateMachine.add('shelf_off',
										ShelfOff(),
										transitions={'done': 'leg_remove_true'},
										autonomy={'done': Autonomy.Off})

			# x:385 y:339
			OperatableStateMachine.add('leg_remove_true',
										ShelfLegRemoveTrue(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
