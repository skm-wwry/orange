#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.init_lift_sm import init_liftSM
from agv_flexbe_states.initialization_ending import InitializationEnding
from agv_flexbe_states.initialization_pose import InitializationPose
from agv_flexbe_states.judge_amcl import JudgeAMCL
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 01 2020
@author: zenglei
'''
class initial_taskSM(Behavior):
	'''
	initialization: pose - alert
	'''


	def __init__(self):
		super(initial_taskSM, self).__init__()
		self.name = 'initial_task'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(init_liftSM, 'init_lift')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:401 y:632
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:91 y:49
			OperatableStateMachine.add('init_lift',
										self.use_behavior(init_liftSM, 'init_lift'),
										transitions={'finished': 'initial-pose'},
										autonomy={'finished': Autonomy.Inherit})

			# x:354 y:472
			OperatableStateMachine.add('initial-music',
										InitializationEnding(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:360 y:91
			OperatableStateMachine.add('initial-pose',
										InitializationPose(position_x=82.310, position_y=17.478, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'judge-amcl'},
										autonomy={'done': Autonomy.Off})

			# x:359 y:227
			OperatableStateMachine.add('judge-amcl',
										JudgeAMCL(),
										transitions={'true': 'initial-music', 'false': 'wait-1s'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off})

			# x:582 y:227
			OperatableStateMachine.add('wait-1s',
										WaitState(wait_time=1),
										transitions={'done': 'initial-pose'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
