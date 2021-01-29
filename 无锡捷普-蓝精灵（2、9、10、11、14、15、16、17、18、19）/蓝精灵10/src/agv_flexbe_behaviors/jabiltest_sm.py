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
class jabilTestSM(Behavior):
	'''
	20200507
	'''


	def __init__(self):
		super(jabilTestSM, self).__init__()
		self.name = 'jabilTest'

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
			# x:35 y:39
			OperatableStateMachine.add('upsite001',
										Navigation(position_x=86.781, position_y=26.003, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'arrived': 'shelf_docking', 'failed': 'log3', 'canceled': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:956 y:32
			OperatableStateMachine.add('blkc01l1Dwon',
										Navigation(position_x=46.945, position_y=173.659, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'arrived': 'lift_dump', 'failed': 'log3', 'canceled': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1156 y:297
			OperatableStateMachine.add('blkc01l1up',
										Navigation(position_x=45.339, position_y=174.662, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'shelf_docking_2', 'failed': 'log3', 'canceled': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1157 y:216
			OperatableStateMachine.add('doforward110',
										DoForward(),
										transitions={'succeeded': 'blkc01l1up', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:284 y:536
			OperatableStateMachine.add('doforword100',
										DoForward(),
										transitions={'succeeded': 'home', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:92 y:536
			OperatableStateMachine.add('home',
										Navigation(position_x=3.31, position_y=4.41, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id='map'),
										transitions={'arrived': 'finished', 'failed': 'log3', 'canceled': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:1123 y:51
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turnRight1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:678 y:530
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turnLeft'},
										autonomy={'finished': Autonomy.Inherit})

			# x:728 y:41
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc01l1Dwon'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1115 y:532
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'beginDown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:407 y:206
			OperatableStateMachine.add('log',
										LogState(text="timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:424 y:350
			OperatableStateMachine.add('log3',
										LogState(text="seek failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:592 y:203
			OperatableStateMachine.add('log_2',
										LogState(text="turn right log", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:256 y:35
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turnRight', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1123 y:386
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turnRight3', 'failed': 'log3'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:482 y:536
			OperatableStateMachine.add('turnLeft',
										TurnLeft(),
										transitions={'succeeded': 'doforword100', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:499 y:38
			OperatableStateMachine.add('turnRight',
										TurnRight(),
										transitions={'succeeded': 'lift_load', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1157 y:127
			OperatableStateMachine.add('turnRight1',
										TurnRight(),
										transitions={'succeeded': 'doforward110', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1157 y:459
			OperatableStateMachine.add('turnRight3',
										TurnRight(),
										transitions={'succeeded': 'lift_load_2', 'failed': 'log3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:938 y:529
			OperatableStateMachine.add('beginDown',
										Navigation(position_x=2.21, position_y=3.31, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id='map'),
										transitions={'arrived': 'lift_dump_2', 'failed': 'log3', 'canceled': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
