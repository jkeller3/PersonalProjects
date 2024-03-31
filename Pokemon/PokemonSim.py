from PokemonClass import Pokemon
from PokemonAttacks import Attack
from PokemonTypes import *
from PokemonBattle import *


if __name__ == '__main__':
	ironHead = Attack('Iron Head', 'Steel', 80, 15)
	playRough = Attack('Play Rough', 'Fairy', 90, 10)
	focusPunch = Attack('Focus Punch', 'Fighting', 150, 5)
	firePunch = Attack('Fire Punch', 'Fire', 75, 15)
	
	mawile = Pokemon(303, 'Mawile', ('Steel', 'Fairy'), 20, 38, 25, 35, 13, [ironHead, playRough, focusPunch, firePunch])

	gigaDrain = Attack('Giga Drain', 'Grass', 60, 10)
	sludgeBomb = Attack('Sludge Bomb', 'Poison', 90, 15)
	hiddenPower = Attack('Hidden Power', 'Fire', 60, 15)
	sleepPowder = Attack('Sleep Powder', 'Grass', 0, 10)
	roserade = Pokemon(407, 'Roserade', ('Grass', 'Poison'), 20, 38, 36, 22, 20, [gigaDrain, sludgeBomb, hiddenPower, sleepPowder])

	dynamicPunch = Attack('Dynamic Punch', 'Fighting', 100, 5)
	stoneEdge = Attack('Stone Edge', 'Rock', 100, 5)
	typesA = ('Steel', 'Dragon')
	dialga = Pokemon(68, 'Dialga', typesA, 20, 46, 50, 32, 12, [stoneEdge, dynamicPunch, None, None])

	fireBlast = Attack('Fire Blast', 'Fire', 120, 5)
	airSlash = Attack('Air Slash', 'Flying', 80, 10)
	solarBeam = Attack('Solarbeam', 'Grass', 120, 5)
	earthquake = Attack('Earthquake', 'Ground', 100, 10)
	charizard = Pokemon (9, 'Charizard', ('Fire', 'Flying'), 20, 42, 38, 20, 24, [fireBlast, airSlash, solarBeam, earthquake])

	print(mawile)


	#print(roserade.weaknesses)

	#for x in roserade.weaknesses:
		#if (x == firePunch.type):
			#print("It's super effective!")

	# Battle.displayInfo(mawile, roserade)

	# Battle.fight(Battle, charizard, machamp)




