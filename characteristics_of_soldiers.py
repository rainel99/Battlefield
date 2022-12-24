
from abc import ABC, ABCMeta, abstractmethod
from enum import Enum
import abc
#import Soldier

class EnumAttribute(Enum):
	Low = 0
	Medium = 1
	High = 2

class Characteristics(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_buff(self, soldier , enum_attribute : EnumAttribute):
        pass


class Experience(Characteristics):
	def apply_buff(self, soldier ):
		if soldier.age >= 27 and soldier.age < 30:
			soldier.incress_chance_crit(0.1)
		if soldier.age >= 30  and soldier.age < 33:
			soldier.incress_chance_crit(0.12)
			soldier.life_points -= 10

class Morale(Characteristics):
	def apply_buff(self, soldier, enum_attribute: EnumAttribute):
		if enum_attribute == 0:
			soldier.temamte_supp = True
		if enum_attribute == 1:
			soldier.temamte_supp = True
			soldier.incress_chance_crit(0.13)
		if enum_attribute == 2:
			soldier.temamte_supp = True
			soldier.incress_chance_crit(0.19)
			soldier.defense -= 10


class AdvantageousTerrain(Characteristics):
	def apply_buff(self, soldier , enum_attribute : EnumAttribute):
		if enum_attribute == 0:
			soldier.attack += soldier.attack *0.2
			soldier.defense += soldier.defense *0.2
		if enum_attribute == 1:
			soldier.attack += soldier.attack *0.5
			soldier.defense += soldier.defense *0.5
			soldier.attack_range +=1
		if enum_attribute == 2:
			soldier.attack += soldier.attack *0.8
			soldier.defense += soldier.defense *0.8
			soldier.attack_range += 3

class GoodArmament(Characteristics):
	def apply_buff(self, soldier , enum_attribute : EnumAttribute):
		if enum_attribute == 0:
			soldier.attack += 2
			soldier.defense += 2
		if enum_attribute == 1:
			soldier.attack+= 6
			soldier.defense+= 6
			soldier.speed += 3
		if enum_attribute == 2:
			soldier.attack+= 14
			soldier.defense+= 14
			soldier.speed+= 3
			soldier.energy+= 10



class AlliesOfConvenience(Characteristics):
	def apply_buff(self, soldier , enum_attribute : EnumAttribute):
		if enum_attribute == 0:
			pass
		if enum_attribute == 1:
			pass
		if enum_attribute == 2:
			pass

class Agility(Characteristics):
	def apply_buff(self, soldier, enum_attribute : EnumAttribute):
		soldier.speed += 10
		soldier.energy_regen += 20


class Strength(Characteristics):
	def apply_buff(self, soldier, enum_attribute: EnumAttribute):
		soldier.life_points += 30
		soldier.speed -=7

	
all_characteristics = {0 : Morale(), 1 : AdvantageousTerrain(), 2 : GoodArmament(), 3 : AlliesOfConvenience(), 4 : Agility() , 5 : Strength()}