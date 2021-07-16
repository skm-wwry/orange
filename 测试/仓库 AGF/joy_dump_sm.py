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
@author: ouiyeah
'''
class joy_dumpSM(Behavior):
	'''
	joy_dump
	'''


	def __init__(self):
		super(joy_dumpSM, self).__init__()
		self.name = 'joy_dump'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:183 y:540
		_state_machine = OperatableStateMachine(outcomes=['finished'])
		_state_machine.userdata.topic = ""

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:131 y:124
			OperatableStateMachine.add('joy_dump_1',
										joy_feedback_array_pub(topic="joy_feedback_array", data_type=1, data_id=2, data_intensity=1),
										transitions={'done': 'wait5s'},
										autonomy={'done': Autonomy.Off},
										remapping={'topic': 'topic'})

			# x:131 y:324
			OperatableStateMachine.add('joy_load_0',
										joy_feedback_array_pub(topic="joy_feedback_array", data_type=1, data_id=2, data_intensity=0),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'topic': 'topic'})

			# x:157 y:224
			OperatableStateMachine.add('wait5s',
										WaitState(wait_time=5),
										transitions={'done': 'joy_load_0'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
