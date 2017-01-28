from sys import exit 
from Entity import * # GETTING A DIFFERENT FILE
from random import randint
import time
# GLOBAL VARIABLES TO BE ACCESSED BY THE CLASSES

# BOOLEANS RELATED TO WHETHER OR NOT A ROOM HAS BEEN COLLECTED
riverIced = False # WHETHER OR NOT THE RIVER HAS ICE, AND IS ABLE TO BE WALKED OVER.
towerOfHanoiCompleted = False # WHETHER OR NOT THE TOWEROFHANOI HAS BEEN ACCOMPLISHED
alreadyEnteredRoom = False

# CONTAINERS THAT THE PLAYERS HAVE
inventory = [] # PLACE THAT CAN HOLD MISCOULANIOUS
grenades = [] # LIST CONTAINING THE TWO TYPES OF GRENADES

# CYCLINDERS IN ICE AND FIRE ROOM
cyclinder_left = ["cold"]# LEFT CYCLINDER HAVING "COLD"
cyclinder_right = ["fire"] # RIGHT CYCLINDER HAVING "FIRE"

# ENTITY CREATION
player = Entity(100, 14, 20, 6, 4) # MAKING A CHARACTER STATS, 100 HEALTH, ARMOR 20, 20 SIDED DICE, ATTACK DICE OF 6
terentatek1 = Entity(8, 3, 20, 4, 1) # MAKING ENEMY STATS, 40 HEALTH, 1 ARMOR, 20 SIDED DICE, ATTACK DICE OF 8
terentatek2  = Entity(8, 3, 20, 4, 1) # MAKING ENEMY STATS, 40 HEALTH, 1 ARMOR, 20 SIDED DICE, ATTACK DICE OF 8
	# def __init__(self, health, armor, twenty_sided_dice, attack_dice, strength_modifier):
class Scene(object):
	def enter(self):
		print ("This scene is not yet configured. Subclass it and implement enter().")
		exit(1)
		
class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		# BE SURE TO PRINT OUT THE LAST SCENE
		current_scene.enter()	
		
class Death(Scene):
	quips = [
	"You died, are you sad yet.",
	"Why continue?",
	"DIED!!!",
	"Get good son."
	]
	
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)-1)])
		exit(1)	
		
# MAIN CORRIDOR
class CentralCorridor(Scene):
	def enter(self):
		player.print_stats() # PRINTING OUT THE PLAYERS STATS
		
		print ("You are about to become a true Sith.")
		print ("The problem is you need to go retrive a lightsaber.")
		print ("Ahead of you there are three doors.")
		action = input("1.Left door \n2.Middle door\n3.Right door\n> ")
		if action == 1:
			print ("\nYou turn left, and begin to enter into the room.\n")
			time.sleep(1)
			return 'towerOfHanoi'
		elif action == 2:
			print ("\nYou feel a stinging, but walk through the ominious door.\n")
			time.sleep(1)
			return 'riverOfAcid'
		elif action == 3:
			print ("\nHorrible screeches are heard, but there is a need to press on.")
			time.sleep(1)
			return 'terrorRoom'
		else:
			print ("What are you even doing!")
			return 'central_corridor'
