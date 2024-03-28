SELECT*
FROM Pokedex
WHERE National_Dex NOT LIKE '%.%'
	AND National_Dex >= 252
	AND National_Dex < 386

SELECT Pokemon_Name AS Pokemon, HP, Attack, Defense, Special_Attack, Special_Defense, Speed, Total, Type_I, Type_II
FROM Pokedex
WHERE Attack >= 150 AND Speed > 100
ORDER BY Attack DESC

CREATE TABLE #KantoPokedex(
id int,
Name varchar(50),
HP int,
Attack int,
Defense int,
SpAttack int,
SpDefense int,
Speed int,
Total int,
Type1 varchar(50),
Type2 varchar(50)
)

INSERT INTO #KantoPokedex
SELECT *
FROM Pokedex
WHERE National_Dex NOT LIKE '%.%'
	AND National_Dex < 152

SELECT *
FROM #KantoPokedex

SELECT id, Name, Type1, Type2
FROM #KantoPokedex
WHERE Type1 = 'Grass'
	OR Type2 = 'Grass'

SELECT id, Name, Type1, Type2
FROM #KantoPokedex
WHERE Type1 = 'Fire'
	OR Type2 = 'Fire'