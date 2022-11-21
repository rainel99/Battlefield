
from abc import ABC, abstractmethod
from asyncio.unix_events import DefaultEventLoopPolicy

from Soldier import Soldier
from Soldier import Soldier
from enum import IntEnum

class EnumAttribute(IntEnum):
	Low = 0
	Medium = 1
	High = 2

class Characteristics(ABC):
    @abstractmethod
    def aplly_buff(self, soldier : Soldier, enum_attribute : EnumAttribute):
        pass


class Experience(Characteristics):
	def apply_buff(self, soldier : Soldier):
		if soldier.age < 25:
			pass
		if soldier.age >= 25 and soldier.age < 40:
			pass
		if soldier.age >= 40:
			pass

class Morale(Characteristics):
	def aplly_buff(self, soldier: Soldier, enum_attribute: EnumAttribute):
		if enum_attribute == 0:
			pass
		if enum_attribute == 1:
			pass
		if enum_attribute == 2:
			pass	


class AdvantageousTerrain(Characteristics):
	def apply_buff(self, soldier : Soldier, enum_attribute : EnumAttribute):
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
	def apply_buff(self, soldier : Soldier, enum_attribute : EnumAttribute):
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
	def aplly_buff(self, soldier : Soldier, enum_attribute : EnumAttribute):
		if enum_attribute == 0:
			pass
		if enum_attribute == 1:
			pass
		if enum_attribute == 2:
			pass

class Agility(Characteristics):
	def aplly_buff(self, soldier: Soldier):
		soldier.speed += 10
		soldier.enery_regen += 20


class Strength(Characteristics):
	def aplly_buff(self, soldier: Soldier, enum_attribute: EnumAttribute):
		soldier.life_points += 30
		soldier.speed -=7



