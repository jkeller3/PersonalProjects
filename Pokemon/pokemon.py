import time
import numpy as np
import sys

# Delay printing

def delay_print(s):
	# print one character at a time
	# https://stackoverflow.com/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)

# Create the class
class Pokemon:
	def __init__(self, name, type1, moves, EVs):
		# save variables as attributes
		self.name = name
		self.type1 = type1
		self.moves = moves
		self.attack = EVs['ATTACK']
		self.defense = EVs['DEFENSE']
		self.cHealth = 20
		self.mHealth = 20

	def displayHealth(self, Pokemon2):
		# Print the health of each pokemon
		print(f"\n{self.name}\t\tHLTH\t{self.cHealth}/{self.mHealth}")
		print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.cHealth}/{Pokemon2.mHealth}")

	def displayInfo(self, Pokemon2):
		# Print fight information
		print("-----POKEMON BATTLE-----")
		print(f"\n{self.name}")
		print("TYPE/", self.type1)
		print("ATTACK/", self.attack)
		print("DEFENSE/", self.defense)
		print("LVL/", 3*(1+np.mean([self.attack,self.defense])))
		print("\nVS")
		print(f"\n{Pokemon2.name}")
		print("TYPE/", Pokemon2.type1)
		print("ATTACK/", Pokemon2.attack)
		print("DEFENSE/", Pokemon2.defense)
		print("LVL/", 3*(1+np.mean([Pokemon2.attack,Pokemon2.defense])))
		time.sleep(2)

	def isEffective(self, Pokemon2):
		# Consider type advantages
		version = ['Fire', 'Water', 'Grass']
		for i,k in enumerate(version):
			if self.type1 == k:
				if Pokemon2.type1 == k or  Pokemon2.type1 == version[(i+1)%3]:
					damage = self.attack - Pokemon2.defense
					delay_print(f"\nAttack did {damage} damage. Its not very effective...")


				elif Pokemon2.type1 == version[(i+2)%3]:
					damage = (self.attack - Pokemon2.defense) * 2
					delay_print(f"\nAttack did {damage} damage. Its super effective!")

				else:
					damage = self.attack - Pokemon2.defense
					delay_print(f"\nAttack did {damage} damage.")
		Pokemon2.cHealth -= damage




	def isFainted(self, Pokemon2):
		if(Pokemon2.cHealth <= 0):
			delay_print(f"\n{Pokemon2.name} has fainted!")

	def chooseAttack(self, Pokemon2):
		for i, x in enumerate(self.moves):
			print(f"{i+1}", x)
		index = int(input('Pick a move: '))
		delay_print(f"\n{self.name} used {self.moves[index-1]}!")
		time.sleep(1)

	def fight(self, Pokemon2):
		# Allow two pokemon to fight each other
		self.displayInfo(Pokemon2)
		
		# Now for the actual fighting...f
		# Continue while pokemon still have health
		while (self.cHealth > 0) and (Pokemon2.cHealth > 0):
			self.displayHealth(Pokemon2)

			print(f"Go {self.name}!")
			
			self.chooseAttack(Pokemon2)

			self.isEffective(Pokemon2)

			self.displayHealth(Pokemon2)

			self.isFainted(Pokemon2)

			# Pokemon2s turn
			print(f"Go {Pokemon2.name}!")
			Pokemon2.chooseAttack(Pokemon2)

			# Determine damage
			Pokemon2.isEffective(self)

			Pokemon2.displayHealth(self)

			Pokemon2.isFainted(self)

		money = np.random.choice(5000)
		delay_print(f"Opponent paid you ${money}.")



if __name__ == '__main__':
	# Create Pokemon
	Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
	Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK': 10, 'DEFENSE': 10})
	Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Whip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK': 8, 'DEFENSE': 12})


	Charizard.fight(Blastoise) # Get them to fight



