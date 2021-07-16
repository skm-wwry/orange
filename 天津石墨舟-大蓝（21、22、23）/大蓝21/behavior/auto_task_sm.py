#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.apriltag_docking_sm import apriltag_dockingSM
from agv_flexbe_behaviors.do_backward_sm import do_backwardSM
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.rotate_dump_sm import rotate_dumpSM
from agv_flexbe_behaviors.rotate_home_sm import rotate_homeSM
from agv_flexbe_behaviors.rotate_load_sm import rotate_loadSM
from agv_flexbe_behaviors.turn_left_sm import turn_leftSM
from agv_flexbe_behaviors.turn_right_sm import turn_rightSM
from agv_flexbe_states.from_where import FromWhere
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.site_transfer_from import SiteTransferFrom
from agv_flexbe_states.site_transfer_to import SiteTransferTo
from agv_flexbe_states.to_where import ToWhere
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 07 2020
@author: sunkm
'''
class auto_taskSM(Behavior):
	'''
	auto navigation task
	'''


	def __init__(self):
		super(auto_taskSM, self).__init__()
		self.name = 'auto_task'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(apriltag_dockingSM, 'down/apriltag_docking')
		self.add_behavior(do_backwardSM, 'down/do_backward')
		self.add_behavior(do_backwardSM, 'down/do_backward_2')
		self.add_behavior(lift_dumpSM, 'down/lift_dump')
		self.add_behavior(rotate_dumpSM, 'down/rotate_dump')
		self.add_behavior(rotate_loadSM, 'down/rotate_load')
		self.add_behavior(turn_leftSM, 'down/turn_left')
		self.add_behavior(turn_rightSM, 'down/turn_right')
		self.add_behavior(apriltag_dockingSM, 'take/apriltag_docking')
		self.add_behavior(do_backwardSM, 'take/do_backward')
		self.add_behavior(do_backwardSM, 'take/do_backward_2')
		self.add_behavior(lift_loadSM, 'take/lift_load')
		self.add_behavior(rotate_homeSM, 'take/rotate_home')
		self.add_behavior(rotate_loadSM, 'take/rotate_load')
		self.add_behavior(turn_leftSM, 'take/turn_left')
		self.add_behavior(turn_rightSM, 'take/turn_right')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1233 y:540, x:1133 y:540
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.to_site = ""
		_state_machine.userdata.des_site = ""
		_state_machine.userdata.from_site = ""

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:412 y:750
		_sm_take_0 = OperatableStateMachine(outcomes=['finished'])

		with _sm_take_0:
			# x:125 y:121
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'take/turn_right'),
										transitions={'finished': 'rotate_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:375 y:321
			OperatableStateMachine.add('do_backward',
										self.use_behavior(do_backwardSM, 'take/do_backward'),
										transitions={'finished': 'apriltag_docking'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:521
			OperatableStateMachine.add('do_backward_2',
										self.use_behavior(do_backwardSM, 'take/do_backward_2'),
										transitions={'finished': 'turn_left'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:421
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'take/lift_load'),
										transitions={'finished': 'do_backward_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:721
			OperatableStateMachine.add('rotate_home',
										self.use_behavior(rotate_homeSM, 'take/rotate_home'),
										transitions={'finished': 'finished'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:221
			OperatableStateMachine.add('rotate_load',
										self.use_behavior(rotate_loadSM, 'take/rotate_load'),
										transitions={'finished': 'apriltag_docking', 'failed': 'rotate_load'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:125 y:621
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'take/turn_left'),
										transitions={'finished': 'rotate_home'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:321
			OperatableStateMachine.add('apriltag_docking',
										self.use_behavior(apriltag_dockingSM, 'take/apriltag_docking'),
										transitions={'finished': 'lift_load', 'failed': 'do_backward'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		# x:433 y:740
		_sm_down_1 = OperatableStateMachine(outcomes=['failed'])

		with _sm_down_1:
			# x:125 y:121
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'down/turn_left'),
										transitions={'finished': 'rotate_dump'},
										autonomy={'finished': Autonomy.Inherit})

			# x:375 y:321
			OperatableStateMachine.add('do_backward',
										self.use_behavior(do_backwardSM, 'down/do_backward'),
										transitions={'finished': 'apriltag_docking'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:521
			OperatableStateMachine.add('do_backward_2',
										self.use_behavior(do_backwardSM, 'down/do_backward_2'),
										transitions={'finished': 'turn_right'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:421
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'down/lift_dump'),
										transitions={'finished': 'do_backward_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:221
			OperatableStateMachine.add('rotate_dump',
										self.use_behavior(rotate_dumpSM, 'down/rotate_dump'),
										transitions={'finished': 'apriltag_docking', 'failed': 'rotate_dump'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:125 y:721
			OperatableStateMachine.add('rotate_load',
										self.use_behavior(rotate_loadSM, 'down/rotate_load'),
										transitions={'finished': 'rotate_load', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:125 y:621
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'down/turn_right'),
										transitions={'finished': 'rotate_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:321
			OperatableStateMachine.add('apriltag_docking',
										self.use_behavior(apriltag_dockingSM, 'down/apriltag_docking'),
										transitions={'finished': 'lift_dump', 'failed': 'do_backward'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:96 y:224
			OperatableStateMachine.add('FromWhere',
										FromWhere(),
										transitions={'done': 'ToWhere'},
										autonomy={'done': Autonomy.Off},
										remapping={'from_site': 'from_site'})

			# x:646 y:324
			OperatableStateMachine.add('ToSiteName',
										SiteTransferTo(),
										transitions={'arrived': 'down', 'canceled': 'ToSiteName', 'failed': 'ToSiteName'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:96 y:324
			OperatableStateMachine.add('ToWhere',
										ToWhere(),
										transitions={'done': 'FromSiteName'},
										autonomy={'done': Autonomy.Off},
										remapping={'des_site': 'des_site', 'to_site': 'to_site'})

			# x:446 y:424
			OperatableStateMachine.add('door_left_open',
										SiteNavigation(site_name="door_left_open", position=[0,0,0], orientation=[0,0,0,1], frame_id="map"),
										transitions={'arrived': 'ToSiteName', 'canceled': 'door_left_open', 'failed': 'door_left_open'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:996 y:424
			OperatableStateMachine.add('door_left_open1',
										SiteNavigation(site_name="door_left_open", position=[0,0,0], orientation=[0,0,0,1], frame_id="map"),
										transitions={'arrived': 'home', 'canceled': 'door_left_open1', 'failed': 'door_left_open1'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:442 y:225
			OperatableStateMachine.add('door_right_open',
										SiteNavigation(site_name="door_right_open", position=[0,0,0], orientation=[0,0,0,1], frame_id="map"),
										transitions={'arrived': 'ToSiteName', 'canceled': 'door_right_open', 'failed': 'door_right_open'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:994 y:224
			OperatableStateMachine.add('door_right_open1',
										SiteNavigation(site_name="door_right_open", position=[0,0,0], orientation=[0,0,0,1], frame_id="map"),
										transitions={'arrived': 'home', 'canceled': 'door_right_open1', 'failed': 'door_right_open1'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:843 y:321
			OperatableStateMachine.add('down',
										_sm_down_1,
										transitions={'failed': 'door_left_open1'},
										autonomy={'failed': Autonomy.Inherit})

			# x:1146 y:324
			OperatableStateMachine.add('home',
										SiteNavigation(site_name="initial_pose", position=[0,0,0], orientation=[0,0,0,1], frame_id="map"),
										transitions={'arrived': 'finished', 'canceled': 'home', 'failed': 'home'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:293 y:321
			OperatableStateMachine.add('take',
										_sm_take_0,
										transitions={'finished': 'door_right_open'},
										autonomy={'finished': Autonomy.Inherit})

			# x:96 y:424
			OperatableStateMachine.add('FromSiteName',
										SiteTransferFrom(),
										transitions={'arrived': 'take', 'canceled': 'FromSiteName', 'failed': 'FromSiteName'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'from_site': 'from_site'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
