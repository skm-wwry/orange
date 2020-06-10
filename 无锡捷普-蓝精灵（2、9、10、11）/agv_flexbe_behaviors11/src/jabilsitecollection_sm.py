#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_states.site_collection import SiteCollection
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Mon Jun 08 2020
@author: skm
'''
class jabilSiteCollectionSM(Behavior):
	'''
	站点采集
	'''


	def __init__(self):
		super(jabilSiteCollectionSM, self).__init__()
		self.name = 'jabilSiteCollection'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1283 y:334
		_state_machine = OperatableStateMachine(outcomes=['finished'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:47 y:24
			OperatableStateMachine.add('home',
										SiteCollection(position_x=29.606, position_y=5.834, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'charge_point'},
										autonomy={'done': Autonomy.Off})

			# x:1047 y:24
			OperatableStateMachine.add('blkc01l2down',
										SiteCollection(position_x=44.421, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc01l3down'},
										autonomy={'done': Autonomy.Off})

			# x:1247 y:24
			OperatableStateMachine.add('blkc01l3down',
										SiteCollection(position_x=41.446, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc02down'},
										autonomy={'done': Autonomy.Off})

			# x:1247 y:174
			OperatableStateMachine.add('blkc02down',
										SiteCollection(position_x=48.593, position_y=153.700, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc02up'},
										autonomy={'done': Autonomy.Off})

			# x:1047 y:174
			OperatableStateMachine.add('blkc02up',
										SiteCollection(position_x=40.133, position_y=152.676, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'blkc03down'},
										autonomy={'done': Autonomy.Off})

			# x:847 y:174
			OperatableStateMachine.add('blkc03down',
										SiteCollection(position_x=48.647, position_y=131.882, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc03up'},
										autonomy={'done': Autonomy.Off})

			# x:647 y:174
			OperatableStateMachine.add('blkc03up',
										SiteCollection(position_x=40.367, position_y=132.025, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id=0),
										transitions={'done': 'blkc04down'},
										autonomy={'done': Autonomy.Off})

			# x:447 y:174
			OperatableStateMachine.add('blkc04down',
										SiteCollection(position_x=44.264, position_y=89.765, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'blkc04up'},
										autonomy={'done': Autonomy.Off})

			# x:247 y:174
			OperatableStateMachine.add('blkc04up',
										SiteCollection(position_x=39.884, position_y=89.399, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc05l1down'},
										autonomy={'done': Autonomy.Off})

			# x:47 y:174
			OperatableStateMachine.add('blkc05l1down',
										SiteCollection(position_x=37.083, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc05l2down'},
										autonomy={'done': Autonomy.Off})

			# x:47 y:324
			OperatableStateMachine.add('blkc05l2down',
										SiteCollection(position_x=34.411, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc05l3down'},
										autonomy={'done': Autonomy.Off})

			# x:247 y:324
			OperatableStateMachine.add('blkc05l3down',
										SiteCollection(position_x=31.375, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc06down'},
										autonomy={'done': Autonomy.Off})

			# x:447 y:324
			OperatableStateMachine.add('blkc06down',
										SiteCollection(position_x=38.268, position_y=152.651, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc06up'},
										autonomy={'done': Autonomy.Off})

			# x:647 y:324
			OperatableStateMachine.add('blkc06up',
										SiteCollection(position_x=29.681, position_y=152.753, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'blkc07down'},
										autonomy={'done': Autonomy.Off})

			# x:847 y:324
			OperatableStateMachine.add('blkc07down',
										SiteCollection(position_x=38.305, position_y=131.705, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc07up'},
										autonomy={'done': Autonomy.Off})

			# x:1047 y:324
			OperatableStateMachine.add('blkc07up',
										SiteCollection(position_x=29.405, position_y=131.698, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:247 y:24
			OperatableStateMachine.add('charge_point',
										SiteCollection(position_x=30.214, position_y=5.917, position_z=0, orientation_x=0, orientation_y=0, orientation_z=0, orientation_w=1, frame_id='map'),
										transitions={'done': 'initial_pose'},
										autonomy={'done': Autonomy.Off})

			# x:644 y:25
			OperatableStateMachine.add('enddown',
										SiteCollection(position_x=82.310, position_y=18.461, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'blkc01l1down'},
										autonomy={'done': Autonomy.Off})

			# x:447 y:24
			OperatableStateMachine.add('initial_pose',
										SiteCollection(position_x=30.477, position_y=6.062, position_z=0, orientation_x=0, orientation_y=0, orientation_z=1, orientation_w=0, frame_id='map'),
										transitions={'done': 'enddown'},
										autonomy={'done': Autonomy.Off})

			# x:847 y:24
			OperatableStateMachine.add('blkc01l1down',
										SiteCollection(position_x=47.113, position_y=173.94, position_z=0, orientation_x=0, orientation_y=0, orientation_z=-0.7071, orientation_w=0.7071, frame_id='map'),
										transitions={'done': 'blkc01l2down'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
