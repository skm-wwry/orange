#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.navigation import Navigation
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon May 25 2020
@author: skm
'''
class BackHomeSM(Behavior):
	'''
	20200525
	'''


	def __init__(self):
		super(BackHomeSM, self).__init__()
		self.name = 'BackHome'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:184 y:114
			OperatableStateMachine.add('backhome',
										Navigation(position_x=82.310, position_y=17.963, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'arrived': 'finished', 'failed': 'failed', 'canceled': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'failed': Autonomy.Off, 'canceled': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
