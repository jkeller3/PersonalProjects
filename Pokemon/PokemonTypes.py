# Pokemon types

# from PokemonBattle import damageCalcs
# from PokemonClass import Pokemon
# from PokemonAttacks import Attack

class Type:
	def __init__(self):
		self.weaknesses = []
		self.resistances = []
		self.immunities = []
	def __str__(self):
		return 'Weaknesses: {}, Resistances: {}, Immunities: {}'.format(self.weaknesses, self.resistances, self.immunities)
	def __repr__(self):
		return 'Weaknesses: {}, Resistances: {}, Immunities: {}'.format(self.weaknesses, self.resistances, self.immunities)

class Normal(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fighting']
		self.immunities = ['Ghost']


class Fire(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Water', 'Ground', 'Rock']
		self.resistances = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']

class Water(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Grass', 'Electric']
		self.resistances = ['Fire', 'Water', 'Ice', 'Steel']

class Grass(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fire', 'Flying', 'Poison', 'Ice', 'Bug']
		self.resistances = ['Ground', 'Water', 'Electric', 'Grass']


class Electric(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Ground']
		self.resistances = ['Flying', 'Steel', 'Electric']

class Ice(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fire', 'Fighting', 'Rock', 'Steel']
		self.resistances = ['Ice']

class Fighting(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Flying', 'Fairy', 'Psychic']
		self.resistances = ['Dark', 'Rock', 'Bug']

class Poison(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Psychic', 'Ground']
		self.resistances = ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']

class Ground(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Water', 'Grass', 'Ice']
		self.resistances = ['Rock']
		self.immunities = ['Electric']

class Flying(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Electric', 'Ice', 'Rock']
		self.resistances = ['Grass', 'Fighting', 'Bug']
		self.immunities = ['Ground']

class Psychic(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Bug', 'Ghost', 'Dark']
		self.resistances = ['Fighting', 'Psychic']

class Bug(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fire', 'Flying', 'Rock']
		self.resistances = ['Grass', 'Fighting', 'Ground']

class Rock(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Ground', 'Fighting', 'Grass', 'Water', 'Steel']
		self.resistances = ['Flying', 'Fire', 'Normal', 'Poison']

class Ghost(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Ghost', 'Dark']
		self.resistances = ['Poison', 'Bug']
		self.immunities = ['Normal', 'Fighting']

class Dragon(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Dragon', 'Fairy', 'Ice']
		self.resistances = ['Fire', 'Water', 'Grass', 'Electric']

class Dark(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fighting', 'Bug', 'Fairy']
		self.resistances = ['Ghost', 'Dark']
		self.immunities = ['Psychic']

class Steel(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Fire', 'Fighting', 'Ground']
		self.resistances = ['Grass', 'Flying', 'Normal', 'Ice', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
		self.immunities = ['Poison']

class Fairy(Type):
	def __init__(self):
		Type.__init__(self)
		self.weaknesses = ['Poison', 'Steel']
		self.resistances = ['Dark', 'Fighting', 'Bug']
		self.immunities = ['Dragon']

# if __name__ == '__main__':

		