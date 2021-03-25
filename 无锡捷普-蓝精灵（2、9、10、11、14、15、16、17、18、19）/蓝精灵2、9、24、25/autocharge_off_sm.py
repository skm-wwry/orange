#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.agv_footprint import AgvFootprint
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.joy_operation import JoyOperation
from agv_flexbe_states.site_navigation import SiteNavigation
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 15 2020
@author: zenglei
'''
class autocharge_offSM(Behavior):
	'''
	autocharge off
	'''


	def __init__(self):
		super(autocharge_offSM, self).__init__()
		self.name = 'autocharge_off'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:183 y:490
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:146 y:24
			OperatableStateMachine.add('joy_start_0',
										JoyOperation(topic="joy_feedback_array", idd=7, intensity=0, typee=1),
										transitions={'done': 'agv_footprint'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:374
			OperatableStateMachine.add('charge_off_alert',
										AlertPlay(sound_id=1, mode="single", wait_time=2, single_time=3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:224
			OperatableStateMachine.add('home',
										SiteNavigation(site_name="initial_pose"),
										transitions={'arrived': 'charge_off_alert', 'canceled': 'log', 'failed': 'log'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:357 y:224
			OperatableStateMachine.add('log',
										LogState(text="haha", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:124
			OperatableStateMachine.add('agv_footprint',
										AgvFootprint(),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
