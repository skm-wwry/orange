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
from agv_flexbe_states.do_backward import DoBackward
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.navigation import Navigation
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
class BLKC01l3SM(Behavior):
	'''
	blkco1
	'''


	def __init__(self):
		super(BLKC01l3SM, self).__init__()
		self.name = 'BLKC01l3'

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
		# x:680 y:33, x:1275 y:410
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:74 y:20
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turnright', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:75 y:324
			OperatableStateMachine.add('blkc01l3Dwon',
										Navigation(position_x=41.446, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'lift_dump', 'failed': 'log3', 'canceled': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1198 y:511
			OperatableStateMachine.add('do_backward_60',
										HomingControl(target_frame="base_link", target_x=-0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'failed', 'failed': 'log12'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:75 y:605
			OperatableStateMachine.add('do_forward_60',
										HomingControl(target_frame="base_link", target_x=0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'playblkc01l3', 'failed': 'log5'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:839 y:29
			OperatableStateMachine.add('dobackward',
										DoBackward(),
										transitions={'succeeded': 'finished', 'failed': 'log10'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1200 y:603
			OperatableStateMachine.add('home',
										Navigation(position_x=82.310, position_y=18.098, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'do_backward_60', 'failed': 'log11', 'canceled': 'log11'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:76 y:415
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turnright1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:840 y:221
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turnright3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:74 y:220
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc01l3Dwon'},
										autonomy={'finished': Autonomy.Inherit})

			# x:842 y:410
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'beginDown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:281 y:21
			OperatableStateMachine.add('log',
										LogState(text="timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:1046 y:30
			OperatableStateMachine.add('log10',
										LogState(text="dobackward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'dobackward'},
										autonomy={'done': Autonomy.Off})

			# x:1405 y:603
			OperatableStateMachine.add('log11',
										LogState(text="home canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:1405 y:513
			OperatableStateMachine.add('log12',
										LogState(text="do_backward_60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_backward_60'},
										autonomy={'done': Autonomy.Off})

			# x:286 y:326
			OperatableStateMachine.add('log3',
										LogState(text="blkc01l3 canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc01l3Dwon'},
										autonomy={'done': Autonomy.Off})

			# x:287 y:418
			OperatableStateMachine.add('log4',
										LogState(text="turnright1 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnright1'},
										autonomy={'done': Autonomy.Off})

			# x:289 y:505
			OperatableStateMachine.add('log5',
										LogState(text="do_forward_60 canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_forward_60'},
										autonomy={'done': Autonomy.Off})

			# x:1050 y:605
			OperatableStateMachine.add('log6',
										LogState(text="shelf_docking failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:1049 y:511
			OperatableStateMachine.add('log7',
										LogState(text="turnright2 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnright2'},
										autonomy={'done': Autonomy.Off})

			# x:1047 y:318
			OperatableStateMachine.add('log8',
										LogState(text="begindown cancled", severity=Logger.REPORT_HINT),
										transitions={'done': 'beginDown'},
										autonomy={'done': Autonomy.Off})

			# x:1044 y:127
			OperatableStateMachine.add('log9',
										LogState(text="turnright failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnright3'},
										autonomy={'done': Autonomy.Off})

			# x:283 y:126
			OperatableStateMachine.add('log_2',
										LogState(text="turnright log", severity=Logger.REPORT_HINT),
										transitions={'done': 'turnright'},
										autonomy={'done': Autonomy.Off})

			# x:288 y:605
			OperatableStateMachine.add('playblkc01l3',
										AlertPlay(sound_id=53, mode="loop", wait_time=5, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:843 y:599
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turnright2', 'failed': 'log6'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:665 y:606
			OperatableStateMachine.add('stopblkc01l3',
										AlertLoopStop(),
										transitions={'done': 'shelf_docking_2'},
										autonomy={'done': Autonomy.Off})

			# x:74 y:126
			OperatableStateMachine.add('turnright',
										TurnRight(),
										transitions={'succeeded': 'lift_load', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:76 y:508
			OperatableStateMachine.add('turnright1',
										TurnRight(),
										transitions={'succeeded': 'do_forward_60', 'failed': 'log4'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:843 y:511
			OperatableStateMachine.add('turnright2',
										TurnRight(),
										transitions={'succeeded': 'lift_load_2', 'failed': 'log7'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:840 y:125
			OperatableStateMachine.add('turnright3',
										TurnRight(),
										transitions={'succeeded': 'dobackward', 'failed': 'log9'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:479 y:606
			OperatableStateMachine.add('wait30s',
										WaitTime(wait_time=30),
										transitions={'done': 'stopblkc01l3'},
										autonomy={'done': Autonomy.Off})

			# x:840 y:318
			OperatableStateMachine.add('beginDown',
										Navigation(position_x=86, position_y=24.264, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'lift_dump_2', 'failed': 'log8', 'canceled': 'log8'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
