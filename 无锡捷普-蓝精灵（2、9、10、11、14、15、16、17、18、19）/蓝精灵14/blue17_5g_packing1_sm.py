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
from agv_flexbe_behaviors.turn_right_sm import turn_rightSM
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.site_navigation import SiteNavigation
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Sep 25 2020
@author: sunkm
'''
class blue17_5G_packing1SM(Behavior):
	'''
	blue17_5G_packing1
	'''


	def __init__(self):
		super(blue17_5G_packing1SM, self).__init__()
		self.name = 'blue17_5G_packing1'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_dumpSM, 'lift_dump_2')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(lift_loadSM, 'lift_load_2')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(shelf_dockingSM, 'shelf_docking_2')
		self.add_behavior(turn_leftSM, 'turn_left_2')
		self.add_behavior(turn_leftSM, 'turn_left_3')
		self.add_behavior(turn_leftSM, 'turn_left_4')
		self.add_behavior(turn_rightSM, 'turn_right')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:82 y:415, x:483 y:240
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:24
			OperatableStateMachine.add('blue17_up1',
										SiteNavigation(site_name="blue17_up1"),
										transitions={'arrived': 'shelf_docking', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:846 y:24
			OperatableStateMachine.add('blue17_down1',
										SiteNavigation(site_name="blue17_down1"),
										transitions={'arrived': 'lift_dump', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:646 y:524
			OperatableStateMachine.add('blue17_down2',
										SiteNavigation(site_name="blue17_down2"),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1047 y:324
			OperatableStateMachine.add('blue17_up2',
										SiteNavigation(site_name="blue17_up2"),
										transitions={'arrived': 'shelf_docking_2', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1047 y:224
			OperatableStateMachine.add('do_forward50',
										HomingControl(target_frame="base_link", target_x=0.5, target_y=0, target_yaw=0),
										transitions={'succeeded': 'blue17_up2', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1025 y:21
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:425 y:521
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turn_left_4'},
										autonomy={'finished': Autonomy.Inherit})

			# x:625 y:21
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blue17_down1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:825 y:521
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'blue17_down2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:225 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turn_right', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1025 y:421
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turn_left_3', 'failed': 'wait1s'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1026 y:121
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'turn_left_2'),
										transitions={'finished': 'do_forward50'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1025 y:521
			OperatableStateMachine.add('turn_left_3',
										self.use_behavior(turn_leftSM, 'turn_left_3'),
										transitions={'finished': 'lift_load_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:225 y:521
			OperatableStateMachine.add('turn_left_4',
										self.use_behavior(turn_leftSM, 'turn_left_4'),
										transitions={'finished': 'blue17'},
										autonomy={'finished': Autonomy.Inherit})

			# x:425 y:21
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'turn_right'),
										transitions={'finished': 'lift_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:357 y:424
			OperatableStateMachine.add('wait1s',
										WaitState(wait_time=1),
										transitions={'done': 'blue17'},
										autonomy={'done': Autonomy.Off})

			# x:46 y:524
			OperatableStateMachine.add('blue17',
										SiteNavigation(site_name="blue17"),
										transitions={'arrived': 'finished', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
