import random


class Entity(object):

	def __init__(self, health, armor, twenty_sided_dice, attack_dice, strength_modifier):
		self.health = health
		self.armor = armor
		self.twenty_sided_dice = twenty_sided_dice
		self.attack_dice = attack_dice
		self.strength_modifier = strength_modifier
		
	def print_stats(self):
		print ("Current Status:",)
		print ("Health: %d," % self.get_health(),)
		print ("Armor: %d," % self.get_armor(),)
		print ("Twenty Sided Dice: %d," % self.get_twenty_sided_dice(),)
		print ("Attack Dice: %d" % self.get_attack_dice(),)
		print ("Strength Modifier: %d" % self.get_strength_modifier())
		print ("\n")
		
	
	
	def get_strength_modifier(self):
		return self.strength_modifier
		
	def get_health(self):
		return self.health
	
	def get_armor(self):
		return self.armor
	
	def get_twenty_sided_dice(self):
		return self.twenty_sided_dice
	
	def get_attack_dice(self):
		return self.attack_dice
	
	def chance_to_hit(self, twenty_sided_dice, armor, strength_modifier):
		chance = random.randint(1, twenty_sided_dice)
		
		if chance == 20:
			return True
		
		chance = chance + strength_modifier
		if chance >= armor:
			return True
		
		elif chance < armor:
			return False
		
	def attack_dice_roll(self, attack_dice, strength_modifier):
		attack_damage = random.randint(1, attack_dice)
		attack_damage = attack_damage + strength_modifier
		
		return attack_damage
		
	def health_remover(self, attack):
		self.health = self.health - attack
		
	def strength_modifier_add(self, value):
		self.strength_modifier = self.strength_modifier + value