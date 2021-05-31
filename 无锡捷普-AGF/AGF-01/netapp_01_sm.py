#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.fork_dump_sm import fork_dumpSM
from agv_flexbe_behaviors.fork_load_sm import fork_loadSM
from agv_flexbe_states.from_where import FromWhere
from agv_flexbe_states.scan_pallet import ScanPallet
from agv_flexbe_states.site_navigation import SiteNavigation
from agv_flexbe_states.site_transfer_from import SiteTransferFrom
from agv_flexbe_states.to_where import ToWhere
from agv_flexbe_states.wait_time import WaitTime
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Sep 02 2020
@author: sumkm
'''
class NetApp_01SM(Behavior):
	'''
	NetApp_01
	'''


	def __init__(self):
		super(NetApp_01SM, self).__init__()
		self.name = 'NetApp_01'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(fork_dumpSM, 'fork_dump')
		self.add_behavior(fork_dumpSM, 'fork_dump_2')
		self.add_behavior(fork_loadSM, 'fork_load')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1383 y:290, x:1383 y:590
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:325 y:71
			OperatableStateMachine.add('fork_dump_2',
										self.use_behavior(fork_dumpSM, 'fork_dump_2'),
										transitions={'finished': 'SiteBegin'},
										autonomy={'finished': Autonomy.Inherit})

			# x:146 y:224
			OperatableStateMachine.add('FromWhere',
										FromWhere(),
										transitions={'done': 'ToWhere'},
										autonomy={'done': Autonomy.Off},
										remapping={'from_site': 'from_site'})

			# x:746 y:574
			OperatableStateMachine.add('JudgeFirst',
										ScanPallet(ranges=[1.5,3,-2.5,0]),
										transitions={'occupied': 'wait5s', 'free': 'down_lift_begin'},
										autonomy={'occupied': Autonomy.Off, 'free': Autonomy.Off})

			# x:946 y:474
			OperatableStateMachine.add('JudgeLast',
										ScanPallet(ranges=[1.5,3,-2.5,0]),
										transitions={'occupied': 'JudgeLog', 'free': 'down_lift_begin'},
										autonomy={'occupied': Autonomy.Off, 'free': Autonomy.Off})

			# x:1157 y:574
			OperatableStateMachine.add('JudgeLog',
										LogState(text="Obstacle detected, end of task", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:346 y:574
			OperatableStateMachine.add('SiteBack',
										SiteNavigation(site_name="NetApp_01_back"),
										transitions={'arrived': 'down_lift_wait', 'canceled': 'SiteBack', 'failed': 'SiteBack'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:346 y:174
			OperatableStateMachine.add('SiteBegin',
										SiteNavigation(site_name="NetApp_01_begin"),
										transitions={'arrived': 'SiteMiddle', 'canceled': 'SiteBegin', 'failed': 'SiteBegin'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:346 y:274
			OperatableStateMachine.add('SiteMiddle',
										SiteNavigation(site_name="NetApp_01_middle"),
										transitions={'arrived': 'SiteName', 'canceled': 'SiteMiddle', 'failed': 'SiteMiddle'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:346 y:374
			OperatableStateMachine.add('SiteName',
										SiteNavigation(site_name="NetApp_01"),
										transitions={'arrived': 'fork_load', 'canceled': 'SiteName', 'failed': 'SiteName'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:146 y:324
			OperatableStateMachine.add('ToWhere',
										ToWhere(),
										transitions={'done': 'FromSiteName'},
										autonomy={'done': Autonomy.Off},
										remapping={'to_site': 'to_site'})

			# x:746 y:274
			OperatableStateMachine.add('down_lift',
										SiteNavigation(site_name="down_lift"),
										transitions={'arrived': 'fork_dump', 'canceled': 'down_lift', 'failed': 'down_lift'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:746 y:474
			OperatableStateMachine.add('down_lift_begin',
										SiteNavigation(site_name="down_lift_begin"),
										transitions={'arrived': 'down_lift_middle', 'canceled': 'down_lift_begin', 'failed': 'down_lift_begin'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:745 y:374
			OperatableStateMachine.add('down_lift_middle',
										SiteNavigation(site_name="down_lift_middle"),
										transitions={'arrived': 'down_lift', 'canceled': 'down_lift_middle', 'failed': 'down_lift_middle'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:546 y:574
			OperatableStateMachine.add('down_lift_wait',
										SiteNavigation(site_name="down_lift_wait"),
										transitions={'arrived': 'JudgeFirst', 'canceled': 'down_lift_wait', 'failed': 'down_lift_wait'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:725 y:171
			OperatableStateMachine.add('fork_dump',
										self.use_behavior(fork_dumpSM, 'fork_dump'),
										transitions={'finished': 'home_back'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:471
			OperatableStateMachine.add('fork_load',
										self.use_behavior(fork_loadSM, 'fork_load'),
										transitions={'finished': 'SiteBack'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1146 y:274
			OperatableStateMachine.add('home',
										SiteNavigation(site_name="home"),
										transitions={'arrived': 'finished', 'canceled': 'home', 'failed': 'home'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:746 y:74
			OperatableStateMachine.add('home_back',
										SiteNavigation(site_name="home_back"),
										transitions={'arrived': 'home_back_begin', 'canceled': 'home_back', 'failed': 'home_back'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1143 y:74
			OperatableStateMachine.add('home_back_begin',
										SiteNavigation(site_name="home_back_begin"),
										transitions={'arrived': 'home_back_middle', 'canceled': 'home_back_begin', 'failed': 'home_back_begin'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1140 y:174
			OperatableStateMachine.add('home_back_middle',
										SiteNavigation(site_name="home_back_middle"),
										transitions={'arrived': 'home', 'canceled': 'home_back_middle', 'failed': 'home_back_middle'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:574
			OperatableStateMachine.add('wait5s',
										WaitTime(wait_time=5),
										transitions={'done': 'JudgeLast'},
										autonomy={'done': Autonomy.Off})

			# x:146 y:424
			OperatableStateMachine.add('FromSiteName',
										SiteTransferFrom(),
										transitions={'arrived': 'fork_dump_2', 'canceled': 'FromSiteName', 'failed': 'FromSiteName'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'from_site': 'from_site'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
