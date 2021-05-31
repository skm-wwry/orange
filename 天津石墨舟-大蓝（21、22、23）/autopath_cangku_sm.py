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
from agv_flexbe_behaviors.close_sm import closeSM
from agv_flexbe_behaviors.do_backward_sm import do_backwardSM
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.open_sm import openSM
from agv_flexbe_behaviors.rotate_dump_sm import rotate_dumpSM
from agv_flexbe_behaviors.rotate_home_sm import rotate_homeSM
from agv_flexbe_behaviors.rotate_load_sm import rotate_loadSM
from agv_flexbe_behaviors.turn_left_sm import turn_leftSM
from agv_flexbe_behaviors.turn_right_sm import turn_rightSM
from agv_flexbe_states.site_navigation import SiteNavigation
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Apr 19 2021
@author: sunkm
'''
class AutoPathcangkuSM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(AutoPathcangkuSM, self).__init__()
		self.name = 'AutoPath-cangku'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(apriltag_dockingSM, 'apriltag_docking')
		self.add_behavior(apriltag_dockingSM, 'apriltag_docking_2')
		self.add_behavior(apriltag_dockingSM, 'apriltag_docking_3')
		self.add_behavior(apriltag_dockingSM, 'apriltag_docking_4')
		self.add_behavior(closeSM, 'close')
		self.add_behavior(closeSM, 'close_2')
		self.add_behavior(do_backwardSM, 'do_backward')
		self.add_behavior(do_backwardSM, 'do_backward_2')
		self.add_behavior(do_backwardSM, 'do_backward_3')
		self.add_behavior(do_backwardSM, 'do_backward_4')
		self.add_behavior(do_backwardSM, 'do_backward_5')
		self.add_behavior(do_backwardSM, 'do_backward_6')
		self.add_behavior(do_backwardSM, 'do_backward_7')
		self.add_behavior(do_backwardSM, 'do_backward_8')
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_dumpSM, 'lift_dump_2')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(lift_loadSM, 'lift_load_2')
		self.add_behavior(openSM, 'open')
		self.add_behavior(openSM, 'open_2')
		self.add_behavior(rotate_dumpSM, 'rotate_dump')
		self.add_behavior(rotate_dumpSM, 'rotate_dump_2')
		self.add_behavior(rotate_homeSM, 'rotate_home')
		self.add_behavior(rotate_homeSM, 'rotate_home_2')
		self.add_behavior(rotate_homeSM, 'rotate_home_3')
		self.add_behavior(rotate_loadSM, 'rotate_load')
		self.add_behavior(turn_leftSM, 'turn_left')
		self.add_behavior(turn_leftSM, 'turn_left_2')
		self.add_behavior(turn_leftSM, 'turn_left_3')
		self.add_behavior(turn_rightSM, 'turn_right')
		self.add_behavior(turn_rightSM, 'turn_right_2')
		self.add_behavior(turn_rightSM, 'turn_right_3')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:533 y:540
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:146 y:24
			OperatableStateMachine.add('cangku1',
										SiteNavigation(site_name="cangku1"),
										transitions={'arrived': 'turn_left', 'canceled': 'cangku1log', 'failed': 'cangku1log'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:125 y:921
			OperatableStateMachine.add('apriltag_docking_2',
										self.use_behavior(apriltag_dockingSM, 'apriltag_docking_2'),
										transitions={'finished': 'close', 'failed': 'do_backward_6'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:725 y:821
			OperatableStateMachine.add('apriltag_docking_3',
										self.use_behavior(apriltag_dockingSM, 'apriltag_docking_3'),
										transitions={'finished': 'lift_load_2', 'failed': 'do_backward_7'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:725 y:121
			OperatableStateMachine.add('apriltag_docking_4',
										self.use_behavior(apriltag_dockingSM, 'apriltag_docking_4'),
										transitions={'finished': 'close_2', 'failed': 'do_backward_8'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:746 y:324
			OperatableStateMachine.add('cangku1-1',
										SiteNavigation(site_name="cangku1"),
										transitions={'arrived': 'turn_left_3', 'canceled': 'cangku1-1log', 'failed': 'cangku1-1log'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:954 y:324
			OperatableStateMachine.add('cangku1-1log',
										LogState(text="failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'cangku1-1'},
										autonomy={'done': Autonomy.Off})

			# x:357 y:24
			OperatableStateMachine.add('cangku1log',
										LogState(text="failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'cangku1'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:724
			OperatableStateMachine.add('cangku2',
										SiteNavigation(site_name="cangku2"),
										transitions={'arrived': 'turn_right_2', 'canceled': 'cangku2log', 'failed': 'cangku2log'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:7 y:724
			OperatableStateMachine.add('cangku2log',
										LogState(text="filed", severity=Logger.REPORT_HINT),
										transitions={'done': 'cangku2'},
										autonomy={'done': Autonomy.Off})

			# x:325 y:921
			OperatableStateMachine.add('close',
										self.use_behavior(closeSM, 'close'),
										transitions={'finished': 'lift_dump'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:21
			OperatableStateMachine.add('close_2',
										self.use_behavior(closeSM, 'close_2'),
										transitions={'finished': 'lift_dump_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:521
			OperatableStateMachine.add('do_backward',
										self.use_behavior(do_backwardSM, 'do_backward'),
										transitions={'finished': 'turn_right'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:921
			OperatableStateMachine.add('do_backward_2',
										self.use_behavior(do_backwardSM, 'do_backward_2'),
										transitions={'finished': 'apriltag_docking_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:521
			OperatableStateMachine.add('do_backward_3',
										self.use_behavior(do_backwardSM, 'do_backward_3'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:121
			OperatableStateMachine.add('do_backward_4',
										self.use_behavior(do_backwardSM, 'do_backward_4'),
										transitions={'finished': 'turn_right_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:521
			OperatableStateMachine.add('do_backward_5',
										self.use_behavior(do_backwardSM, 'do_backward_5'),
										transitions={'finished': 'apriltag_docking'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:1021
			OperatableStateMachine.add('do_backward_6',
										self.use_behavior(do_backwardSM, 'do_backward_6'),
										transitions={'finished': 'apriltag_docking_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:925 y:821
			OperatableStateMachine.add('do_backward_7',
										self.use_behavior(do_backwardSM, 'do_backward_7'),
										transitions={'finished': 'apriltag_docking_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:925 y:121
			OperatableStateMachine.add('do_backward_8',
										self.use_behavior(do_backwardSM, 'do_backward_8'),
										transitions={'finished': 'apriltag_docking_4'},
										autonomy={'finished': Autonomy.Inherit})

			# x:525 y:921
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'do_backward_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:21
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'do_backward_4'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:321
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'open'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:721
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'open_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:421
			OperatableStateMachine.add('open',
										self.use_behavior(openSM, 'open'),
										transitions={'finished': 'do_backward'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:621
			OperatableStateMachine.add('open_2',
										self.use_behavior(openSM, 'open_2'),
										transitions={'finished': 'do_backward_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:421
			OperatableStateMachine.add('rotate_dump',
										self.use_behavior(rotate_dumpSM, 'rotate_dump'),
										transitions={'finished': 'apriltag_docking'},
										autonomy={'finished': Autonomy.Inherit})

			# x:925 y:221
			OperatableStateMachine.add('rotate_dump_2',
										self.use_behavior(rotate_dumpSM, 'rotate_dump_2'),
										transitions={'finished': 'apriltag_docking_4'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:621
			OperatableStateMachine.add('rotate_home',
										self.use_behavior(rotate_homeSM, 'rotate_home'),
										transitions={'finished': 'cangku2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:925 y:421
			OperatableStateMachine.add('rotate_home_2',
										self.use_behavior(rotate_homeSM, 'rotate_home_2'),
										transitions={'finished': 'cangku1-1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:321
			OperatableStateMachine.add('rotate_home_3',
										self.use_behavior(rotate_homeSM, 'rotate_home_3'),
										transitions={'finished': 'cangku1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:821
			OperatableStateMachine.add('rotate_load',
										self.use_behavior(rotate_loadSM, 'rotate_load'),
										transitions={'finished': 'apriltag_docking_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:121
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'turn_left'),
										transitions={'finished': 'rotate_dump'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:421
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'turn_left_2'),
										transitions={'finished': 'rotate_home_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:725 y:221
			OperatableStateMachine.add('turn_left_3',
										self.use_behavior(turn_leftSM, 'turn_left_3'),
										transitions={'finished': 'rotate_dump_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:621
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'turn_right'),
										transitions={'finished': 'rotate_home'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:821
			OperatableStateMachine.add('turn_right_2',
										self.use_behavior(turn_rightSM, 'turn_right_2'),
										transitions={'finished': 'rotate_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:221
			OperatableStateMachine.add('turn_right_3',
										self.use_behavior(turn_rightSM, 'turn_right_3'),
										transitions={'finished': 'rotate_home_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:221
			OperatableStateMachine.add('apriltag_docking',
										self.use_behavior(apriltag_dockingSM, 'apriltag_docking'),
										transitions={'finished': 'lift_load', 'failed': 'do_backward_5'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
