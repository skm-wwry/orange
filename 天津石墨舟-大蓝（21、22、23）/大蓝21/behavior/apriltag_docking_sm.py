#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.alert_loop_stop import AlertLoopStop
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.check_detect import CheckDetect
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.reconfigure_state import ReconfigureState
from agv_flexbe_states.task_switch import TaskSwitch
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on 20210201
@author: Lei Zeng
'''
class apriltag_dockingSM(Behavior):
	'''
	apriltag docking
	'''


	def __init__(self):
		super(apriltag_dockingSM, self).__init__()
		self.name = 'apriltag_docking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:333 y:640, x:533 y:565
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:72 y:92
			OperatableStateMachine.add('vel_x_dec',
										ReconfigureState(client="homing_control_server", parameter="max_vel_x", value=0.06),
										transitions={'done': 'tag_on'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:249
			OperatableStateMachine.add('alert_stop_tag',
										AlertLoopStop(),
										transitions={'done': 'check_tag'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:349
			OperatableStateMachine.add('check_tag',
										CheckDetect(dy=0.03, dyaw=0.1, target_frame="current_object"),
										transitions={'succeeded': 'tag_off', 'failed': 'tag_off_'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:458 y:149
			OperatableStateMachine.add('log',
										LogState(text="homing exception", severity=Logger.REPORT_HINT),
										transitions={'done': 'tag_homing'},
										autonomy={'done': Autonomy.Off})

			# x:308 y:49
			OperatableStateMachine.add('tag_aiming',
										WaitState(wait_time=7),
										transitions={'done': 'tag_homing'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:149
			OperatableStateMachine.add('tag_homing',
										HomingControl(target_frame="base_object", target_x=-0.48, target_y=0, target_yaw=0),
										transitions={'succeeded': 'alert_stop_tag', 'failed': 'log'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:297 y:449
			OperatableStateMachine.add('tag_off',
										TaskSwitch(seq=0, frame_id="apriltag"),
										transitions={'done': 'vel_x_inc'},
										autonomy={'done': Autonomy.Off})

			# x:497 y:349
			OperatableStateMachine.add('tag_off_',
										TaskSwitch(seq=0, frame_id="apriltag"),
										transitions={'done': 'vel_x_inc_'},
										autonomy={'done': Autonomy.Off})

			# x:72 y:174
			OperatableStateMachine.add('tag_on',
										TaskSwitch(seq=1, frame_id="apriltag"),
										transitions={'done': 'alert_on_tag'},
										autonomy={'done': Autonomy.Off})

			# x:297 y:524
			OperatableStateMachine.add('vel_x_inc',
										ReconfigureState(client="homing_control_server", parameter="max_vel_x", value=0.2),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:497 y:424
			OperatableStateMachine.add('vel_x_inc_',
										ReconfigureState(client="homing_control_server", parameter="max_vel_x", value=0.2),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:72 y:274
			OperatableStateMachine.add('alert_on_tag',
										AlertPlay(sound_id=30, mode="loop", wait_time=3, single_time=3),
										transitions={'done': 'tag_aiming'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
