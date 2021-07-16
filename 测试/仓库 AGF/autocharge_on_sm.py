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
from agv_flexbe_states.pile_off import PileOff
from agv_flexbe_states.pile_on import PileOn
from agv_flexbe_states.reconfigure_state import ReconfigureState
from agv_flexbe_states.site_navigation import SiteNavigation
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
		# x:883 y:440, x:1033 y:440
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
										HomingControl(target_frame="base_shelf", target_x=-0.75, target_y=0, target_yaw=0),
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


		# x:283 y:240, x:433 y:240, x:133 y:240, x:433 y:340, x:283 y:340, x:133 y:340
		_sm_container_1 = ConcurrencyContainer(outcomes=['finished', 'failed', 'stop'], conditions=[
										('stop', [('do_backwards', 'succeeded')]),
										('finished', [('do_backwards', 'failed'), ('current_detection', 'done')]),
										('failed', [('current_detection', 'timeout')])
										])

		with _sm_container_1:
			# x:96 y:124
			OperatableStateMachine.add('do_backwards',
										HomingControl(target_frame="base_link", target_x=-0.1, target_y=0, target_yaw=0),
										transitions={'succeeded': 'stop', 'failed': 'finished'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:394 y:124
			OperatableStateMachine.add('current_detection',
										CurrentDetection(current=0.1, timeout=5),
										transitions={'done': 'finished', 'timeout': 'failed'},
										autonomy={'done': Autonomy.Off, 'timeout': Autonomy.Off})



		with _state_machine:
			# x:96 y:124
			OperatableStateMachine.add('s2',
										SiteNavigation(site_name="S2"),
										transitions={'arrived': 'change_bz', 'canceled': 's2', 'failed': 's2'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:693 y:121
			OperatableStateMachine.add('Pile',
										_sm_pile_0,
										transitions={'done': 'joy_start_1'},
										autonomy={'done': Autonomy.Inherit})

			# x:296 y:124
			OperatableStateMachine.add('change_bz',
										ReconfigureState(client="move_base", parameter="base_local_planner", value="bz_local_planner/BZPlannerROS"),
										transitions={'done': 's1'},
										autonomy={'done': Autonomy.Off})

			# x:96 y:424
			OperatableStateMachine.add('change_teb',
										ReconfigureState(client="move_base", parameter="base_local_planner", value="teb_local_planner/TebLocalPlannerROS"),
										transitions={'done': 's2'},
										autonomy={'done': Autonomy.Off})

			# x:296 y:424
			OperatableStateMachine.add('forward_600mm',
										HomingControl(target_frame="base_link", target_x=0.6, target_y=0, target_yaw=0),
										transitions={'succeeded': 'change_teb', 'failed': 'forward_600mm'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:696 y:424
			OperatableStateMachine.add('joy_start_0',
										JoyOperation(topic="joy_feedback_array", idd=7, intensity=0, typee=1),
										transitions={'done': 'wait5s'},
										autonomy={'done': Autonomy.Off})

			# x:696 y:224
			OperatableStateMachine.add('joy_start_1',
										JoyOperation(topic="joy_feedback_array", idd=7, intensity=1, typee=1),
										transitions={'done': 'Container'},
										autonomy={'done': Autonomy.Off})

			# x:496 y:124
			OperatableStateMachine.add('s1',
										SiteNavigation(site_name="S1"),
										transitions={'arrived': 'Pile', 'canceled': 's1', 'failed': 's1'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:707 y:324
			OperatableStateMachine.add('wait',
										WaitState(wait_time=20),
										transitions={'done': 'joy_start_0'},
										autonomy={'done': Autonomy.Off})

			# x:507 y:424
			OperatableStateMachine.add('wait5s',
										WaitState(wait_time=5),
										transitions={'done': 'forward_600mm'},
										autonomy={'done': Autonomy.Off})

			# x:896 y:221
			OperatableStateMachine.add('Container',
										_sm_container_1,
										transitions={'finished': 'wait', 'failed': 'timeout', 'stop': 'wait'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'stop': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
