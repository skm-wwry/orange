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
from agv_flexbe_states.blkc_cross import BlkcCross
from agv_flexbe_states.blkc_take import BlkcTake
from agv_flexbe_states.from_where import FromWhere
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.site_transfer_from import SiteTransferFrom
from agv_flexbe_states.site_transfer_to import SiteTransferTo
from agv_flexbe_states.to_where import ToWhere
from agv_flexbe_states.wait_time import WaitTime
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
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
		self.add_behavior(do_backward1mSM, 'branch1/do_backward1m')
		self.add_behavior(do_forward1mSM, 'branch1/do_forward1m')
		self.add_behavior(lift_dumpSM, 'branch1/lift_dump')
		self.add_behavior(lift_dumpSM, 'branch1/lift_dump_2')
		self.add_behavior(lift_loadSM, 'branch1/lift_load_2')
		self.add_behavior(shelf_dockingSM, 'branch1/shelf_docking_2')
		self.add_behavior(turn_leftSM, 'branch1/turn_left_2')
		self.add_behavior(turn_rightSM, 'branch1/turn_right')
		self.add_behavior(turn_rightSM, 'branch1/turn_right_2')
		self.add_behavior(do_backward1mSM, 'branch2/do_backward1m')
		self.add_behavior(do_forward1mSM, 'branch2/do_forward1m')
		self.add_behavior(lift_dumpSM, 'branch2/lift_dump')
		self.add_behavior(lift_dumpSM, 'branch2/lift_dump_2')
		self.add_behavior(lift_loadSM, 'branch2/lift_load_2')
		self.add_behavior(shelf_dockingSM, 'branch2/shelf_docking_2')
		self.add_behavior(turn_leftSM, 'branch2/turn_left')
		self.add_behavior(turn_leftSM, 'branch2/turn_left_2')
		self.add_behavior(turn_leftSM, 'branch2/turn_left_3')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')
		self.add_behavior(turn_leftSM, 'turn_left')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1133 y:290, x:1133 y:390
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.to_site = ""
		_state_machine.userdata.des_site = ""
		_state_machine.userdata.from_site = ""

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:883 y:840, x:1033 y:240, x:1283 y:240
		_sm_branch2_0 = OperatableStateMachine(outcomes=['arrived', 'finished', 'done'], input_keys=['to_site'])

		with _sm_branch2_0:
			# x:125 y:121
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'branch2/lift_dump'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:975 y:121
			OperatableStateMachine.add('do_backward1m',
										self.use_behavior(do_backward1mSM, 'branch2/do_backward1m'),
										transitions={'finished': 'finished', 'failed': 'log4'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:125 y:321
			OperatableStateMachine.add('do_forward1m',
										self.use_behavior(do_forward1mSM, 'branch2/do_forward1m'),
										transitions={'finished': 'playMusic', 'failed': 'log1'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:596 y:824
			OperatableStateMachine.add('initial_pose',
										SiteNavigation(site_name="initial_pose"),
										transitions={'arrived': 'arrived', 'canceled': 'initial_pose', 'failed': 'initial_pose'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:575 y:221
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'branch2/lift_dump_2'),
										transitions={'finished': 'turn_left_3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:575 y:421
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'branch2/lift_load_2'),
										transitions={'finished': 'return_print'},
										autonomy={'finished': Autonomy.Inherit})

			# x:357 y:524
			OperatableStateMachine.add('log-take',
										LogState(text="navigation site take canceled or failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'ToTake'},
										autonomy={'done': Autonomy.Off})

			# x:357 y:324
			OperatableStateMachine.add('log1',
										LogState(text="do_forward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'playMusic'},
										autonomy={'done': Autonomy.Off})

			# x:607 y:724
			OperatableStateMachine.add('log2',
										LogState(text="branch2 shelf_docking timeout return home", severity=Logger.REPORT_HINT),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:807 y:324
			OperatableStateMachine.add('log3',
										LogState(text="branch2 return_print navigation failed or cancled", severity=Logger.REPORT_HINT),
										transitions={'done': 'return_print'},
										autonomy={'done': Autonomy.Off})

			# x:1257 y:124
			OperatableStateMachine.add('log4',
										LogState(text="do_backward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'done'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:424
			OperatableStateMachine.add('playMusic',
										AlertPlay(sound_id=51, mode="loop", wait_time=3, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:596 y:324
			OperatableStateMachine.add('return_print',
										SiteNavigation(site_name="return_point"),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:575 y:621
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'branch2/shelf_docking_2'),
										transitions={'finished': 'turn_left', 'failed': 'log2'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:146 y:624
			OperatableStateMachine.add('stopMusic',
										AlertLoopStop(),
										transitions={'done': 'ToTake'},
										autonomy={'done': Autonomy.Off})

			# x:575 y:521
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'branch2/turn_left'),
										transitions={'finished': 'lift_load_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:221
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'branch2/turn_left_2'),
										transitions={'finished': 'do_forward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:575 y:121
			OperatableStateMachine.add('turn_left_3',
										self.use_behavior(turn_leftSM, 'branch2/turn_left_3'),
										transitions={'finished': 'do_backward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:157 y:524
			OperatableStateMachine.add('wait30s',
										WaitState(wait_time=30),
										transitions={'done': 'stopMusic'},
										autonomy={'done': Autonomy.Off})

			# x:346 y:624
			OperatableStateMachine.add('ToTake',
										BlkcTake(),
										transitions={'arrived': 'shelf_docking_2', 'canceled': 'log-take', 'failed': 'log-take'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'to_site': 'to_site'})


		# x:933 y:240, x:833 y:840, x:1183 y:240
		_sm_branch1_1 = OperatableStateMachine(outcomes=['finished', 'arrived', 'done'])

		with _sm_branch1_1:
			# x:125 y:121
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'branch1/lift_dump'),
										transitions={'finished': 'turn_right'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:321
			OperatableStateMachine.add('do_forward1m',
										self.use_behavior(do_forward1mSM, 'branch1/do_forward1m'),
										transitions={'finished': 'playMusic', 'failed': 'log1'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:546 y:824
			OperatableStateMachine.add('initial_pose',
										SiteNavigation(site_name="initial_pose"),
										transitions={'arrived': 'arrived', 'canceled': 'log6', 'failed': 'log6'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:525 y:221
			OperatableStateMachine.add('lift_dump_2',
										self.use_behavior(lift_dumpSM, 'branch1/lift_dump_2'),
										transitions={'finished': 'turn_left_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:525 y:421
			OperatableStateMachine.add('lift_load_2',
										self.use_behavior(lift_loadSM, 'branch1/lift_load_2'),
										transitions={'finished': 'return_point'},
										autonomy={'finished': Autonomy.Inherit})

			# x:357 y:324
			OperatableStateMachine.add('log1',
										LogState(text="do_forward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'playMusic'},
										autonomy={'done': Autonomy.Off})

			# x:557 y:724
			OperatableStateMachine.add('log2',
										LogState(text="branch1 shelf_docking timeout return home", severity=Logger.REPORT_HINT),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:757 y:324
			OperatableStateMachine.add('log3',
										LogState(text="branch1 return_print navigation failed or cancled", severity=Logger.REPORT_HINT),
										transitions={'done': 'return_point'},
										autonomy={'done': Autonomy.Off})

			# x:1157 y:124
			OperatableStateMachine.add('log4',
										LogState(text="dobackward failed", severity=Logger.REPORT_HINT),
										transitions={'done': 'done'},
										autonomy={'done': Autonomy.Off})

			# x:357 y:824
			OperatableStateMachine.add('log6',
										LogState(text="initial_pose navigation canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:424
			OperatableStateMachine.add('playMusic',
										AlertPlay(sound_id=51, mode="loop", wait_time=5, single_time=3),
										transitions={'done': 'wait30s'},
										autonomy={'done': Autonomy.Off})

			# x:546 y:324
			OperatableStateMachine.add('return_point',
										SiteNavigation(site_name="return_point"),
										transitions={'arrived': 'lift_dump_2', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:525 y:621
			OperatableStateMachine.add('shelf_docking_2',
										self.use_behavior(shelf_dockingSM, 'branch1/shelf_docking_2'),
										transitions={'finished': 'turn_right_2', 'failed': 'log2'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:146 y:624
			OperatableStateMachine.add('stopMusic',
										AlertLoopStop(),
										transitions={'done': 'shelf_docking_2'},
										autonomy={'done': Autonomy.Off})

			# x:525 y:121
			OperatableStateMachine.add('turn_left_2',
										self.use_behavior(turn_leftSM, 'branch1/turn_left_2'),
										transitions={'finished': 'do_backward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:125 y:221
			OperatableStateMachine.add('turn_right',
										self.use_behavior(turn_rightSM, 'branch1/turn_right'),
										transitions={'finished': 'do_forward1m'},
										autonomy={'finished': Autonomy.Inherit})

			# x:525 y:521
			OperatableStateMachine.add('turn_right_2',
										self.use_behavior(turn_rightSM, 'branch1/turn_right_2'),
										transitions={'finished': 'lift_load_2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:146 y:524
			OperatableStateMachine.add('wait30s',
										WaitTime(wait_time=30),
										transitions={'done': 'stopMusic'},
										autonomy={'done': Autonomy.Off})

			# x:875 y:121
			OperatableStateMachine.add('do_backward1m',
										self.use_behavior(do_backward1mSM, 'branch1/do_backward1m'),
										transitions={'finished': 'finished', 'failed': 'log4'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:96 y:324
			OperatableStateMachine.add('ToWhere',
										ToWhere(),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:96 y:224
			OperatableStateMachine.add('FromWhere',
										FromWhere(),
										transitions={'done': 'ToWhere'},
										autonomy={'done': Autonomy.Off},
										remapping={'from_site': 'from_site'})

			# x:696 y:324
			OperatableStateMachine.add('Judge',
										BlkcCross(),
										transitions={'1_5': 'branch1', '2_3_4_6': 'branch2'},
										autonomy={'1_5': Autonomy.Off, '2_3_4_6': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:496 y:324
			OperatableStateMachine.add('ToSiteName',
										SiteTransferTo(),
										transitions={'arrived': 'Judge', 'canceled': 'log3', 'failed': 'log3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:893 y:221
			OperatableStateMachine.add('branch1',
										_sm_branch1_1,
										transitions={'finished': 'finished', 'arrived': 'failed', 'done': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'arrived': Autonomy.Inherit, 'done': Autonomy.Inherit})

			# x:893 y:421
			OperatableStateMachine.add('branch2',
										_sm_branch2_0,
										transitions={'arrived': 'failed', 'finished': 'finished', 'done': 'finished'},
										autonomy={'arrived': Autonomy.Inherit, 'finished': Autonomy.Inherit, 'done': Autonomy.Inherit},
										remapping={'to_site': 'to_site'})

			# x:275 y:421
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'ToSiteName'},
										autonomy={'finished': Autonomy.Inherit})

			# x:307 y:124
			OperatableStateMachine.add('log1',
										LogState(text="shelfDocking failed timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:107 y:524
			OperatableStateMachine.add('log2',
										LogState(text="ToSite path failed or canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'FromSiteName'},
										autonomy={'done': Autonomy.Off})

			# x:507 y:224
			OperatableStateMachine.add('log3',
										LogState(text="SiteTransterT0 failed or canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'ToSiteName'},
										autonomy={'done': Autonomy.Off})

			# x:275 y:221
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'turn_left', 'failed': 'log1'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:275 y:321
			OperatableStateMachine.add('turn_left',
										self.use_behavior(turn_leftSM, 'turn_left'),
										transitions={'finished': 'lift_load'},
										autonomy={'finished': Autonomy.Inherit})

			# x:96 y:424
			OperatableStateMachine.add('FromSiteName',
										SiteTransferFrom(),
										transitions={'arrived': 'shelf_docking', 'canceled': 'log2', 'failed': 'log2'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'from_site': 'from_site'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
