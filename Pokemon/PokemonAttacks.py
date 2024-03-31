# Pokemon Attacks

class Attack:
	def __init__(self, name, type, power, pp):
		self.name = name
		self.type = type
		self.power = power
		self.pp = pp

	def __str__(self):
		return  '{}'.format(self.name)

	def __repr__(self):
		return 'Attack: {}, Type: {}, Power: {}, PP: {}\n'.format(self.name, self.type, self.power, self.pp)