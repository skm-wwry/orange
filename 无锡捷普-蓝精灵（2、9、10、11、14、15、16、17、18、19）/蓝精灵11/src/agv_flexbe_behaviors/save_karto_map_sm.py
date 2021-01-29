#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.alert_play import AlertPlay
from agv_flexbe_states.karto_save_map import KartoSaveMap
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue Sep 29 2020
@author: Zeng Lei
'''
class save_karto_mapSM(Behavior):
	'''
	save slam-toolobox map and posegraph
	'''


	def __init__(self):
		super(save_karto_mapSM, self).__init__()
		self.name = 'save_karto_map'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:491 y:83
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('save_map',
										KartoSaveMap(map_name="mymap"),
										transitions={'done': 'save_map_alert'},
										autonomy={'done': Autonomy.Off})

			# x:254 y:44
			OperatableStateMachine.add('save_map_alert',
										AlertPlay(sound_id=21, mode="single", wait_time=3, single_time=3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
