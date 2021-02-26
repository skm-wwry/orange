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
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Feb 04 2021
@author: sunkm
'''
class musicSM(Behavior):
	'''
	music
	'''


	def __init__(self):
		super(musicSM, self).__init__()
		self.name = 'music'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:283 y:240
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:96 y:24
			OperatableStateMachine.add('open',
										AlertPlay(sound_id=12, mode="loop", wait_time=5, single_time=3),
										transitions={'done': 'wait100s'},
										autonomy={'done': Autonomy.Off})

			# x:107 y:124
			OperatableStateMachine.add('wait100s',
										WaitState(wait_time=100),
										transitions={'done': 'end'},
										autonomy={'done': Autonomy.Off})

			# x:96 y:224
			OperatableStateMachine.add('end',
										AlertLoopStop(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