# CLASS DEFINING THE ROOM THAT HAS ACID IN IT.
class RiverOfAcid(Scene):
	def enter(self):
		# GLOBAL VARIABLES TO BE USED
		global grenade
		global riverIced
	
		while True:
			if riverIced == False:
				
				self.no_ice_message()
				
				# OPTION IF COLD EXIST WITHIN GRENADE, AND FIRE IS NOT.
				if 'cold' in grenades and 'fire' not in grenades:
					self.river_options_cold_only()
					choice = input(">")
					print ("\n")
					# CHOICE IF THEY DECIDE TO THROW THE GRENADE
					if choice == 1:
					
						print ('You throw the grenade, immediately the ice ripples from where it hit.')
						print ('Branching to the edges of the river in a thick sheet of ice.')
						print ('It seems that a person would be able to walk over it.\n')
						
						riverIced = True 	
						return self.cross_river()
					# IF THEY DECIDE TO WALK AWAY.
					elif choice == 2:
						return 'central_corridor'
						
					# IF UNLISTED CHOICE CHOOSEN
					else:
						print ("Do not know what that means.")
						
				# IF COLD NOT AVAIABLE, BUT FIRE IS
				elif 'cold' not in grenades and 'fire' in grenades:
					self.river_options_fire_only()
					choice = input(">")
					print ('\n')
					
					# CHOICE IF THEY DECIDE TO THROW GRENADE
					if choice == 1:
						print ("You launch the grenede into the bubbling acid river.")
						print ("A rumbling starts to occur.")
						print ("The whole river lights up in a spectacular fireball.\n")
						return 'death'
					
					# IF THEY WALK AWAY 
					elif choice == 2:
						return 'central_corridor'
					
					# UNKNOWN COMMAND
					else:
						print ("Do not know what that means.")
					
				# BOT GRENADES ARE IN	
				elif 'cold' in grenades and 'fire' in grenades:
					self.river_options_both()
					choice = input(">")
					print ("\n")
					
					# CHOICE IF THEY DECIDE TO THROW THE COLD GRENADE
					if choice == 1:
					
						print ('You throw the grenade, immediately the ice ripples from where it hit.')
						print ('Branching to the edges of the river in a thick sheet of ice.')
						print ('It seems that a person would be able to walk over it.')
						riverIced = True
						return self.cross_river()
											
					# CHOICE IF THEY DECIDE TO THROW THE FIRE GRENADE
					elif choice == 2:
						print ("You launch the grenede into the bubbling acid river.")
						print ("A rumbling starts to occur.")
						print ("The whole river lights up in a spectacular fireball.")
						return 'death'
						
					# IF THEY WALK AWAY 
					elif choice == 3:
						return 'central_corridor'
					
					# UNKNOWN COMMAND
					else:
						print ("Do not know what that means.")
			
				elif grenades == []:
				
					# DISPLAY CURRENT OPTIONS
					self.river_options_emptylist()
				
					choice = input(">")
					print ("\n")
					# IF STATEMENT EITHER SENDING CHARACTER TO CENTRAL_CORRIDOR OR NOT UNDERSTANDING WHAT WAS WRITTEN.
					if choice == 1:
						return 'central_corridor'
				
					else:
						print ('Do not know what that is.')
			
			elif riverIced == True:
				self.ice_message()
				return self.cross_river()
				
	
	# OTHER DEFININTIONS IN RIVEROFACID
	
	def cross_river(self):
		print ("Do you wish to walk over?")
		action = input("1.Yes\n2.No\n>")
		if action == 1:
			return 'lightsaber_room'
		
		elif action == 2:
			return 'central_corridor'
		
		else:
			return 'riverOfAcid'
	
	# GIVING OPTION TO THROW ICE GRENADE
	def river_options_cold_only(self):
		print ('1. Throw cold grenade')
		print ('2. Walk away')
	
	# GIVING OPTION TO THROW FIRE GRENADE
	def river_options_fire_only(self):
		print ('1. Throw fire grenade')
		print ('2. Walk away')

	# GIVING OPTION TO THROW GRENADES OR WALK AWAY
	def river_options_both(self):
		print ('1. Throw cold grenade')
		print ('2. Throw fire grenade')
		print ('3. Walk away')
	
	# ALLOWING PlAYER TO WALK AWAY
	def river_options_emptylist(self):
		print ("\n1. Walk away")
	
	def ice_message(self):
		print ("The river has been frozen, allowing for someone to walk over it.")
		
	def no_ice_message(self):
		print ("A large room with a river of acid flows through it.")
		print ("Too dangerous to simply walk through.")
		print ("If only there was some sort of way to walk over the river.\n")
		
		
