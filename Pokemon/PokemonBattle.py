import time
import sys
import numpy as np
import random
# Delay printing

def delay_print(s):
	# print one character at a time
	# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)

# Create the class
class Battle:
	def __init__(self, pPokemon, ePokemon):
		pass

	def displayHealth(pPokemon, ePokemon):
		# Print the health of each pokemon
		print(f"\n{pPokemon.name}\tHLTH\t{pPokemon.chp}/{pPokemon.hp}")
		print(f"{ePokemon.name}\t\tHLTH\t{ePokemon.chp}/{ePokemon.hp}")

	def displayInfo(pPokemon, ePokemon):
		# Print fight information
		print("-----POKEMON BATTLE-----")
		print(f"\n{pPokemon.name}")
		print("TYPE/", pPokemon.types)
		print("ATTACK/", pPokemon.attack)
		print("DEFENSE/", pPokemon.defense)
		print("LVL/", pPokemon.level)
		print("\nVS")
		print(f"\n{ePokemon.name}")
		print("TYPE/",ePokemon.types)
		print("ATTACK/",ePokemon.attack)
		print("DEFENSE/",ePokemon.defense)
		print("LVL/", ePokemon.level)
		time.sleep(2)

	def damageCalcs(self, pPokemon, attack, ePokemon):
		stabmultiplier = self.stab(self, pPokemon.types, attack.type)
		effectivemultiplier = self.checkChart(self, pPokemon, attack.type, ePokemon)
		crit = self.checkCrit(self)
		# random modifier to add variance to damage calculations
		randmod = random.randint(217,255) / 255
		damage = int(((((2*pPokemon.level)/5+2) * (attack.power * (pPokemon.attack / ePokemon.defense)))/50 + 2) * stabmultiplier * effectivemultiplier * crit * randmod)
		print(f"It's attack did {damage} damage.")
		ePokemon.chp -= damage
		if(ePokemon.chp<0):
			ePokemon.chp=0

	def stab(self, ptype, atype):
		multiplier = 1
		for i in ptype:
			if i == atype:
				print('\nYou got a STAB boost!')
				multiplier = 1.5
		return multiplier

	def checkChart(self, pPokemon, atype, ePokemon):
		multiplier = 1
		for i in ePokemon.weaknesses:
			if i == atype:	
				multiplier *= 2

		for i in ePokemon.resistances:
			if i == atype:
				multiplier = multiplier / 2

		if(ePokemon.immunities):
			for i in ePokemon.immunities:
				if i == atype:
					multiplier = 0

		if(multiplier > 1):
			print(f"\nIt's super effective!")

		elif(multiplier == 0):
			print(f"\nIt doesn't effect {ePokemon.name}.")

		elif(multiplier < 1):
			print(f"\nIt's not very effective.")

		return multiplier

	def checkCrit(self):
		num = random.randint(1, 16)
		# 1 in 16 percent chance of crit
		if num == 16:
			print("\nIt's a critical hit!")
			return 2
		else:
			return 1

	def isFainted(self, pokemon):
		if(pokemon.chp <= 0):
			delay_print(f"\n{pokemon.name} has fainted.")

	def chooseAttack(self, pPokemon):
		for i, x in enumerate(pPokemon.moves):
			print(f"{i+1}", x)
		index = int(input('Pick a move: '))
		return index-1

	def printAttack(self, pokemon, attack):
		delay_print(f"\n{pokemon.name} used {attack}.")
		time.sleep(1)

	def battleOutcome(victory):
		money = np.random.choice(5000)
		if(victory):
			delay_print(f" You have won the battle!")
			delay_print(f"\nOpponent paid you ${money}.")
		else:
			delay_print(f" You have lost the battle.")
			delay_print(f"\nPay opponent ${money}.")

	def fight(self, pPokemon, ePokemon):
		# Allow two pokemon to fight each other
		self.displayInfo(pPokemon, ePokemon)
		
		print(f"Go {pPokemon.name}!")

		# Now for the actual fighting...
		# Continue while pokemon still have health
		while (pPokemon.chp > 0) and (ePokemon.chp > 0):
			self.displayHealth(pPokemon, ePokemon)
			atkChoice = self.chooseAttack(self, pPokemon)
			if(pPokemon.speed > ePokemon.speed):
				self.printAttack(self, pPokemon, pPokemon.moves[atkChoice])
				self.damageCalcs(self, pPokemon, pPokemon.moves[atkChoice], ePokemon)
				self.displayHealth(pPokemon, ePokemon)
				self.isFainted(self, ePokemon)
				if(ePokemon.chp>0):
					self.printAttack(self, ePokemon, ePokemon.moves[0])
					self.damageCalcs(self, ePokemon, ePokemon.moves[0], pPokemon)
					self.displayHealth(pPokemon, ePokemon)
					self.isFainted(self, ePokemon)
			else:
				self.printAttack(self, ePokemon, ePokemon.moves[0])
				self.damageCalcs(self, ePokemon, ePokemon.moves[0], pPokemon)
				self.displayHealth(pPokemon, ePokemon)
				self.isFainted(self, ePokemon)
				if(pPokemon.chp>0):
					self.printAttack(self, pPokemon, pPokemon.moves[atkChoice])
					self.damageCalcs(self, pPokemon, pPokemon.moves[atkChoice], ePokemon)
					self.displayHealth(pPokemon, ePokemon)
					self.isFainted(self, ePokemon)
			# Need to implement random for AI attack
		if(pPokemon.chp == 0):
			self.battleOutcome(False)
		if(ePokemon.chp == 0):
			self.battleOutcome(True)	