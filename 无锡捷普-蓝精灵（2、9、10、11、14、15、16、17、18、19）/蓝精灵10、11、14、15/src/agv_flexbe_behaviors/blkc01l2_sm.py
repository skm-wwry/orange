#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.do_backward1m_sm import do_backward1mSM
from agv_flexbe_behaviors.do_forward1m_sm import do_forward1mSM
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.shelf_docking_sm import shelf_dockingSM
from agv_flexbe_behaviors.turn_left_sm import turn_leftSM
from agv_flexbe_behaviors.turn_right_sm import turn_rightSM
from agv_flexbe_states.alert_loop_stop import AlertLoopStop
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.wait_time import WaitTime
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 07 2020
@author: skm
'''
class BLKC01l2SM(Behavior):
	'''
	blkco1
	'''


	def __init__(self):
		super(BLKC01l2SM, self).__init__()
		self.name = 'BLKC01l2'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(do_backward1mSM, 'do_backward1m')
		self.add_behavior(do_backward1mSM, 'do_backward1m_2')
		self.add_behavior(do_forward1mSM, 'do_forward1m')
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_dumpSM, 'lift_dump_2')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(lift_loadSM, 'lift_load_2')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(shelf_dockingSM, 'shelf_docking_2')
		self.add_behavior(turn_leftSM, 'turn_left')
		self.add_behavior(turn_leftSM, 'turn_left_2')
		self.add_behavior(turn_rightSM, 'turn_right')
		self.add_behavior(turn_rightSM, 'turn_right_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:33 y:740, x:33 y:440
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:75 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turn_left_2', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1091 y:724
			OperatableStateMachine.add('blue10_beginDown',
										SiteNavigation(site_name="beginDown"),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'log8', 'failed': 'log8'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:396 y:424
			OperatableStateMachine.add('blue10_home',
										SiteNavigation(site_name="blue10_home"),
										transitions={'arrived': 'do_backward1m_2', 'canceled': 'log11', 'failed': 'log11'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:125 y:721
			OperatableStateMachine.add('do_backward1m',
										self.use_behavior(do_backward1mSM, 'do_backward1m'),
										transitions={'finished': 'finished', 'failed': 'log10'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:125 y:421
			OperatableStateMachine.add('do_backward1m_2',
										self.use_behavior(do_backward1mSM, 'do_backward1m_2'),
										transitions={'finished': 'failed', 'failed': 'log12'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1275 y:21
			OperatableStateMachine.add('do_forward1m',
										self.use_behavior(do_forward1mSM, 'do_forward1m'),
										transitions={'finished': 'playblkc01l1', 'failed': 'log5'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:875 y:21
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turn_right'},
										autonomy={'finished': Autonomy.Inherit})

			# x:775 y:721
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turn_left'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:21
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc01l2Dwon'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1275 y:721
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'blue10_beginDown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:107 y:124
			OperatableStateMachine.add('log',
										LogState(text="timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:157 y:624
			OperatableStateMachine.add('log10',
										LogState(text="dobackward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:407 y:324
			OperatableStateMachine.add('log11',
										LogState(text="home canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blue10_home'},
										autonomy={'done': Autonomy.Off})

			# x:157 y:324
			OperatableStateMachine.add('log12',
										LogState(text="do_backward_60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:707 y:124
			OperatableStateMachine.add('log3',
										LogState(text="blkc01l1 canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc01l2Dwon'},
										autonomy={'done': Autonomy.Off})

			# x:1507 y:24
			OperatableStateMachine.add('log5',
										LogState(text="do_forward_60 canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'playblkc01l1'},
										autonomy={'done': Autonomy.Off})

			# x:807 y:424
			OperatableStateMachine.add('log6',
										LogState(text="shelf_docking failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'blue10_home'},
										autonomy={'done': Autonomy.Off})

			# x:1107 y:624
			OperatableStateMachine.add('log8',
										LogState(text="begindown cancled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blue10_beginDown'},
										autonomy={'done': Autonomy.Off})

			# x:1296 y:124
			OperatableStateMachine.add('playblkc01l1',
										AlertPlay(sound_id=52, mode="loop", wait_time=5, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:1275 y:421
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turn_right_2', 'failed': 'log6'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1296 y:324
			OperatableStateMachine.add('stopblkc01l1',
										AlertLoopStop(),
										transitions={'done': 'shelf_docking_2'},
										autonomy={'done': Autonomy.Off})

			# x:375 y:721
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'turn_left'),
										transitions={'finished': 'do_backward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:275 y:21
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'turn_left_2'),
										transitions={'finished': 'lift_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1075 y:21
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'turn_right'),
										transitions={'finished': 'do_forward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1275 y:571
			OperatableStateMachine.add('turn_right_2',
										self.use_behavior(turn_rightSM, 'turn_right_2'),
										transitions={'finished': 'lift_load_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1296 y:224
			OperatableStateMachine.add('wait30s',
										WaitTime(wait_time=30),
										transitions={'done': 'stopblkc01l1'},
										autonomy={'done': Autonomy.Off})

			# x:696 y:24
			OperatableStateMachine.add('blkc01l2Dwon',
										SiteNavigation(site_name="blkc01l2Dwon"),
										transitions={'arrived': 'lift_dump', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
