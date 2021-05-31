#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.driver import driver
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
		# x:133 y:290, x:233 y:140
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.topic = 'drive_request'
		_state_machine.userdata.name = ''
		_state_machine.userdata.mb_addr = 0
		_state_machine.userdata.mb_data = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:46 y:74
			OperatableStateMachine.add('rotate_load',
										driver(topic='', name='rotate_pos', mb_addr='', mb_data='1.57', timeoff=1.0, timeout=0.0),
										transitions={'done': 'rotate_stop', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'topic', 'name': 'name', 'mb_addr': 'mb_addr', 'mb_data': 'mb_data', 'mb_expect': 'mb_expect', 'mb_except': 'mb_except'})

			# x:46 y:174
			OperatableStateMachine.add('rotate_stop',
										driver(topic='', name='rotate_vel', mb_addr='', mb_data='', timeoff=0.0, timeout=0.0),
										transitions={'done': 'finished', 'failed': 'failed'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'topic', 'name': 'name', 'mb_addr': 'mb_addr', 'mb_data': 'mb_data', 'mb_expect': 'mb_expect', 'mb_except': 'mb_except'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
