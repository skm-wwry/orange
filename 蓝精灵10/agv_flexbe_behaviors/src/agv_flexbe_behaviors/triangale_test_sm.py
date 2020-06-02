#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.do_backward import DoBackward
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.navigation import Navigation
from agv_flexbe_states.task_switch import TaskSwitch
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 12 2020
@author: zl
'''
class triangale_testSM(Behavior):
	'''
	test
	'''


	def __init__(self):
		super(triangale_testSM, self).__init__()
		self.name = 'triangale_test'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:339 y:62
			OperatableStateMachine.add('s-1',
										Navigation(position_x=-3.70, position_y=0.53, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'triangle_on', 'failed': 'log-1', 'canceled': 'log-1'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:336 y:559
			OperatableStateMachine.add('log',
										LogState(text="pause-s2", severity=Logger.REPORT_HINT),
										transitions={'done': 's-2'},
										autonomy={'done': Autonomy.Off})

			# x:123 y:196
			OperatableStateMachine.add('log-1',
										LogState(text="pause-s1", severity=Logger.REPORT_HINT),
										transitions={'done': 's-1'},
										autonomy={'done': Autonomy.Off})

			# x:770 y:227
			OperatableStateMachine.add('log-3',
										LogState(text="pause-homing", severity=Logger.REPORT_HINT),
										transitions={'done': 'triangle_homing'},
										autonomy={'done': Autonomy.Off})

			# x:768 y:456
			OperatableStateMachine.add('log-4',
										LogState(text="pause-backhaha", severity=Logger.REPORT_HINT),
										transitions={'done': 'do-back'},
										autonomy={'done': Autonomy.Off})

			# x:330 y:434
			OperatableStateMachine.add('s-2',
										Navigation(position_x=-16.40, position_y=1.667, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id='map'),
										transitions={'arrived': 'wait-2s', 'failed': 'log', 'canceled': 'log'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:577 y:226
			OperatableStateMachine.add('triangle_homing',
										HomingControl(target_frame="base_object", target_x=-0.55, target_y=0, target_yaw=0),
										transitions={'succeeded': 'triangle_off', 'failed': 'log-3'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:574 y:322
			OperatableStateMachine.add('triangle_off',
										TaskSwitch(seq=0, frame_id="triangle"),
										transitions={'done': 'do-back'},
										autonomy={'done': Autonomy.Off})

			# x:571 y:60
			OperatableStateMachine.add('triangle_on',
										TaskSwitch(seq=1, frame_id="triangle"),
										transitions={'done': 'wait15s'},
										autonomy={'done': Autonomy.Off})

			# x:337 y:261
			OperatableStateMachine.add('wait-2s',
										WaitState(wait_time=2),
										transitions={'done': 's-1'},
										autonomy={'done': Autonomy.Off})

			# x:585 y:140
			OperatableStateMachine.add('wait15s',
										WaitState(wait_time=15),
										transitions={'done': 'triangle_homing'},
										autonomy={'done': Autonomy.Off})

			# x:577 y:436
			OperatableStateMachine.add('do-back',
										DoBackward(),
										transitions={'succeeded': 's-2', 'failed': 'log-4'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
