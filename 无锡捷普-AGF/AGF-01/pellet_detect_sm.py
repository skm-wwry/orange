#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.scan_pallet import ScanPallet
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Sep 22 2020
@author: zl
'''
class pellet_detectSM(Behavior):
	'''
	pallet 
	'''


	def __init__(self):
		super(pellet_detectSM, self).__init__()
		self.name = 'pellet_detect'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:634 y:135, x:504 y:265
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:96 y:144
			OperatableStateMachine.add('scan_pallet',
										ScanPallet(ranges=[-1,1,1,2]),
										transitions={'occupied': 'log', 'free': 'log-2'},
										autonomy={'occupied': Autonomy.Off, 'free': Autonomy.Off})

			# x:248 y:238
			OperatableStateMachine.add('log-2',
										LogState(text="meiyou", severity=Logger.REPORT_HINT),
										transitions={'done': 'failed'},
										autonomy={'done': Autonomy.Off})

			# x:271 y:75
			OperatableStateMachine.add('log',
										LogState(text="you", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
