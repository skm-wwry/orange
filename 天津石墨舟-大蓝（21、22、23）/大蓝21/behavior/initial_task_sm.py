#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.close_sm import closeSM
from agv_flexbe_behaviors.init_lift_sm import init_liftSM
from agv_flexbe_states.initialization_ending import InitializationEnding
from agv_flexbe_states.judge_amcl import JudgeAMCL
from agv_flexbe_states.site_initialization import SiteInitialization
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
		self.add_behavior(closeSM, 'close')
		self.add_behavior(init_liftSM, 'init_lift')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:533 y:490
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:296 y:74
			OperatableStateMachine.add('initial_pose',
										SiteInitialization(site_name="initial_pose"),
										transitions={'done': 'judge_amcl'},
										autonomy={'done': Autonomy.Off})

			# x:275 y:371
			OperatableStateMachine.add('init_lift',
										self.use_behavior(init_liftSM, 'init_lift'),
										transitions={'finished': 'initial_music', 'failed': 'init_lift'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:295 y:474
			OperatableStateMachine.add('initial_music',
										InitializationEnding(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:296 y:174
			OperatableStateMachine.add('judge_amcl',
										JudgeAMCL(),
										transitions={'true': 'close', 'false': 'wait1s'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off})

			# x:507 y:174
			OperatableStateMachine.add('wait1s',
										WaitState(wait_time=1),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:275 y:271
			OperatableStateMachine.add('close',
										self.use_behavior(closeSM, 'close'),
										transitions={'finished': 'init_lift'},
										autonomy={'finished': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