# CLASS DEFINING ROOM THAT HAS MONSTERS
class TerrorRoom(Scene):
	def enter(self):
		global alreadyEnteredRoom
		if alreadyEnteredRoom == False:
			print ("\nTwo hulking behemoths are standing wtihin the room.")
			print ("They reek of death.")
			print ("They stand infront of a door.")
			print ("Looks like you need to defeat them in order to proceed.\n")
			alreadyEnteredRoom = True
			
		# TWENTY SIDED DICE
		player.get_twenty_sided_dice()

		# GRABBING PLAYER STATS
		player.get_health()
		player.get_strength_modifier()
		player.get_attack_dice()
		player.get_armor()
	
		# TERENTATEK STATS	 
		terentatek1.get_strength_modifier()
		terentatek1.get_armor()
		terentatek1.get_attack_dice()
		
		# TERENTATEK1 STAT 
		terentatek1.get_health()
		
		# TERENTATEK2 STAT 
		terentatek2.get_health()

		# terentatek1.print_stats()
		# terentatek2.print_stats()

		repeat = True

		while repeat:
			if terentatek1.get_health() > 0 and terentatek2.get_health() > 0:
				if player.get_health() <= 0: 
					return 'death'
					repeat = False
				else:
					print ("\nBoth are alive!")
					self.first_terentatek_attempt()
					self.second_terentatek_attempt()
					self.options()
					return self.players_turn_both()
			elif terentatek1.get_health() <= 0 and terentatek2.get_health() > 0:
				if player.get_health() <= 0: 
					return 'death'
					repeat = False
				else:
					print ("\nThe second Terentatek is alive!")
					self.second_terentatek_attempt()
					self.options_second_only()
					return self.players_turn_second() 
			elif terentatek1.get_health() > 0 and terentatek2.get_health()<= 0:
				if player.get_health() <= 0: 
					return 'death'
					repeat = False
				else:
					print ("\nThe first Terentatek is alive!")
					self.first_terentatek_attempt() 
					self.options_first_only()
					return self.players_turn_first()
			else: 
				print ("\nBoth have been defeated!")
				return 'landOfIceAndFire'
	
	def players_turn_both(self):
		action = input(">")
		
		if action == 1:
			print ("-----Player Attacks First Terentatek-----")
			if player.chance_to_hit():
				damage = player.attack_dice_roll()
				
				print ("HIT: - %d" % damage)
				terentatek1.health_remover(damage)
				print ("First Terentatek HEALTH: %s" % terentatek1.get_health())
				if terentatek1.get_health() < 0:
					print ("First Terentatek died")
				return "terrorRoom"
			else:
				print ("MISS")
				return ("terrorRoom")
		elif action == 2:	
			print ("-----Player Attacks Second Terentatek-----")
			if player.chance_to_hit():
				damage = player.attack_dice_roll()
				
				print ("HIT: - %d" % damage)
				terentatek2.health_remover(damage)
				print ("Second Terentatek HEALTH: %s" % terentatek2.get_health())
				if terentatek2.get_health() < 0:
					print ("Second Terentatek died")
				return "terrorRoom"
			else:
				print ("MISS")
				return ("terrorRoom")
		
		elif action == 3:
			return 'central_corridor'
		
		else:
			print ("No action taken!!!")	
			return "terrorRoom"

	def players_turn_first(self):
		action = input(">")
			
		if action == 1:
			print ("-----Player Attacks First Terentatek-----")
			if player.chance_to_hit():
				damage = player.attack_dice_roll()
				
				print ("HIT: - %d" % damage)
				terentatek1.health_remover(damage)
				print ("First Terentatek HEALTH: %s" % terentatek1.get_health())
				if terentatek1.get_health() < 0:
					print ("First Terentatek died")
				return "terrorRoom"	
			else:
				print ("MISS"	)
				return ("terrorRoom")
						
		elif action == 2:
			return 'central_corridor'
			
		else:
			print ("No action taken!!!")	
			return "terrorRoom"	

	def players_turn_second(self):
		action = input(">")
			
		if action == 1:
			print ("\n-----Player Attacks Second Terentatek-----")
			if player.chance_to_hit():
				damage = player.attack_dice_roll()
				
				print ("HIT: - %d" % damage)
				terentatek2.health_remover(damage)
				print ("Second Terentatek HEALTH: %s" % terentatek2.get_health())
				if terentatek2.get_health() < 0:
					print ("Second Terentatek died")
				return "terrorRoom"	
			else:
				print ("MISS"		)
				return ("terrorRoom")
							
		
		elif action == 2:
			return 'central_corridor'
		
		else:
			print ("No action taken!!!")	
			return "terrorRoom"

	# DEFINITION WILL DO THE FIRST TERENTAEK TURN IN ATTACKING THE PLAYER CHARACTER		
	def first_terentatek_attempt(self):
		print ("\n-----First Terentatek Attacks-----")
		time.sleep(1)
		if terentatek1.chance_to_hit():
			damage = terentatek1.attack_dice_roll()
			
			print ("HIT: - %d" % damage)
			player.health_remover(damage)
			print ("PLAYER HEALTH: %s" % player.get_health())		
		else:
			print ("MISS")
			print ("PLAYER HEALTH: %s" % player.get_health())				
			
	# DEFINITION WILL DO THE SECOND TERENTAEK TURN IN ATTACKING THE PLAYER CHARCTER.
	def second_terentatek_attempt(self):
		print ("\n-----Second Terentatek Attacks-----")
		time.sleep(1)
		if terentatek2.chance_to_hit():
			damage = terentatek2.attack_dice_roll()
			
			print ("HIT: - %d" % damage)
			player.health_remover(damage)
			print ("PLAYER HEALTH: %s" % player.get_health())
			
		else:
			print ("MISS")
			print ("PLAYER HEALTH: %s" % player.get_health())		

	def options(self):
		print ("\n1. Attack first terentatek")
		print ("2. Attack second terentatek")
		print ("3. Run Away")
		
	def options_first_only(self):
		print ("\n1. Attack first terentatek")
		print ("2. Run Away")
	
	def options_second_only(self):
		print ("\n1. Attack second terentatek")
		print ("2. Run Away")
	
	
