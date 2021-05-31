#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.alert_loop_stop import AlertLoopStop
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.homing_shelf import ShelfHoming
from agv_flexbe_states.reconfigure_state import ReconfigureState
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
		# x:283 y:590, x:483 y:590
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:46 y:74
			OperatableStateMachine.add('shelf_on',
										ShelfOn(),
										transitions={'done': 'alert_on_shelf'},
										autonomy={'done': Autonomy.Off})

			# x:437 y:274
			OperatableStateMachine.add('alert_stop_no_target',
										AlertLoopStop(),
										transitions={'done': 'shelf_off_no_target'},
										autonomy={'done': Autonomy.Off})

			# x:246 y:274
			OperatableStateMachine.add('alert_stop_shelf',
										AlertLoopStop(),
										transitions={'done': 'shelf_off'},
										autonomy={'done': Autonomy.Off})

			# x:246 y:474
			OperatableStateMachine.add('leg_remove_true',
										ReconfigureState(client="scan_rectifier", parameter="footprint_enabled", value=True),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:256 y:74
			OperatableStateMachine.add('shelf_aiming',
										WaitState(wait_time=5),
										transitions={'done': 'shelf_homing'},
										autonomy={'done': Autonomy.Off})

			# x:246 y:174
			OperatableStateMachine.add('shelf_homing',
										ShelfHoming(),
										transitions={'succeeded': 'alert_stop_shelf', 'failed': 'shelf_homing_resend', 'no_target': 'alert_stop_no_target'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off, 'no_target': Autonomy.Off})

			# x:435 y:174
			OperatableStateMachine.add('shelf_homing_resend',
										LogState(text="resend shelf homing goal", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_homing'},
										autonomy={'done': Autonomy.Off})

			# x:246 y:374
			OperatableStateMachine.add('shelf_off',
										ShelfOff(),
										transitions={'done': 'leg_remove_true'},
										autonomy={'done': Autonomy.Off})

			# x:440 y:374
			OperatableStateMachine.add('shelf_off_no_target',
										ShelfOff(),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:46 y:174
			OperatableStateMachine.add('alert_on_shelf',
										AlertPlay(sound_id=15, mode="loop", wait_time=3, single_time=3),
										transitions={'done': 'shelf_aiming'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
