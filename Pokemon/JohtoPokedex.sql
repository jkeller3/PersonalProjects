SELECT *
FROM Pokedex
WHERE National_Dex NOT LIKE '%.%'
	AND National_Dex >= 152 
	AND National_Dex < 252

CREATE TABLE #JohtoPokedex(
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

INSERT INTO #JohtoPokedex
SELECT *
FROM Pokedex
WHERE National_Dex NOT LIKE '%.%'
	AND National_Dex >= 152
	AND National_Dex < 252

SELECT *
FROM #JohtoPokedex

SELECT id, Name, HP, Attack, Defense, Type1, Type2
FROM #JohtoPokedex
WHERE Type1 = 'Grass'
	OR Type2 = 'Grass'