# CLASS THAT HAS TWO GRANADES IN PILLARS TO BE CHOSEN
class IceAndFire(Scene):
	def enter(self):
		print ("\nWithin the room lies a two large cyclinders.")
		
		while True:
		
			if cyclinder_left != [] and cyclinder_right != []:
				self.menu_for_both_pillars_full()
				
				choice = input(">")
				
				if choice == 1:
					self.remove_cold_grenade()
					
				elif choice == 2:
					self.remove_fire_grenade()
				
				elif choice == 3: 
					return 'central_corridor'
				
				else:
					print ("NO NO NO")
			elif cyclinder_left != [] and cyclinder_right == []:
				self.menu_for_cold_left()
				
				choice = input(">")
				
				if choice == 1:
					self.remove_cold_grenade()
				
				elif choice == 2: 
					return 'central_corridor'
				
				else:
					print ("NO NO NO")
			
			elif cyclinder_left == [] and cyclinder_right != []:
				self.menu_for_fire_left()
				
				choice = input(">")
				
				if choice == 1:
					self.remove_fire_grenade()
					
				elif choice ==2:
					return 'central_corridor'
				
				else:
					print ("NO NO NO")
			else: 
				self.menu_for_neither_there()
				
				choice = input(">")
				
				if choice == 1:
					return 'central_corridor' # CHANGE TO terrorRoom
				else:
					print ("There is nothing to do here now.")
	# FEEDBACK TO PLAYER SO THEY KNOW THAT THEY HAVE COLLECTED ITEMS
	def for_Loop_Display(self, pillar):
		print ("Grenades:",)
		for item in grenades:
			print (item + "",)
		print ("\n")
		
	# REMOVING THE FIRE GRENADE FROM THE RIGHT CYCLINDER LIST
	def remove_fire_grenade(self):
		global grenades
		global cyclinder_left
		global cyclinder_right
		
		cyclinder_right.remove('fire')
		grenades.append("fire")
		self.for_Loop_Display(grenades)
		
	
	# REMOVING THE COLD GRENADE FROM THE LEFT CYCLINDER LIST	
	def remove_cold_grenade(self):
		global grenades
		global cyclinder_left
		global cyclinder_right	
		
		cyclinder_left.remove("cold")
		grenades.append("cold")
		self.for_Loop_Display(grenades)
	
	# DISPLAYING THE MENU THAT HAS BOTH PILLARS FILLED WITH ITEMS
	def menu_for_both_pillars_full(self):
		print ("The left cyclinder holds a grenade, it eminates a chill.")
		print ("The right cyclinder holds another grenade, hot to the touch.\n")
		
		print ("1. Take the cold grenede.")
		print ("2. Take the fire grenade.")
		print ("3. Walk away from the cyclinders.")
		
		
	# DISPLAYING THE MENU THAT HAS ONLY THE FIRE GRENADE REMAINING	
	def menu_for_fire_left(self):
		print ("The right cyclinder holds another grenade, hot to the touch.")
		print ("1. Take the fire grenade.")
		print ("2. Walk away from the cyclinders.")
	
	# DISPLAYING THE MENU THAT HAS ONLY THE COLD GRENADE REMAINING
	def menu_for_cold_left(self):
		print ("The left cyclinder holds a grenade, it eminates a chill.")
		print ("1. Take the cold grenade.")
		print ("2. Walk away from the cyclinders.")
	# DISPLAYING THE MENU WHEN NO GRANADES REMAIN 
	def menu_for_neither_there(self):
		print ("Nothing more to collect from the room.")
		print ("1. Walk away from the cyclinders.")
		
