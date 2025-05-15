CREATE DATABASE CardCatalog;
GO

USE [CardCatalog]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Cards](
	[id] [varchar](250) NOT NULL,
	[object] [varchar](max) NULL,
	[oracle_id] [varchar](max) NULL,
	[multiverse_ids] [varchar](max) NULL,
	[mtgo_id] [varchar](max) NULL,
	[mtgo_foil_id] [varchar](max) NULL,
	[tcgplayer_id] [varchar](max) NULL,
	[cardmarket_id] [varchar](max) NULL,
	[name] [varchar](max) NULL,
	[lang] [varchar](max) NULL,
	[released_at] [varchar](max) NULL,
	[uri] [varchar](max) NULL,
	[scryfall_uri] [varchar](max) NULL,
	[layout] [varchar](max) NULL,
	[highres_image] [varchar](max) NULL,
	[image_status] [varchar](max) NULL,
	[image_uris] [varchar](max) NULL,
	[mana_cost] [varchar](max) NULL,
	[cmc] [varchar](max) NULL,
	[type_line] [varchar](max) NULL,
	[oracle_text] [varchar](max) NULL,
	[power] [varchar](max) NULL,
	[toughness] [varchar](max) NULL,
	[colors] [varchar](max) NULL,
	[color_identity] [varchar](max) NULL,
	[keywords] [varchar](max) NULL,
	[legalities] [varchar](max) NULL,
	[games] [varchar](max) NULL,
	[reserved] [varchar](max) NULL,
	[foil] [varchar](max) NULL,
	[nonfoil] [varchar](max) NULL,
	[finishes] [varchar](max) NULL,
	[oversized] [varchar](max) NULL,
	[promo] [varchar](max) NULL,
	[reprint] [varchar](max) NULL,
	[variation] [varchar](max) NULL,
	[set_id] [varchar](max) NULL,
	[set] [varchar](max) NULL,
	[set_name] [varchar](max) NULL,
	[set_type] [varchar](max) NULL,
	[set_uri] [varchar](max) NULL,
	[set_search_uri] [varchar](max) NULL,
	[scryfall_set_uri] [varchar](max) NULL,
	[rulings_uri] [varchar](max) NULL,
	[prints_search_uri] [varchar](max) NULL,
	[collector_number] [varchar](max) NULL,
	[digital] [varchar](max) NULL,
	[rarity] [varchar](max) NULL,
	[flavor_text] [varchar](max) NULL,
	[card_back_id] [varchar](max) NULL,
	[artist] [varchar](max) NULL,
	[artist_ids] [varchar](max) NULL,
	[illustration_id] [varchar](max) NULL,
	[border_color] [varchar](max) NULL,
	[frame] [varchar](max) NULL,
	[full_art] [varchar](max) NULL,
	[textless] [varchar](max) NULL,
	[booster] [varchar](max) NULL,
	[story_spotlight] [varchar](max) NULL,
	[edhrec_rank] [varchar](max) NULL,
	[penny_rank] [varchar](max) NULL,
	[prices] [varchar](max) NULL,
	[related_uris] [varchar](max) NULL,
	[purchase_uris] [varchar](max) NULL,
	[all_parts] [varchar](max) NULL,
	[promo_types] [varchar](max) NULL,
	[arena_id] [varchar](max) NULL,
	[security_stamp] [varchar](max) NULL,
	[card_faces] [varchar](max) NULL,
	[preview] [varchar](max) NULL,
	[produced_mana] [varchar](max) NULL,
	[watermark] [varchar](max) NULL,
	[frame_effects] [varchar](max) NULL,
	[loyalty] [varchar](max) NULL,
	[printed_name] [varchar](max) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[UpdateLog](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Update_Date] [datetime2](7) NULL,
	[Update_Table] [nvarchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
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
	[Update_Date] [datetime2](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[CardId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Inventory](
	[Set] [varchar](50) NOT NULL,
	[Collector Number] [varchar](50) NOT NULL,
	[Quantity] [int] NULL,
	[foiled] [char](1) NULL,
	[Proxied] [char](1) NULL,
	[Update_Date] [datetime2](7) NULL,
 CONSTRAINT [PK_Inventory] PRIMARY KEY CLUSTERED 
(
	[Set] ASC,
	[Collector Number] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[Decks](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[Name] [nvarchar](200) NOT NULL,
	[Description] [nvarchar](200) NULL,
	[Colors] [varchar](5) NULL,
	[Update_Date] [datetime2](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

CREATE TABLE [dbo].[DeckCards](
	[DeckId] [int] NOT NULL,
	[Set] [varchar](max) NOT NULL,
	[Collector_number] [varchar](max) NOT NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

CREATE TABLE [dbo].[PriceHistory](
	[CardId] [varchar](250) NOT NULL,
	[Age] [varchar](3) NOT NULL,
	[usd] [decimal](18, 2) NULL,
	[usd_foil] [decimal](18, 2) NULL,
	[usd_etched] [decimal](18, 2) NULL,
	[eur] [decimal](18, 2) NULL,
	[eur_foil] [decimal](18, 2) NULL,
	[eur_etched] [decimal](18, 2) NULL,
	[tix] [decimal](18, 2) NULL,
	[Update_Date] [datetime2](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[Age] ASC,
	[CardId] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO



CREATE USER [cardLoader] FOR LOGIN [cardLoader] WITH DEFAULT_SCHEMA=[dbo]
GO



