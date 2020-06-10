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
from agv_flexbe_states.alert_loop_stop import AlertLoopStop
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.turn_left import TurnLeft
from agv_flexbe_states.turn_right import TurnRight
from agv_flexbe_states.wait_time import WaitTime
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 07 2020
@author: skm
'''
class BLKC04l3SM(Behavior):
	'''
	blkc04
	'''


	def __init__(self):
		super(BLKC04l3SM, self).__init__()
		self.name = 'BLKC04l3'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_dumpSM, 'lift_dump_2')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(lift_loadSM, 'lift_load_2')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(shelf_dockingSM, 'shelf_docking_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:936 y:133, x:767 y:330
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:76 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turnRight', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1100 y:597
			OperatableStateMachine.add('blkc04up',
										SiteNavigation(site_name=blkc04up),
										transitions={'arrived': 'shelf_docking_2', 'canceled': 'log6', 'failed': 'log6'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:891 y:28
			OperatableStateMachine.add('do_backward_100',
										HomingControl(target_frame="base_link", target_x=-1.0, target_y=0, target_yaw=0),
										transitions={'succeeded': 'finished', 'failed': 'log11'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:80 y:604
			OperatableStateMachine.add('do_forward_60',
										HomingControl(target_frame="base_link", target_x=0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'playblkc04l3', 'failed': 'log5'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:729 y:398
			OperatableStateMachine.add('dobackward60',
										HomingControl(target_frame="base_link", target_x=-0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'failed', 'failed': 'log13'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1094 y:203
			OperatableStateMachine.add('enddown',
										SiteNavigation(site_name=home),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'log9', 'failed': 'log9'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:730 y:498
			OperatableStateMachine.add('home',
										SiteNavigation(site_name=home),
										transitions={'arrived': 'dobackward60', 'canceled': 'log12', 'failed': 'log12'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:78 y:390
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turnleft'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1092 y:115
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turnright3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:74 y:202
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc04down'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1094 y:295
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'enddown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:295 y:23
			OperatableStateMachine.add('log',
										LogState(text="shelf_docking failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:1307 y:26
			OperatableStateMachine.add('log10',
										LogState(text="turnright3 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnright3'},
										autonomy={'done': Autonomy.Off})

			# x:723 y:29
			OperatableStateMachine.add('log11',
										LogState(text="dobackward_100 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_backward_100'},
										autonomy={'done': Autonomy.Off})

			# x:513 y:500
			OperatableStateMachine.add('log12',
										LogState(text="home failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:510 y:396
			OperatableStateMachine.add('log13',
										LogState(text="dobackward60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'dobackward60'},
										autonomy={'done': Autonomy.Off})

			# x:291 y:298
			OperatableStateMachine.add('log3',
										LogState(text="blkc04down canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc04down'},
										autonomy={'done': Autonomy.Off})

			# x:291 y:393
			OperatableStateMachine.add('log4',
										LogState(text="turnleft failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnleft'},
										autonomy={'done': Autonomy.Off})

			# x:293 y:497
			OperatableStateMachine.add('log5',
										LogState(text="do_forward_60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_forward_60'},
										autonomy={'done': Autonomy.Off})

			# x:1317 y:592
			OperatableStateMachine.add('log6',
										LogState(text="blkc02up canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc04up'},
										autonomy={'done': Autonomy.Off})

			# x:898 y:497
			OperatableStateMachine.add('log7',
										LogState(text="shelf_docking_2 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:1310 y:399
			OperatableStateMachine.add('log8',
										LogState(text="turnright failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnRight2'},
										autonomy={'done': Autonomy.Off})

			# x:1306 y:198
			OperatableStateMachine.add('log9',
										LogState(text="enddown failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'enddown'},
										autonomy={'done': Autonomy.Off})

			# x:294 y:112
			OperatableStateMachine.add('log_2',
										LogState(text="turnright failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnRight'},
										autonomy={'done': Autonomy.Off})

			# x:513 y:600
			OperatableStateMachine.add('playblkc04l3',
										AlertPlay(sound_id=71, mode="loop", wait_time=3, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:1098 y:495
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turnRight2', 'failed': 'log7'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:898 y:597
			OperatableStateMachine.add('stopblkc04l3',
										AlertLoopStop(),
										transitions={'done': 'blkc04up'},
										autonomy={'done': Autonomy.Off})

			# x:76 y:115
			OperatableStateMachine.add('turnRight',
										TurnRight(),
										transitions={'succeeded': 'lift_load', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1097 y:397
			OperatableStateMachine.add('turnRight2',
										TurnRight(),
										transitions={'succeeded': 'lift_load_2', 'failed': 'log8'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:80 y:496
			OperatableStateMachine.add('turnleft',
										TurnLeft(),
										transitions={'succeeded': 'do_forward_60', 'failed': 'log4'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1091 y:26
			OperatableStateMachine.add('turnright3',
										TurnRight(),
										transitions={'succeeded': 'do_backward_100', 'failed': 'log10'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:730 y:599
			OperatableStateMachine.add('wait30s',
										WaitTime(wait_time=30),
										transitions={'done': 'stopblkc04l3'},
										autonomy={'done': Autonomy.Off})

			# x:76 y:299
			OperatableStateMachine.add('blkc04down',
										SiteNavigation(site_name=blkc04down),
										transitions={'arrived': 'lift_dump', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