# CLASS THAT DEFINES THE LIGHTSABERROOM
class LightsaberRoom(Scene):
	
	def enter(self):
		print ("\nWould you look at that, a large map!")
		print ("Seems to be coordinates for something.")
		print ("Around the room is a container.")
		
		while True:
			action = input("1.Approach\n2.Leave\n3.Investigate\n>")
			return self.overall_choice(action)
		
	def overall_choice(self, action):
		if action == 1:
			return self.approach_option()
		
		elif action == 2:
			return 'riverOfAcid'
		
		elif action == 3:
			return self.investigate_option()
	
	
	def approach_option(self):	
		print ("The container opens by itself.")
		print ("An eminating darkness comes from within the container.")
	
		choice = input("1.Reach in\n2.Kick it\n>")
		return self.container_options(choice)
		
	def container_options(self, choice):
		if choice == 1:
			print ('You grasp the sith lightsaber, filling you with hate; your power 10 folds.')
			print ('You are now considered a True Sith.')
			return 'finished'
		
		elif choice == 2:
			print ("You kick the container.")
			print ("A sudden jolt and a flash of light is seen.")
			print ("The lightsaber is in your chest.")
			return 'death'
		else:
			print ("How about a real choice?")
			
	def investigate_option(self):
		print ("Pulses in response to being proped at.")
		print ("The map when completed leads to an Unknown Sector of Space.")
		return "lightsaber_room" 
		
