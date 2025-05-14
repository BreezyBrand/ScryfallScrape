USE [CardCatalog]
GO

/****** Object:  Table [dbo].[Inventory]    Script Date: 5/14/2025 12:17:22 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

DELETE FROM Inventory

--SAMPLE DATA, REMOVE/REPLACE WITH YOUR INVENTORY
INSERT INTO
	Inventory ([Set],[Collector Number],[Quantity],[Proxied])
VALUES
	('REX','8',1,'N'),
	('REX','16',1,'N'),
	('DRC','58',1,'N'),
	('M3C','121',1,'N'),
	('LCC','232',1,'N'),
	('PCY','83',1,'N'),
	('MH3','217',1,'N'),
	('GTC','240',1,'N'),
	('FDN','215',1,'N'),
	('INR','55',1,'N'),
	('RIX','123',1,'N'),
	('CLU','160',1,'N'),
	('WHO','265',1,'N'),
	('DSC','244',1,'N'),
	('REX','2',1,'N'),
	('KHM','128',1,'N'),
	('STX','177',1,'N'),
	('REX','20',1,'N'),
	('M3C','338',1,'N'),
	('LCI','183',1,'N'),
	('TSR','202',1,'N'),
	('FDN','154',1,'N'),
	('BLC','119',1,'N'),
	('RAV','51',1,'N'),
	('CMM','96',1,'N'),
	('RIX','104',1,'N'),
	('BLC','219',1,'N'),
	('FDN','225',1,'N'),
	('REX','4',1,'N'),
	('CLB','78',1,'N'),
	('IKO','250',1,'N'),
	('ZNR','192',1,'N'),
	('C16','155',1,'N'),
	('LTR','418',1,'N'),
	('REX','5',1,'N'),
	('LCC','246',1,'N'),
	('M19','61',1,'N'),
	('VOW','68',1,'N'),
	('IKO','58',1,'N'),
	('RIX','107',1,'N'),
	('RIX','141',1,'N'),
	('RIX','144',1,'N'),
	('OTP','32',1,'N'),
	('MH1','244',1,'N'),
	('2XM','212',1,'N'),
	('WHO','52',1,'N'),
	('GRN','51',1,'N'),
	('8ED','274',1,'N'),
	('LCC','249',1,'N'),
	('XLN','155',1,'N'),
	('XLN','202',1,'N'),
	('RIX','110',1,'N'),
	('LTC','325',1,'N'),
	('LCC','253',1,'N'),
	('M3C','411',1,'N'),
	('INR','282',1,'N'),
	('ONE','182',1,'N'),
	('REX','6',1,'N'),
	('LCC','257',1,'N'),
	('MM3','244',1,'N'),
	('BLB','192',1,'N'),
	('BLB','68',1,'N'),
	('RIX','115',1,'N'),
	('NEM','117',1,'N'),
	('XLN','208',1,'N'),
	('CMD','261',1,'N'),
	('ZNR','166',1,'N'),
	('CLB','361',1,'N'),
	('CMM','259',1,'N'),
	('GRN','257',1,'N'),
	('GTC','247',1,'N'),
	('INR','285',1,'N'),
	('MH3','259',1,'N'),
	('XLN','164',1,'N'),
	('C20','162',1,'N'),
	('C13','60',1,'N'),
	('CMR','358',1,'N'),
	('ACR','043',1,'N'),
	('REX','7',1,'N'),
	('BLB','162',1,'N'),
	('MH3','236',1,'N'),
	('CHK','199',1,'N')


INSERT INTO Decks ([Name],[Description]) VALUES ('Life finds a way...','Dino Deck Clone')

INSERT INTO 
	DeckCards ([DeckId],[Set],[Collector_number])
SELECT
	1,
	inv.[Set],
	inv.[Collector Number]
FROM
	Inventory inv

--SAMPLE DATA, REMOVE/REPLACE WITH YOUR INVENTORY

--SELECT 
--	c.[name],
--	inv.[set],
--	c.[set],
--	inv.[Collector Number],
--	c.[collector_number]
--FROM
--	Inventory inv
--	LEFT JOIN Cards c ON  CONCAT(inv.[Set],inv.[Collector Number]) = CONCAT(c.[Set],c.[Collector_number])
	