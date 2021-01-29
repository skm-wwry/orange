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
from agv_flexbe_states.current_detection import CurrentDetection
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.joy_operation import JoyOperation
from agv_flexbe_states.navigation import Navigation
from agv_flexbe_states.pile_off import PileOff
from agv_flexbe_states.pile_on import PileOn
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Dec 13 2019
@author: Lei Zeng
'''
class autocharge_onSM(Behavior):
	'''
	autocharge
	'''


	def __init__(self):
		super(autocharge_onSM, self).__init__()
		self.name = 'autocharge_on'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:289 y:580, x:521 y:593
		_state_machine = OperatableStateMachine(outcomes=['finished', 'timeout'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:871 y:47
		_sm_pile_0 = OperatableStateMachine(outcomes=['done'])

		with _sm_pile_0:
			# x:74 y:36
			OperatableStateMachine.add('pile_on',
										PileOn(),
										transitions={'done': 'pile_alert'},
										autonomy={'done': Autonomy.Off})

			# x:409 y:135
			OperatableStateMachine.add('charge-homing',
										HomingControl(target_frame="base_shelf", target_x=-0.425, target_y=0, target_yaw=0),
										transitions={'succeeded': 'alert_stop', 'failed': 'log-homing'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:239 y:134
			OperatableStateMachine.add('detection-waiting',
										WaitState(wait_time=5),
										transitions={'done': 'charge-homing'},
										autonomy={'done': Autonomy.Off})

			# x:422 y:257
			OperatableStateMachine.add('log-homing',
										LogState(text="resend charge homing", severity=Logger.REPORT_HINT),
										transitions={'done': 'charge-homing'},
										autonomy={'done': Autonomy.Off})

			# x:74 y:130
			OperatableStateMachine.add('pile_alert',
										AlertPlay(sound_id=6, mode="loop", wait_time=3, single_time=3),
										transitions={'done': 'detection-waiting'},
										autonomy={'done': Autonomy.Off})

			# x:627 y:47
			OperatableStateMachine.add('pile_off',
										PileOff(),
										transitions={'done': 'done'},
										autonomy={'done': Autonomy.Off})

			# x:629 y:133
			OperatableStateMachine.add('alert_stop',
										AlertLoopStop(),
										transitions={'done': 'pile_off'},
										autonomy={'done': Autonomy.Off})


		# x:237 y:241, x:634 y:109, x:85 y:237, x:631 y:155, x:203 y:301, x:64 y:306
		_sm_container_1 = ConcurrencyContainer(outcomes=['finished', 'failed', 'stop'], conditions=[
										('stop', [('do_backwards', 'succeeded')]),
										('finished', [('do_backwards', 'failed'), ('current_detection', 'done')]),
										('failed', [('current_detection', 'timeout')])
										])

		with _sm_container_1:
			# x:81 y:99
			OperatableStateMachine.add('do_backwards',
										HomingControl(target_frame="base_link", target_x=-0.15, target_y=0, target_yaw=0),
										transitions={'succeeded': 'stop', 'failed': 'finished'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:316 y:99
			OperatableStateMachine.add('current_detection',
										CurrentDetection(current=0.1, timeout=30),
										transitions={'done': 'finished', 'timeout': 'failed'},
										autonomy={'done': Autonomy.Off, 'timeout': Autonomy.Off})



		with _state_machine:
			# x:247 y:36
			OperatableStateMachine.add('charge_point',
										Navigation(position_x=84.473, position_y=17.963, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'Pile', 'failed': 'log_1', 'canceled': 'log_1'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:244 y:150
			OperatableStateMachine.add('Pile',
										_sm_pile_0,
										transitions={'done': 'turn_back'},
										autonomy={'done': Autonomy.Inherit})

			# x:249 y:341
			OperatableStateMachine.add('joy_start_1',
										JoyOperation(topic="joy_feedback_array", idd=7, intensity=1, typee=1),
										transitions={'done': 'Container'},
										autonomy={'done': Autonomy.Off})

			# x:484 y:33
			OperatableStateMachine.add('log_1',
										LogState(text="charge-point resend", severity=Logger.REPORT_HINT),
										transitions={'done': 'charge_point'},
										autonomy={'done': Autonomy.Off})

			# x:485 y:250
			OperatableStateMachine.add('log_2',
										LogState(text="turn back log", severity=Logger.REPORT_HINT),
										transitions={'done': 'turn_back'},
										autonomy={'done': Autonomy.Off})

			# x:249 y:249
			OperatableStateMachine.add('turn_back',
										HomingControl(target_frame="base_link", target_x=0, target_y=0, target_yaw=3.14159),
										transitions={'succeeded': 'joy_start_1', 'failed': 'log_2'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:250 y:441
			OperatableStateMachine.add('Container',
										_sm_container_1,
										transitions={'finished': 'finished', 'failed': 'timeout', 'stop': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'stop': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