# CLASS THAT DEFINES THE TOWEROFHANOIROOM		
class TowerOfHanoiRoom(Scene):
	def enter(self):	
		global towerOfHanoiCompleted
		global inventory
		# IF THIS ROOM HAS BEEN COMPLETED INFORM THE PLAYER AND LET THEM MAKE A CHOICE
		if towerOfHanoiCompleted == True:
			print ("Looks like there is nothin else in the room")
			print ("1. Stare as pillars that once held energy.")
			print ("2. Leave the room.")
			choice = input(">")
			print ('\n')
			
			if choice == 1:
				return 'towerOfHanoi'
				
			elif choice == 2:
				return 'central_corridor'
			
			else:
				print ("Might as well stare at the pillars a little long.")
				print ("Not like there is anything more important to do.")
				return 'towerOfHanoi'
				
		# IF THE ROOM HAS NOT BEEN COMPLETED GIVE THE PLAYER CHOICES.
		else:
			# NOTICE THE PILLARS 
			print ("You see three pillars of energy within the room.")
			print ("There seems to be a console.")
			action = input("1.Approach\n2.Hack\n3.Walk away\n>") # GETTING AN ACTION
			
			# CREATING THE LISTS FOR PILLARS
			left_pillar = ["bottom", "lower-mid", "upper-mid", "top"] # FILLING LEFT_PILLAR WITH ENERGY BANDS
			middle_pillar = [] # CREATE A MIDDLE_PILLAR
			right_pillar = [] # CREATE A RIGHT_PILLAR
			if action == 1:
			# Printing out the rules for the game
				self.rules()
				# Looping the possible menus options
				while True:
					# Menu for if only left_pillar has bands
					if left_pillar != [] and middle_pillar == [] and right_pillar == []:
						
						# Menu telling options 
						self.choices_for_left_full()
				
						choice = input(">")
						print ('\n')
						if choice == 1:
							# Opening up submenu for actions from left pillar
							self.move_from_left(left_pillar, middle_pillar, right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 2:
							self.reset_systems(left_pillar,middle_pillar,right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 3:
							return 'central_corridor'
						
						elif choice == 4:
							self.rules()
							
						else:
							print ("Why don't you try again?")
					# Menu for if left_pillar and middle_pillar has a band
					elif left_pillar != [] and middle_pillar != [] and right_pillar == []:
						self.choices_for_left_middle_full()
					
						choice = input(">")
					
						if choice == 1:
							self.move_from_left()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 2:
							self.move_from_middle()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 3:
							self.reset_systems(left_pillar, middle_pillar, right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 4:
							return 'towerOfHanoi'
						
						elif choice == "5":
							self.rules()
						
						else: 
							pass
				
					# Menu for if left_pillar and right_pillar has bands 
					elif left_pillar != [] and middle_pillar == [] and right_pillar != []:
						self.choices_for_left_right_full()
					
						choice = input(">")
					
						if choice == 1:
							self.move_from_left()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 2:
							self.move_from_right()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 3:
							self.reset_systems(left_pillar, middle_pillar, right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 4:
							return 'room'
						
						elif choice == 5:
							self.rules()
						
						else: 
							pass
					# Menu for if left_pillar, middle_pillar, and right_pillar has bands 
					elif left_pillar != [] and middle_pillar != [] and right_pillar != []:
					
						self.choices_for_left_middle_right_full()
				
						choice = input(">")
					
						if choice == 1:
							self.move_from_left()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 2:
							self.move_from_middle()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 3:
							self.move_from_right()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 4:
							self.reset_systems(left_pillar, middle_pillar, right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 5:
							return 'room'
						
						elif choice == 6:
							self.rules()
						
						else: 
							pass
					# Menu for if middle_pillar and right_pillar have bands
					elif left_pillar == [] and middle_pillar != [] and right_pillar != []:
					
						#choices_for_middle_right_full()
						choice = input(">")
					
						if choice == 1:
							self.move_from_middle()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 2:
							self.move_from_right()
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 3:
							self.reset_systems(left_pillar, middle_pillar, right_pillar)
							self.displaying_Current(left_pillar, middle_pillar, right_pillar)
						elif choice == 4:	
							return 'room'
						
						elif choice == 5:
							self.rules()
						
						else: 
							pass
					# Menu for if only right_pillar has bands 
					else:
						print ("A cyclinder shoots out of the ground in spectacular fashion.")
						print ("It twists open revealing a handcrafted sword.")
						print ("An evil auroa emminates from it.")
						choice = input(">")
						
						print ('\n')
						
						if choice == 'take':
							NagaShadowSwordBonus = 4
							inventory.add("Naga Shadow Sword") # ADD THING TO INVENTORY
							player.strength_modifier_add(NagaShadowSwordBonus)
						else:
							print ('The sword disappears in cloud smoke.')
						
						towerOfHanoiCompleted = True
						time.sleep(2)
						return 'central_corridor'
			elif action == 2:
			# THINGS THAT HAPPENS WHEN THE PLAYER DECIDES TO HACK
				print ("Trying to be elite haxor is risky buisness")
				time.sleep(2)
				return 'death'
			elif action == 3:
				time.sleep(2)
				return 'central_corridor'
			
			else:
				time.sleep(2)
				return 'towerOfHanoi'
	# MENU FOR WHEN LEFT_PILLAR IS ONLY ONE THAT HAS BANDS IN IT	
	def choices_for_left_full(self):
		print ("\n1. Move system from left pillar")
		print ("2. Reset system")
		print ("3. Walk away")
		print ("4. Reread rules.")
		
	# MENU FOR WHEN LEFT_PILLAR AND RIGHT_PILLAR HAS BANDS IN IT	
	def choices_for_left_right_full(self):
		print ("\n1. Move system from left pillar")
		print ("2. Move system from right pillar")
		print ("3. Reset system")
		print ("4. Walk away")
		print ("5. Reread rules.")		
	# MENU FOR WHEN LEFT_PILLAR AND RIGHT_PILLAR HAS BANDS IN IT	
	def choices_for_left_middle_full(self):
		print ("\n1. Move system from left pillar")
		print ("2. Move system from middle pillar")
		print ("3. Reset system")
		print ("4. Walk away")
		print ("5. Reread rules.")		
	# MENU FOR WHEN LEFT_PILLAR, MIDDLE_PILLAR, AND RIGHT_PILLAR HAVE BANDS IN IT.	
	def choices_for_left_middle_right_full(self):
		print ("\n1. Move system from left pillar")
		print ("2. Move system from middle pillar")
		print ("3. Move system from right pillar")
		print ("4. Reset system")
		print ("5. Walk away")
		print ("6. Reread rules.")
			
	# MENU FOR WHEN MIDDLE_PILLAR AND RIGHT_PILLAR HAVE BANDS IN IT
	def choices_for_middle_right_full(self):
		print ("\n1. Move system from middle pillar")
		print ("2. Move system from right pillar")
		print ("3. Reset system")
		print ("4. Walk away")
		print ("5. Reread rules.")
	def rules(self):
		print ("\n3 pillars, four bands of energy. To continue all four bands")
		print ("must be moved to the right pillar.\n")
		print ("TOP SYSTEM: May be moved without fear.")
		print ("MID-UPPER SYSTEM: Cause overload when transferred to pilar with active TOP SYSTEM.")
		print ("LOWER-UPPER SYSTEM: May be transfered to pillar or no active BASE SYSTEM.")
		print ("BASE SYSTEM: Can only be transferred to nonactive system.")
		print ("A system my only be transferred to another pillar if it is the only")
		print ("active system on that pillar or it is the LAST one listed.")
	
	# FUNCTION TO RESET GAME BACK TO BEGINING
	def reset_systems(self, left_pillar, middle_pillar, right_pillar):
		middle_pillar = []
		left_pillar = [1,2,3,4]
		right_pillar = []
		return middle_pillar, left_pillar, right_pillar

	# FUNCTION FOR MOVING ENERGY BAND FROM LEFT PILLAR
	def move_from_left(self, left_pillar, middle_pillar, right_pillar):
		print ("Chose where you want to place %s" % left_pillar[-1])
		print ("1. Move to middle pillar")
		print ("2. Move to right pillar")
		print ("3. Cancel action ")
		choice = input(">")
		if choice == 1:
			print ("Move to Middle")
			# SAVING LAST IN LEFT LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN LEFT LIST
		
		elif choice == 2:
			print ("Move to Right")
			# SAVING LAST IN LEFT LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN LEFT LIST 
			
			
		elif choice == 3:
			# SENDING BACK TO THE PRIOR METHOD
			return 
		
		else:
			print ("What are you doing")
	# FUNCTION FOR MOVING ENERGY BAND FROM MIDDLE PILLAR	
	def move_from_middle(self, left_pillar, middle_pillar, right_pillar):
		print ("Choose where you want to place %s" % middle_pillar[-1])
		print ("1. Move to left pillar")
		print ("2. Move to right pillar")
		print ("3. Cancel action")
		choice = input(">")
		if choice == 1:
			print ("Move to Left")
			# SAVING LAST IN MIDDLE LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN MIDDLE LIST
		
		elif choice == 2:
			print ("Move to Right")
			# SAVING LAST IN MIDDLE LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN MIDDLE LIST
		
		elif choice == 3:
			# SENDING BACK TO PRIOR METHOD
			return
		
		else:
			print ("What are you doing?")
	# FUNCTION FOR MOVING ENERGY BAND FROM RIGHT PILLAR
	def move_from_right(self, left_pillar, middle_pillar, right_pillar):
		print ("Choose where you want to place %s" % right_pillar[-1])
		print ("1. Move to left pillar")
		print ("2. Move to middle pillar")
		print ("3. Cancel action")
		choice = input(">")
		if choice == 1:
			print ("Move to Left")
			# SAVING LAST IN RIGHT LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN RIGHT LIST
		
		elif choice == 2:
			print ("Move to Middle")
			# SAVING LAST IN RIGHT LIST
			# APPLYING LAST IN LIST TO PROPER INDEX
			# REMOVING LAST IN RIGHT LIST
		
		elif choice == 3:
			# SENDING BACK TO PRIOR METHOD
			return 
		
		else:
			print ("What are you doing?")
	
	def displaying_Current(self, left_pillar, middle_pillar, right_pillar):
		self.for_Loop_Display(left_pillar)
		self.for_Loop_Display(middle_pillar)
		self.for_Loop_Display(right_pillar)
	
	def for_Loop_Display(self, pillar):
		print ("\nActive:")
		for item in pillar:
			print (item,)
	
class Finished(Scene):
	def enter(self):
		print ("\nYou are done.\n")
		return 'finished'
		
class Map(object):
	scenes = {
	'central_corridor': CentralCorridor(),
	'riverOfAcid': RiverOfAcid(),
	'terrorRoom': TerrorRoom(),
	'towerOfHanoi': TowerOfHanoiRoom(),
	'landOfIceAndFire': IceAndFire(),
	'lightsaber_room': LightsaberRoom(),
	'death': Death(),
	'finished': Finished(),
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	def opening_scene(self):
		return self.next_scene(self.start_scene)
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()