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
from agv_flexbe_states.one_off import OneOff
from agv_flexbe_states.one_on import OneOn
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Mar 03 2020
@author: Lei Zeng
'''
class one_dockingSM(Behavior):
	'''
	one docking
	'''


	def __init__(self):
		super(one_dockingSM, self).__init__()
		self.name = 'one_docking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:850 y:125
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:29 y:116
			OperatableStateMachine.add('one_on',
										OneOn(),
										transitions={'done': 'one_aiming'},
										autonomy={'done': Autonomy.Off})

			# x:223 y:118
			OperatableStateMachine.add('one_aiming',
										WaitState(wait_time=10),
										transitions={'done': 'one_homing'},
										autonomy={'done': Autonomy.Off})

			# x:399 y:118
			OperatableStateMachine.add('one_homing',
										HomingControl(target_frame="base_object", target_x=-0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'one_off', 'failed': 'homing_resend'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:609 y:118
			OperatableStateMachine.add('one_off',
										OneOff(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:399 y:283
			OperatableStateMachine.add('homing_resend',
										LogState(text="one homing resend", severity=Logger.REPORT_HINT),
										transitions={'done': 'one_homing'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
