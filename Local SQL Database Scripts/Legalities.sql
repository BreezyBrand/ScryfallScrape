USE [CardCatalog]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Legalities](
	[CardId] [varchar](250) NOT NULL,
	[standard] [varchar](50) NOT NULL,
	[future] [varchar](50) NOT NULL,
	[historic] [varchar](50) NOT NULL,
	[timeless] [varchar](50) NOT NULL,
	[gladiator] [varchar](50) NOT NULL,
	[pioneer] [varchar](50) NOT NULL,
	[explorer] [varchar](50) NOT NULL,
	[modern] [varchar](50) NOT NULL,
	[legacy] [varchar](50) NOT NULL,
	[pauper] [varchar](50) NOT NULL,
	[vintage] [varchar](50) NOT NULL,
	[penny] [varchar](50) NOT NULL,
	[commander] [varchar](50) NOT NULL,
	[oathbreaker] [varchar](50) NOT NULL,
	[standardbrawl] [varchar](50) NOT NULL,
	[brawl] [varchar](50) NOT NULL,
	[alchemy] [varchar](50) NOT NULL,
	[paupercommander] [varchar](50) NOT NULL,
	[duel] [varchar](50) NOT NULL,
	[oldschool] [varchar](50) NOT NULL,
	[premodern] [varchar](50) NOT NULL,
	[predh] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[CardId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
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

	