# Where the Pokemon get made
# from PokemonAttacks import Attack
from PokemonTypes import *

class Pokemon:
	def __init__(self, id, name, types, level, hp, attack, defense, speed, moves):
		self.name = name
		self.id = id
		self.types = types
		self.level = level
		self.hp = hp
		self.chp = hp
		self.attack = attack
		self.defense = defense
		self.speed = speed
		self.moves = moves
		# self.alive = True
		self.typeChart()

	def __repr__(self):
		return f'Pokedex#: {self.id}\nName: {self.name}\nTypes: {self.types}\nLevel: {self.level}\nHP: {self.hp}\nAttack: {self.attack}\nDefense: {self.defense}\nSpeed: {self.speed}\nMoves: {self.moves}'


	def typeChart(self):
		self.weaknesses = []
		self.resistances = []
		self.immunities = []
		toRemove = []
		for i in self.types:
			if(i == 'Normal'):
				chart = Normal()
			if(i == 'Fire'):
				chart = Fire()
			if(i == 'Water'):
				chart = Water()
			if(i == 'Grass'):
				chart = Grass()
			if(i == 'Electric'):
				chart = Electric()
			if(i == 'Ice'):
				chart = Ice()
			if(i == 'Fighting'):
				chart = Fighting()	
			if(i == 'Poison'):
				chart = Poison()
			if(i == 'Ground'):
				chart = Ground()
			if(i == 'Flying'):
				chart = Flying()
			if(i == 'Psychic'):
				chart = Psychic()
			if(i == 'Bug'):
				chart = Bug()
			if(i == 'Rock'):
				chart = Rock()
			if(i == 'Ghost'):
				chart = Ghost()
			if(i == 'Dragon'):
				chart = Dragon()
			if(i == 'Dark'):
				chart = Dark()
			if(i == 'Steel'):
				chart = Steel()
			if(i == 'Fairy'):
				chart = Fairy()
			self.findWeaknesses(chart)

		for i in self.weaknesses:
			for j in self.resistances:
				if i == j:
					toRemove.append(i)


		for i in self.immunities:
			for j in self.weaknesses:
				if i == j:
					toRemove.append(i)
			for j in self.resistances:
				if i == j:
					toRemove.append(i)

		while(len(toRemove)>0):
			for i in self.weaknesses:
				if toRemove[0] == i:
					self.weaknesses.remove(i)
			for i in self.resistances:
				if toRemove[0] == i:
					self.resistances.remove(i)
			remove = toRemove[0]
			# print(f"Removing: {remove}")
			toRemove.remove(remove)


	def findWeaknesses(self, chart):
		for i in chart.weaknesses:
			self.weaknesses.append(i)
		for i in chart.resistances:
			self.resistances.append(i)
		for i in chart.immunities:
			self.immunities.append(i)

	def __str__(self):
		return f"{self.name}'s weaknesses are: {self.weaknesses}\n{self.name}'s resistances are: {self.resistances}\n{self.name}'s immunities are: {self.immunities}"


# if __name__ == '__main__':
