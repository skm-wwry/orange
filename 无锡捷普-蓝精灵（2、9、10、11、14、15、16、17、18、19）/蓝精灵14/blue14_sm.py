#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.shelf_docking_sm import shelf_dockingSM
from agv_flexbe_behaviors.turn_left_sm import turn_leftSM
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.site_navigation import SiteNavigation
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Sep 25 2020
@author: sunkm
'''
class blue14SM(Behavior):
	'''
	blue14
	'''


	def __init__(self):
		super(blue14SM, self).__init__()
		self.name = 'blue14'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(turn_leftSM, 'turn_left')
		self.add_behavior(turn_leftSM, 'turn_left_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:633 y:440, x:383 y:340
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:75 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turn_left', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:346 y:524
			OperatableStateMachine.add('do_forward50',
										HomingControl(target_frame="base_link", target_x=0.5, target_y=0, target_yaw=0),
										transitions={'succeeded': 'blue14', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:96 y:324
			OperatableStateMachine.add('lift_down1',
										SiteNavigation(site_name="lift_down1"),
										transitions={'arrived': 'lift_dump', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:75 y:421
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:75 y:221
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'lift_down1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:75 y:121
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'turn_left'),
										transitions={'finished': 'lift_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:75 y:521
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'turn_left_2'),
										transitions={'finished': 'do_forward50'},
										autonomy={'finished': Autonomy.Inherit})

			# x:596 y:524
			OperatableStateMachine.add('blue14',
										SiteNavigation(site_name="blue14"),
										transitions={'arrived': 'finished', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
