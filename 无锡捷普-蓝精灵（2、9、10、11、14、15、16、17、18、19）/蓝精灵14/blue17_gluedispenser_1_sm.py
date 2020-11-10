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
from agv_flexbe_behaviors.wheel_load_pos_sm import wheel_load_posSM
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.wait_time import WaitTime
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Sep 25 2020
@author: sunkm
'''
class blue17_glueDispenser_1SM(Behavior):
	'''
	glue dispenser site1
	'''


	def __init__(self):
		super(blue17_glueDispenser_1SM, self).__init__()
		self.name = 'blue17_glueDispenser_1'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(wheel_load_posSM, 'wheel_load_pos')
		self.add_behavior(wheel_load_posSM, 'wheel_load_pos_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:835 y:240, x:633 y:240
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:75 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'wheel_load_pos', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:796 y:524
			OperatableStateMachine.add('do_forward50',
										HomingControl(target_frame="base_link", target_x=0.5, target_y=0, target_yaw=0),
										transitions={'succeeded': 'blue17', 'failed': 'failed'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:96 y:424
			OperatableStateMachine.add('lift_down2',
										SiteNavigation(site_name="lift_down2"),
										transitions={'arrived': 'lift_dump', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:75 y:521
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'wheel_load_pos_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:75 y:321
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'lift_down2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:96 y:224
			OperatableStateMachine.add('wait1s',
										WaitTime(wait_time=1),
										transitions={'done': 'lift_load'},
										autonomy={'done': Autonomy.Off})

			# x:546 y:524
			OperatableStateMachine.add('wait2s',
										WaitTime(wait_time=1),
										transitions={'done': 'do_forward50'},
										autonomy={'done': Autonomy.Off})

			# x:75 y:121
			OperatableStateMachine.add('wheel_load_pos',
										self.use_behavior(wheel_load_posSM, 'wheel_load_pos'),
										transitions={'finished': 'wait1s'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:521
			OperatableStateMachine.add('wheel_load_pos_2',
										self.use_behavior(wheel_load_posSM, 'wheel_load_pos_2'),
										transitions={'finished': 'wait2s'},
										autonomy={'finished': Autonomy.Inherit})

			# x:796 y:374
			OperatableStateMachine.add('blue17',
										SiteNavigation(site_name="blue17"),
										transitions={'arrived': 'finished', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
