USE [CardCatalog]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DELETE FROM Legalities

INSERT INTO Legalities ([CardId],[standard],[future],[historic],[timeless],[gladiator],[pioneer],[explorer],[modern],[legacy],[pauper],[vintage],[penny],[commander],[oathbreaker],[standardbrawl],[brawl],[alchemy],[paupercommander],[duel],[oldschool],[premodern],[predh])
SELECT
	[CardId] = id,
	[standard] = 'Not Legal',
	[future]  = 'Not Legal',
	[historic]  = 'Not Legal',
	[timeless]  = 'Not Legal',
	[gladiator] = 'Not Legal',
	[pioneer] = 'Not Legal',
	[explorer] = 'Not Legal',
	[modern] = 'Not Legal',
	[legacy] = 'Not Legal',
	[pauper] = 'Not Legal',
	[vintage] = 'Not Legal',
	[penny] = 'Not Legal',
	[commander] = 'Not Legal',
	[oathbreaker] = 'Not Legal',
	[standardbrawl] = 'Not Legal',
	[brawl] = 'Not Legal',
	[alchemy] = 'Not Legal',
	[paupercommander] = 'Not Legal',
	[duel]  = 'Not Legal',
	[oldschool]  = 'Not Legal',
	[premodern]  = 'Not Legal',
	[predh] = 'Not Legal'
FROM 
	Cards

UPDATE
	Legalities
SET
	[standard] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''standard'': ''legal''%'
	
	
UPDATE
	Legalities
SET
	[future] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''future'': ''not_legal''%'
	
UPDATE
	Legalities
SET
	[historic] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''historic'': ''not_legal''%'

UPDATE
	Legalities
SET
	[timeless] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''timeless'': ''not_legal''%'

UPDATE
	Legalities
SET
	[gladiator] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''gladiator'': ''not_legal''%'

UPDATE
	Legalities
SET
	[pioneer] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''pioneer'': ''not_legal''%'

UPDATE
	Legalities
SET
	[explorer] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''explorer'': ''not_legal''%'

UPDATE
	Legalities
SET
	[modern] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''modern'': ''legal''%'

UPDATE
	Legalities
SET
	[legacy] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''legacy'': ''legal''%'

UPDATE
	Legalities
SET
	[pauper] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''pauper'': ''not_legal''%'

UPDATE
	Legalities
SET
	[vintage] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''vintage'': ''legal''%'

UPDATE
	Legalities
SET
	[penny] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''penny'': ''not_legal''%'

UPDATE
	Legalities
SET
	[commander] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''commander'': ''legal''%'

UPDATE
	Legalities
SET
	[oathbreaker] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''oathbreaker'': ''legal''%'

UPDATE
	Legalities
SET
	[standardbrawl] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''standardbrawl'': ''not_legal''%'

UPDATE
	Legalities
SET
	[brawl] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''brawl'': ''not_legal''%'

UPDATE
	Legalities
SET
	[alchemy] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''alchemy'': ''not_legal''%'

UPDATE
	Legalities
SET
	[paupercommander] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''paupercommander'': ''restricted''%'

UPDATE
	Legalities
SET
	[duel] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''duel'': ''legal''%'

UPDATE
	Legalities
SET
	[oldschool] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''oldschool'': ''not_legal''%'

UPDATE
	Legalities
SET
	[premodern] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''premodern'': ''not_legal''%'

UPDATE
	Legalities
SET
	[predh] = 'legal'
FROM
	Cards c 
	LEFT JOIN legalities l ON c.id = l.CardId
WHERE
	c.legalities LIKE '%''predh'': ''legal''%'

	