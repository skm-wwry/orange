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
from agv_flexbe_states.do_forward import DoForward
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.navigation import Navigation
from agv_flexbe_states.turn_left import TurnLeft
from agv_flexbe_states.turn_right import TurnRight
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 07 2020
@author: skm
'''
class BLKC05l3SM(Behavior):
	'''
	20200507
	'''


	def __init__(self):
		super(BLKC05l3SM, self).__init__()
		self.name = 'BLKC05l3'

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
		# x:29 y:345, x:100 y:344
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:256 y:35
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turnRight', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:940 y:32
			OperatableStateMachine.add('blkc01l6Dwon',
										Navigation(position_x=31.375, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'lift_dump', 'failed': 'log', 'canceled': 'log5'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1366 y:142
			OperatableStateMachine.add('do_forward_60',
										HomingControl(target_frame="base_link", target_x=0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'shelf_docking_2', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:49 y:610
			OperatableStateMachine.add('dobackward60',
										HomingControl(target_frame="base_link", target_x=-0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'finished', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:544 y:601
			OperatableStateMachine.add('doforword100',
										DoForward(),
										transitions={'succeeded': 'home', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:302 y:603
			OperatableStateMachine.add('home',
										Navigation(position_x=82.251, position_y=18.098, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'dobackward60', 'failed': 'log_2', 'canceled': 'log7'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1117 y:27
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turnRight1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1052 y:600
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turnLeft'},
										autonomy={'finished': Autonomy.Inherit})

			# x:695 y:35
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc01l6Dwon'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1330 y:489
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'beginDown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:621 y:211
			OperatableStateMachine.add('log',
										LogState(text="timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:625 y:303
			OperatableStateMachine.add('log3',
										LogState(text="seek failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:850 y:166
			OperatableStateMachine.add('log5',
										LogState(text="blkc01l1down canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc01l6Dwon'},
										autonomy={'done': Autonomy.Off})

			# x:1149 y:434
			OperatableStateMachine.add('log6',
										LogState(text="begindown cancled", severity=Logger.REPORT_HINT),
										transitions={'done': 'beginDown'},
										autonomy={'done': Autonomy.Off})

			# x:184 y:457
			OperatableStateMachine.add('log7',
										LogState(text="home canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:624 y:385
			OperatableStateMachine.add('log_2',
										LogState(text="turn right log", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:1325 y:268
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turnRight3', 'failed': 'log3'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:785 y:603
			OperatableStateMachine.add('turnLeft',
										TurnLeft(),
										transitions={'succeeded': 'doforword100', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:499 y:38
			OperatableStateMachine.add('turnRight',
										TurnRight(),
										transitions={'succeeded': 'lift_load', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1363 y:33
			OperatableStateMachine.add('turnRight1',
										TurnRight(),
										transitions={'succeeded': 'do_forward_60', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1366 y:383
			OperatableStateMachine.add('turnRight3',
										TurnRight(),
										transitions={'succeeded': 'lift_load_2', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1365 y:607
			OperatableStateMachine.add('beginDown',
										Navigation(position_x=86, position_y=24.161, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'lift_dump_2', 'failed': 'log_2', 'canceled': 'log6'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
