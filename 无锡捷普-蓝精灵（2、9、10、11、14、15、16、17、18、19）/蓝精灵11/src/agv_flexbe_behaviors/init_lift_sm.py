#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.lift_bias_pos_sm import lift_bias_posSM
from agv_flexbe_behaviors.lift_dump_limit_sm import lift_dump_limitSM
from agv_flexbe_behaviors.lift_home_pos_sm import lift_home_posSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Apr 23 2020
@author: ouiyeah
'''
class init_liftSM(Behavior):
	'''
	init_lift
	'''


	def __init__(self):
		super(init_liftSM, self).__init__()
		self.name = 'init_lift'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(lift_bias_posSM, 'lift_bias_pos')
		self.add_behavior(lift_dump_limitSM, 'lift_dump_limit')
		self.add_behavior(lift_home_posSM, 'lift_home_pos')
		self.add_behavior(lift_home_posSM, 'lift_home_pos_2')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:432
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('lift_dump_limit',
										self.use_behavior(lift_dump_limitSM, 'lift_dump_limit'),
										transitions={'finished': 'lift_home_pos'},
										autonomy={'finished': Autonomy.Inherit})

			# x:299 y:47
			OperatableStateMachine.add('lift_home_pos',
										self.use_behavior(lift_home_posSM, 'lift_home_pos'),
										transitions={'finished': 'lift_bias_pos'},
										autonomy={'finished': Autonomy.Inherit})

			# x:298 y:340
			OperatableStateMachine.add('lift_home_pos_2',
										self.use_behavior(lift_home_posSM, 'lift_home_pos_2'),
										transitions={'finished': 'finished'},
										autonomy={'finished': Autonomy.Inherit})

			# x:300 y:196
			OperatableStateMachine.add('lift_bias_pos',
										self.use_behavior(lift_bias_posSM, 'lift_bias_pos'),
										transitions={'finished': 'lift_home_pos_2'},
										autonomy={'finished': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
