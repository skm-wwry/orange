#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.do_forward_sm import do_forwardSM
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.music_sm import musicSM
from agv_flexbe_behaviors.shelf_docking_sm import shelf_dockingSM
from agv_flexbe_states.blkc_cross import BlkcCross
from agv_flexbe_states.from_where import FromWhere
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.site_transfer_from import SiteTransferFrom
from agv_flexbe_states.site_transfer_to import SiteTransferTo
from agv_flexbe_states.to_where import ToWhere
from flexbe_states.log_state import LogState
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
		self.add_behavior(do_forwardSM, 'branch1/do_forward')
		self.add_behavior(lift_dumpSM, 'branch1/lift_dump')
		self.add_behavior(musicSM, 'branch1/music')
		self.add_behavior(musicSM, 'branch1/music_2')
		self.add_behavior(musicSM, 'branch1/music_3')
		self.add_behavior(musicSM, 'branch1/music_4')
		self.add_behavior(musicSM, 'branch1/music_5')
		self.add_behavior(musicSM, 'branch1/music_6')
		self.add_behavior(musicSM, 'branch1/music_7')
		self.add_behavior(musicSM, 'branch1/music_8')
		self.add_behavior(musicSM, 'branch1/music_9')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1183 y:340, x:1183 y:490
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.to_site = ""
		_state_machine.userdata.des_site = ""
		_state_machine.userdata.from_site = ""

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:1083 y:440
		_sm_branch1_0 = OperatableStateMachine(outcomes=['arrived'], output_keys=['to_site'])

		with _sm_branch1_0:
			# x:196 y:74
			OperatableStateMachine.add('A1',
										SiteNavigation(site_name="A1"),
										transitions={'arrived': 'music', 'canceled': 'A1', 'failed': 'A1'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:174
			OperatableStateMachine.add('A2',
										SiteNavigation(site_name="A2"),
										transitions={'arrived': 'music_2', 'canceled': 'A2', 'failed': 'A2'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:274
			OperatableStateMachine.add('A3',
										SiteNavigation(site_name="A3"),
										transitions={'arrived': 'music_3', 'canceled': 'A3', 'failed': 'A3'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:374
			OperatableStateMachine.add('A4',
										SiteNavigation(site_name="A4"),
										transitions={'arrived': 'music_4', 'canceled': 'A4', 'failed': 'A4'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:474
			OperatableStateMachine.add('A5',
										SiteNavigation(site_name="A5"),
										transitions={'arrived': 'music_5', 'canceled': 'A5', 'failed': 'A5'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:574
			OperatableStateMachine.add('A6',
										SiteNavigation(site_name="A6"),
										transitions={'arrived': 'music_6', 'canceled': 'A6', 'failed': 'A6'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:674
			OperatableStateMachine.add('A7',
										SiteNavigation(site_name="A7"),
										transitions={'arrived': 'music_7', 'canceled': 'A7', 'failed': 'A7'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:196 y:774
			OperatableStateMachine.add('A8',
										SiteNavigation(site_name="A8"),
										transitions={'arrived': 'music_8', 'canceled': 'A8', 'failed': 'A8'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:796 y:674
			OperatableStateMachine.add('A9',
										SiteNavigation(site_name="A9"),
										transitions={'arrived': 'music_9', 'canceled': 'A9', 'failed': 'A9'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:796 y:174
			OperatableStateMachine.add('IninialPose',
										SiteNavigation(site_name="initial_pose"),
										transitions={'arrived': 'arrived', 'canceled': 'IninialPose', 'failed': 'IninialPose'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:796 y:474
			OperatableStateMachine.add('ReturnPoint',
										SiteNavigation(site_name="return_point"),
										transitions={'arrived': 'lift_dump', 'canceled': 'ReturnPoint', 'failed': 'ReturnPoint'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:775 y:271
			OperatableStateMachine.add('do_forward',
										self.use_behavior(do_forwardSM, 'branch1/do_forward'),
										transitions={'finished': 'IninialPose'},
										autonomy={'finished': Autonomy.Inherit})

			# x:775 y:371
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'branch1/lift_dump'),
										transitions={'finished': 'do_forward'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:71
			OperatableStateMachine.add('music',
										self.use_behavior(musicSM, 'branch1/music'),
										transitions={'finished': 'A2'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:171
			OperatableStateMachine.add('music_2',
										self.use_behavior(musicSM, 'branch1/music_2'),
										transitions={'finished': 'A3'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:271
			OperatableStateMachine.add('music_3',
										self.use_behavior(musicSM, 'branch1/music_3'),
										transitions={'finished': 'A4'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:371
			OperatableStateMachine.add('music_4',
										self.use_behavior(musicSM, 'branch1/music_4'),
										transitions={'finished': 'A5'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:471
			OperatableStateMachine.add('music_5',
										self.use_behavior(musicSM, 'branch1/music_5'),
										transitions={'finished': 'A6'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:571
			OperatableStateMachine.add('music_6',
										self.use_behavior(musicSM, 'branch1/music_6'),
										transitions={'finished': 'A7'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:671
			OperatableStateMachine.add('music_7',
										self.use_behavior(musicSM, 'branch1/music_7'),
										transitions={'finished': 'A8'},
										autonomy={'finished': Autonomy.Inherit})

			# x:475 y:771
			OperatableStateMachine.add('music_8',
										self.use_behavior(musicSM, 'branch1/music_8'),
										transitions={'finished': 'A9'},
										autonomy={'finished': Autonomy.Inherit})

			# x:775 y:571
			OperatableStateMachine.add('music_9',
										self.use_behavior(musicSM, 'branch1/music_9'),
										transitions={'finished': 'ReturnPoint'},
										autonomy={'finished': Autonomy.Inherit})



		with _state_machine:
			# x:296 y:224
			OperatableStateMachine.add('BeginTake',
										SiteNavigation(site_name="begin_take"),
										transitions={'arrived': 'shelf_docking', 'canceled': 'log2', 'failed': 'log2'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:96 y:424
			OperatableStateMachine.add('FromSiteName',
										SiteTransferFrom(),
										transitions={'arrived': 'shelf_docking', 'canceled': 'log1', 'failed': 'log1'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'from_site': 'from_site'})

			# x:96 y:224
			OperatableStateMachine.add('FromWhere',
										FromWhere(),
										transitions={'done': 'ToWhere'},
										autonomy={'done': Autonomy.Off},
										remapping={'from_site': 'from_site'})

			# x:896 y:424
			OperatableStateMachine.add('Judge',
										BlkcCross(),
										transitions={'1_5': 'finished', '2_3_4_6': 'failed'},
										autonomy={'1_5': Autonomy.Off, '2_3_4_6': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:696 y:424
			OperatableStateMachine.add('ToSiteName',
										SiteTransferTo(),
										transitions={'arrived': 'Judge', 'canceled': 'log4', 'failed': 'log4'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:96 y:324
			OperatableStateMachine.add('ToWhere',
										ToWhere(),
										transitions={'done': 'BeginTake'},
										autonomy={'done': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:693 y:321
			OperatableStateMachine.add('branch1',
										_sm_branch1_0,
										transitions={'arrived': 'finished'},
										autonomy={'arrived': Autonomy.Inherit},
										remapping={'to_site': 'to_site'})

			# x:275 y:421
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': 'branch1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:107 y:524
			OperatableStateMachine.add('log1',
										LogState(text="ToSite path failed or canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'FromSiteName'},
										autonomy={'done': Autonomy.Off})

			# x:307 y:124
			OperatableStateMachine.add('log2',
										LogState(text="begin take navigation path faild or canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'BeginTake'},
										autonomy={'done': Autonomy.Off})

			# x:507 y:224
			OperatableStateMachine.add('log3',
										LogState(text="shelfDocking failed timeout", severity=Logger.REPORT_HINT),
										transitions={'done': 'shelf_docking'},
										autonomy={'done': Autonomy.Off})

			# x:707 y:524
			OperatableStateMachine.add('log4',
										LogState(text="SiteTransterT0 failed or canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'ToSiteName'},
										autonomy={'done': Autonomy.Off})

			# x:275 y:321
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'lift_load', 'failed': 'log3'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
