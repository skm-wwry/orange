#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.joy_feedback_array import joy_feedback_array_pub
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Aug 13 2020
@author: sunkm
'''
class closeSM(Behavior):
	'''
	joy close
	'''


	def __init__(self):
		super(closeSM, self).__init__()
		self.name = 'close'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:347
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:131 y:74
			OperatableStateMachine.add('open',
										joy_feedback_array_pub(topic="joy_feedback_array", data_type=1, data_id=10, data_intensity=1),
										transitions={'done': 'wait'},
										autonomy={'done': Autonomy.Off})

			# x:157 y:174
			OperatableStateMachine.add('wait',
										WaitState(wait_time=3),
										transitions={'done': 'close'},
										autonomy={'done': Autonomy.Off})

			# x:131 y:274
			OperatableStateMachine.add('close',
										joy_feedback_array_pub(topic="joy_feedback_array", data_type=1, data_id=10, data_intensity=0),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
