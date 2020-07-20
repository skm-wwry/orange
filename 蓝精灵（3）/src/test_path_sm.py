#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.navigation import Navigation
from agv_flexbe_states.site_navigation import SiteNavigation
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jun 22 2020
@author: skm
'''
class Test_PathSM(Behavior):
	'''
	办公室测试轨迹
	'''


	def __init__(self):
		super(Test_PathSM, self).__init__()
		self.name = 'Test_Path'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:52
			OperatableStateMachine.add('test001',
										Navigation(position_x=25.957, position_y=11.650, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id="map"),
										transitions={'arrived': 'home', 'failed': 'log', 'canceled': 'log'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:58 y:167
			OperatableStateMachine.add('log',
										LogState(text="canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'test001'},
										autonomy={'done': Autonomy.Off})

			# x:258 y:167
			OperatableStateMachine.add('log2',
										LogState(text="canceled", severity=Logger.REPORT_HINT),
										transitions={'done': 'home'},
										autonomy={'done': Autonomy.Off})

			# x:247 y:52
			OperatableStateMachine.add('home',
										SiteNavigation(site_name="home"),
										transitions={'arrived': 'test001', 'canceled': 'log2', 'failed': 'log2'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
