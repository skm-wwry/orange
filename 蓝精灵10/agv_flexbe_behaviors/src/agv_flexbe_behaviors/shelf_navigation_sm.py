#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.shelf_docking_sm import shelf_dockingSM
from agv_flexbe_states.do_backward import DoBackward
from agv_flexbe_states.homing_control import HomingControl
from agv_flexbe_states.navigation import Navigation
from agv_flexbe_states.reconfigure_state import ReconfigureState
from agv_flexbe_states.shelf_leg_remove_false import ShelfLegRemoveFalse
from agv_flexbe_states.turn_left import TurnLeft
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Nov 28 2019
@author: Lei Zeng
'''
class shelf_navigationSM(Behavior):
	'''
	agv navigation and shelf behavior
	'''


	def __init__(self):
		super(shelf_navigationSM, self).__init__()
		self.name = 'shelf_navigation'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(shelf_dockingSM, 'shelf_docking')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:

		# O 898 81 
		# agv local footprint - agv global footprint

		# O 652 387 
		# shelf on - wait5s - homing - shelf off



	def create(self):
		# x:1246 y:135, x:734 y:499
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:96 y:330, x:160 y:333, x:284 y:331, x:330 y:463
		_sm_agv_footprint_0 = ConcurrencyContainer(outcomes=['finished'], conditions=[
										('finished', [('agv-local-footprint', 'done')]),
										('finished', [('agv-global-footprint', 'done')]),
										('finished', [('leg_remove_false', 'done')])
										])

		with _sm_agv_footprint_0:
			# x:93 y:118
			OperatableStateMachine.add('agv-local-footprint',
										ReconfigureState(client="move_base/local_costmap", parameter="footprint", value='[[-0.3,-0.2],[0.3,-0.2],[0.3,0.2],[-0.3,0.2]]'),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:435 y:114
			OperatableStateMachine.add('leg_remove_false',
										ShelfLegRemoveFalse(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:250 y:115
			OperatableStateMachine.add('agv-global-footprint',
										ReconfigureState(client="move_base/global_costmap", parameter="footprint", value='[[-0.3,-0.2],[0.3,-0.2],[0.3,0.2],[-0.3,0.2]]'),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})



		with _state_machine:
			# x:471 y:122
			OperatableStateMachine.add('S-1',
										Navigation(position_x=3, position_y=4.76, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.707, orientation_w=0.707, frame_id='map'),
										transitions={'arrived': 'S-2', 'failed': 'Logger-1', 'canceled': 'Logger-1'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:482 y:439
			OperatableStateMachine.add('Log-5',
										LogState(text="resend", severity=Logger.REPORT_HINT),
										transitions={'done': 'turn_left'},
										autonomy={'done': Autonomy.Off})

			# x:311 y:125
			OperatableStateMachine.add('Logger-1',
										LogState(text="click to resend Goal", severity=Logger.REPORT_HINT),
										transitions={'done': 'S-1'},
										autonomy={'done': Autonomy.Off})

			# x:312 y:216
			OperatableStateMachine.add('Logger-2',
										LogState(text="click to resend Goal", severity=Logger.REPORT_HINT),
										transitions={'done': 'S-2'},
										autonomy={'done': Autonomy.Off})

			# x:1139 y:217
			OperatableStateMachine.add('Logger-3',
										LogState(text="click to resend Goal", severity=Logger.REPORT_HINT),
										transitions={'done': 'S-3'},
										autonomy={'done': Autonomy.Off})

			# x:470 y:208
			OperatableStateMachine.add('S-2',
										Navigation(position_x=2.55, position_y=4.76, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.707, orientation_w=0.707, frame_id='map'),
										transitions={'arrived': 'turn_left', 'failed': 'Logger-2', 'canceled': 'Logger-2'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:953 y:221
			OperatableStateMachine.add('S-3',
										Navigation(position_x=2.5, position_y=5.05, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id='map'),
										transitions={'arrived': 'agv_footprint', 'failed': 'Logger-3', 'canceled': 'Logger-3'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})

			# x:949 y:118
			OperatableStateMachine.add('agv_footprint',
										_sm_agv_footprint_0,
										transitions={'finished': 'S-1'},
										autonomy={'finished': Autonomy.Inherit})

			# x:955 y:316
			OperatableStateMachine.add('do_back',
										DoBackward(),
										transitions={'succeeded': 'S-3', 'failed': 'log-6'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:470 y:36
			OperatableStateMachine.add('do_forward',
										HomingControl(target_frame="base_link", target_x=0.7, target_y=0, target_yaw=0),
										transitions={'succeeded': 'S-1', 'failed': 'Log-4'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:966 y:460
			OperatableStateMachine.add('log-6',
										LogState(text="resend", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_back'},
										autonomy={'done': Autonomy.Off})

			# x:705 y:316
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'do_back', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:473 y:319
			OperatableStateMachine.add('turn_left',
										TurnLeft(),
										transitions={'succeeded': 'shelf_docking', 'failed': 'Log-5'},
										autonomy={'succeeded': Autonomy.Off, 'failed': Autonomy.Off})

			# x:661 y:30
			OperatableStateMachine.add('Log-4',
										LogState(text="resend", severity=Logger.REPORT_HINT),
										transitions={'done': 'do_forward'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
