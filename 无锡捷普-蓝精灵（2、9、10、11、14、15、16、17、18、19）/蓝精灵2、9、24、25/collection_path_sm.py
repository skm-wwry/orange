#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from agv_flexbe_behaviors.do_forward_sm import do_forwardSM
from agv_flexbe_behaviors.lift_dump_sm import lift_dumpSM
from agv_flexbe_behaviors.lift_load_sm import lift_loadSM
from agv_flexbe_behaviors.music_sm import musicSM
from agv_flexbe_behaviors.shelf_docking_sm import shelf_dockingSM
from agv_flexbe_states.site_navigation import SiteNavigation
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Feb 04 2021
@author: sunkm
'''
class Collection_PathSM(Behavior):
	'''
	Collection_Path_120s
	'''


	def __init__(self):
		super(Collection_PathSM, self).__init__()
		self.name = 'Collection_Path'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(do_forwardSM, 'do_forward')
		self.add_behavior(lift_dumpSM, 'lift_dump')
		self.add_behavior(lift_loadSM, 'lift_load')
		self.add_behavior(musicSM, 'music')
		self.add_behavior(musicSM, 'music_2')
		self.add_behavior(musicSM, 'music_3')
		self.add_behavior(musicSM, 'music_4')
		self.add_behavior(musicSM, 'music_5')
		self.add_behavior(musicSM, 'music_6')
		self.add_behavior(musicSM, 'music_7')
		self.add_behavior(musicSM, 'music_8')
		self.add_behavior(musicSM, 'music_9')
		self.add_behavior(shelf_dockingSM, 'shelf_docking')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:83 y:193, x:583 y:290
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:46 y:24
			OperatableStateMachine.add('01',
										SiteNavigation(site_name="up"),
										transitions={'arrived': 'shelf_docking', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:24
			OperatableStateMachine.add('02',
										SiteNavigation(site_name="a1"),
										transitions={'arrived': 'music', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:124
			OperatableStateMachine.add('03',
										SiteNavigation(site_name="a2"),
										transitions={'arrived': 'music_2', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:224
			OperatableStateMachine.add('04',
										SiteNavigation(site_name="a3"),
										transitions={'arrived': 'music_3', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:324
			OperatableStateMachine.add('05',
										SiteNavigation(site_name="a4"),
										transitions={'arrived': 'music_4', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:424
			OperatableStateMachine.add('06',
										SiteNavigation(site_name="a5"),
										transitions={'arrived': 'music_5', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:524
			OperatableStateMachine.add('07',
										SiteNavigation(site_name="a6"),
										transitions={'arrived': 'music_6', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:946 y:624
			OperatableStateMachine.add('08',
										SiteNavigation(site_name="a7"),
										transitions={'arrived': 'music_7', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:696 y:624
			OperatableStateMachine.add('09',
										SiteNavigation(site_name="a8"),
										transitions={'arrived': 'music_8', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:446 y:624
			OperatableStateMachine.add('a10',
										SiteNavigation(site_name="a9"),
										transitions={'arrived': 'music_9', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:25 y:371
			OperatableStateMachine.add('do_forward',
										self.use_behavior(do_forwardSM, 'do_forward'),
										transitions={'finished': 'initial_pose'},
										autonomy={'finished': Autonomy.Inherit})

			# x:46 y:624
			OperatableStateMachine.add('down',
										SiteNavigation(site_name="down"),
										transitions={'arrived': 'lift_dump', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:46 y:224
			OperatableStateMachine.add('initial_pose',
										SiteNavigation(site_name="initial_pose"),
										transitions={'arrived': 'finished', 'canceled': 'failed', 'failed': 'failed'},
										autonomy={'arrived': Autonomy.Off, 'canceled': Autonomy.Off, 'failed': Autonomy.Off})

			# x:25 y:471
			OperatableStateMachine.add('lift_dump',
										self.use_behavior(lift_dumpSM, 'lift_dump'),
										transitions={'finished': 'do_forward'},
										autonomy={'finished': Autonomy.Inherit})

			# x:625 y:21
			OperatableStateMachine.add('lift_load',
										self.use_behavior(lift_loadSM, 'lift_load'),
										transitions={'finished': '02'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:21
			OperatableStateMachine.add('music',
										self.use_behavior(musicSM, 'music'),
										transitions={'finished': '03'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:121
			OperatableStateMachine.add('music_2',
										self.use_behavior(musicSM, 'music_2'),
										transitions={'finished': '04'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:221
			OperatableStateMachine.add('music_3',
										self.use_behavior(musicSM, 'music_3'),
										transitions={'finished': '05'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:321
			OperatableStateMachine.add('music_4',
										self.use_behavior(musicSM, 'music_4'),
										transitions={'finished': '06'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:421
			OperatableStateMachine.add('music_5',
										self.use_behavior(musicSM, 'music_5'),
										transitions={'finished': '07'},
										autonomy={'finished': Autonomy.Inherit})

			# x:1125 y:521
			OperatableStateMachine.add('music_6',
										self.use_behavior(musicSM, 'music_6'),
										transitions={'finished': '08'},
										autonomy={'finished': Autonomy.Inherit})

			# x:925 y:771
			OperatableStateMachine.add('music_7',
										self.use_behavior(musicSM, 'music_7'),
										transitions={'finished': '09'},
										autonomy={'finished': Autonomy.Inherit})

			# x:675 y:771
			OperatableStateMachine.add('music_8',
										self.use_behavior(musicSM, 'music_8'),
										transitions={'finished': 'a10'},
										autonomy={'finished': Autonomy.Inherit})

			# x:425 y:771
			OperatableStateMachine.add('music_9',
										self.use_behavior(musicSM, 'music_9'),
										transitions={'finished': 'down'},
										autonomy={'finished': Autonomy.Inherit})

			# x:325 y:21
			OperatableStateMachine.add('shelf_docking',
										self.use_behavior(shelf_dockingSM, 'shelf_docking'),
										transitions={'finished': 'lift_load', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
