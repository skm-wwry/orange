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
class BLKC06l2SM(Behavior):
	'''
	blkc06
	'''


	def __init__(self):
		super(BLKC06l2SM, self).__init__()
		self.name = 'BLKC06l2'

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
		self.add_behavior(turn_leftSM, 'turn_left_3')
		self.add_behavior(turn_rightSM, 'turn_right')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:33 y:790, x:33 y:540
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:125 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turn_left', 'failed': 'log'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1346 y:124
			OperatableStateMachine.add('blkc02play',
										AlertPlay(sound_id=61, mode="loop", wait_time=5, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:1346 y:324
			OperatableStateMachine.add('blkc02stop',
										AlertLoopStop(),
										transitions={'done': 'blkc06up'},
										autonomy={'done': Autonomy.Off})

			# x:746 y:24
			OperatableStateMachine.add('blkc06Dwon',
										SiteNavigation(site_name="blkc06Dwon"),
										transitions={'arrived': 'lift_dump', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1346 y:424
			OperatableStateMachine.add('blkc06up',
										SiteNavigation(site_name="blkc06up"),
										transitions={'arrived': 'shelf_docking_2', 'canceled': 'log6', 'failed': 'log6'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:596 y:524
			OperatableStateMachine.add('blue10_home',
										SiteNavigation(site_name="blue10_home"),
										transitions={'arrived': 'do_backward1m_2', 'canceled': 'log12', 'failed': 'log12'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:225 y:771
			OperatableStateMachine.add('do_backward1m',
										self.use_behavior(do_backward1mSM, 'do_backward1m'),
										transitions={'finished': 'finished', 'failed': 'log11'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:225 y:521
			OperatableStateMachine.add('do_backward1m_2',
										self.use_behavior(do_backward1mSM, 'do_backward1m_2'),
										transitions={'finished': 'failed', 'failed': 'log13'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1325 y:21
			OperatableStateMachine.add('do_forward1m',
										self.use_behavior(do_forward1mSM, 'do_forward1m'),
										transitions={'finished': 'blkc02play', 'failed': 'log5'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:925 y:21
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:875 y:771
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'lift_dump_2'),
										transitions={'finished': 'turn_left_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:525 y:21
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'blkc06Dwon'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1325 y:771
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'lift_load_2'),
										transitions={'finished': 'beginDown'},
										autonomy={'finished': Autonomy.Inherit})

			# x:157 y:124
			OperatableStateMachine.add('log',
										LogState(text="shelf_docking failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:257 y:674
			OperatableStateMachine.add('log11',
										LogState(text="dobackward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:607 y:424
			OperatableStateMachine.add('log12',
										LogState(text="home failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'blue10_home'},
										autonomy={'done': Autonomy.Off})

			# x:257 y:424
			OperatableStateMachine.add('log13',
										LogState(text="dobackward60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:757 y:124
			OperatableStateMachine.add('log3',
										LogState(text="blkc02down canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc06Dwon'},
										autonomy={'done': Autonomy.Off})

			# x:1557 y:24
			OperatableStateMachine.add('log5',
										LogState(text="do_forward_60 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_forward1m'},
										autonomy={'done': Autonomy.Off})

			# x:1557 y:424
			OperatableStateMachine.add('log6',
										LogState(text="blkc02up canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'blkc06up'},
										autonomy={'done': Autonomy.Off})

			# x:957 y:524
			OperatableStateMachine.add('log7',
										LogState(text="shelf_docking_2 failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'blue10_home'},
										autonomy={'done': Autonomy.Off})

			# x:1157 y:674
			OperatableStateMachine.add('log9',
										LogState(text="begindown failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'beginDown'},
										autonomy={'done': Autonomy.Off})

			# x:1325 y:521
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'shelf_docking_2'),
										transitions={'finished': 'turn_right', 'failed': 'log7'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:325 y:21
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'turn_left'),
										transitions={'finished': 'lift_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:21
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'turn_left_2'),
										transitions={'finished': 'do_forward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:575 y:771
			OperatableStateMachine.add('turn_left_3',
										self.use_behavior(turn_leftSM, 'turn_left_3'),
										transitions={'finished': 'do_backward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1325 y:671
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'turn_right'),
										transitions={'finished': 'lift_load_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1346 y:224
			OperatableStateMachine.add('wait30s',
										WaitTime(wait_time=30),
										transitions={'done': 'blkc02stop'},
										autonomy={'done': Autonomy.Off})

			# x:1146 y:774
			OperatableStateMachine.add('beginDown',
										SiteNavigation(site_name="beginDown"),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'log9', 'failed': 'log9'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
