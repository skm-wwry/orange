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
from agv_flexbe_states.reconfigure_state import ReconfigureState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: ouiyeah
'''
class lift_dumpSM(Behavior):
	'''
	lift_dump
	'''


	def __init__(self):
		super(lift_dumpSM, self).__init__()
		self.name = 'lift_dump'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:283 y:590
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.topic = 'drive_request'
		_state_machine.userdata.name = ''
		_state_machine.userdata.mb_addr = 0
		_state_machine.userdata.mb_data = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:246 y:74
			OperatableStateMachine.add('lift_dump',
										driver(topic='', name='lift_pos', mb_addr='', mb_data='', timeoff=1.0, timeout=0.0),
										transitions={'done': 'lift_stop', 'failed': 'lift_stop'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'topic', 'name': 'name', 'mb_addr': 'mb_addr', 'mb_data': 'mb_data', 'mb_expect': 'mb_expect', 'mb_except': 'mb_except'})

			# x:240 y:374
			OperatableStateMachine.add('agv_local_footprint',
										ReconfigureState(client="move_base/local_costmap", parameter="footprint", value='[[0.347, -0.26], [0.347, 0.26], [-0.342, 0.26], [-0.342, -0.26]]'),
										transitions={'done': 'shelf_leg_remove_false'},
										autonomy={'done': Autonomy.Off})

			# x:246 y:174
			OperatableStateMachine.add('lift_stop',
										driver(topic='', name='lift_vel', mb_addr='', mb_data='', timeoff=0.0, timeout=0.0),
										transitions={'done': 'agv_global_footprint', 'failed': 'lift_stop'},
										autonomy={'done': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'topic': 'topic', 'name': 'name', 'mb_addr': 'mb_addr', 'mb_data': 'mb_data', 'mb_expect': 'mb_expect', 'mb_except': 'mb_except'})

			# x:230 y:474
			OperatableStateMachine.add('shelf_leg_remove_false',
										ReconfigureState(client="scan_rectifier", parameter="footprint_enabled", value=False),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:237 y:274
			OperatableStateMachine.add('agv_global_footprint',
										ReconfigureState(client="move_base/global_costmap", parameter="footprint", value='[[0.347, -0.26], [0.347, 0.26], [-0.342, 0.26], [-0.342, -0.26]]'),
										transitions={'done': 'agv_local_footprint'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
