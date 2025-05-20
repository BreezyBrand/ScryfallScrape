import pyodbc
import datetime
import json

#debug options
debug = False
sample = True
sample_size = 10000
skip = 0

all_card_options = []

# Define connection parameters
server = r'(localdb)\MSSQLLocalDB' # Replace with your server name
database = 'CardCatalog'  # Replace with your database name
username = ''  # Use your username if required, else you can skip this
password = ''  # Use your password if required, else you can skip this

#Create formatted_card class
class formatted_card:
    def __init__(self,card):        
        self.errors = ""

        try:
            self.id = str(card['id'])
        except:    
            self.errors = self.errors + "Could not set ID. "        
            self.id = ''    
        try:
            self.object = str(card['object'])
        except:
            self.errors = self.errors + "Could not set Object. "
            self.object = ''            
        try:
            self.oracle_id = str(card['oracle_id'])
        except:
            self.errors = self.errors + "Could not set Oracle ID. "
            self.oracle_id = ''
        try:
            self.multiverse_ids = str(card['multiverse_ids'])
        except:
            self.errors = self.errors + "Could not set Multiverse ID. "
            self.multiverse_ids = ''
        try:
            self.mtgo_id = str(card['mtgo_id'])
        except:
            self.errors = self.errors + "Could not set MTGO ID. "
            self.mtgo_id = ''
        try:
            self.mtgo_foil_id = str(card['mtgo_foil_id'])
        except:
            self.errors = self.errors + "Could not set MTGO Foil ID. "
            self.mtgo_foil_id = ''
        try:
            self.tcgplayer_id = str(card['tcgplayer_id'])
        except:
            self.errors = self.errors + "Could not set TCG Player ID. "
            self.tcgplayer_id = ''
        try:
            self.cardmarket_id = str(card['cardmarket_id'])
        except:
            self.errors = self.errors + "Could not set Cardmarket ID. "
            self.cardmarket_id = ''
        try:
            self.name = str(card['name'])
        except:
            self.errors = self.errors + "Could not set Name. "
            self.name = ''
        try:
            self.lang = str(card['lang'])
        except:
            self.lang = ''
        try:
            self.released_at = str(card['released_at'])
        except:
            self.released_at = ''
        try:
            self.uri = str(card['uri'])
        except:
            self.uri = ''
        try:
            self.scryfall_uri = str(card['scryfall_uri'])
        except:
            self.scryfall_uri = ''
        try:
            self.layout = str(card['layout'])
        except:
            self.layout = ''
        try:
            self.highres_image = str(card['highres_image'])
        except:
            self.highres_image = ''
        try:
            self.image_status = str(card['image_status'])
        except:
            self.image_status = ''
        try:
            self.image_uris = str(card['image_uris'])
        except:
            self.image_uris = ''
        try:
            self.mana_cost = str(card['mana_cost'])
        except:
            self.mana_cost = ''
        try:
            self.cmc = str(card['cmc'])
        except:
            self.cmc = ''
        try:
            self.type_line = str(card['type_line'])
        except:
            self.type_line = ''
        try:
            self.oracle_text = str(card['oracle_text'])
        except:
            self.oracle_text = ''
        try:
            self.power = str(card['power'])
        except:
            self.power = ''
        try:
            self.toughness = str(card['toughness'])
        except:
            self.toughness = ''
        try:
            self.colors = str(card['colors'])
        except:
            self.colors = ''
        try:
            self.color_identity = str(card['color_identity'])
        except:
            self.color_identity = ''
        try:
            self.keywords = str(card['keywords'])
        except:
            self.keywords = ''
        try:
            self.legalities = str(card['legalities'])
        except:
            self.legalities = ''
        try:
            self.games = str(card['games'])
        except:
            self.games = ''
        try:
            self.reserved = str(card['reserved'])
        except:
            self.reserved = ''
        try:
            self.foil = str(card['foil'])
        except:
            self.foil = ''
        try:
            self.nonfoil = str(card['nonfoil'])
        except:
            self.nonfoil = ''
        try:
            self.finishes = str(card['finishes'])
        except:
            self.finishes = ''
        try:
            self.oversized = str(card['oversized'])
        except:
            self.oversized = ''
        try:
            self.promo = str(card['promo'])
        except:
            self.promo = ''
        try:
            self.reprint = str(card['reprint'])
        except:
            self.reprint = ''
        try:
            self.variation = str(card['variation'])
        except:
            self.variation = ''
        try:
            self.set_id = str(card['set_id'])
        except:
            self.set_id = ''
        try:
            self.set = str(card['set'])
        except:
            self.set = ''
        try:
            self.set_name = str(card['set_name'])
        except:
            self.set_name = ''
        try:
            self.set_type = str(card['set_type'])
        except:
            self.set_type = ''
        try:
            self.set_uri = str(card['set_uri'])
        except:
            self.set_uri = ''
        try:
            self.set_search_uri = str(card['set_search_uri'])
        except:
            self.set_search_uri = ''
        try:
            self.scryfall_set_uri = str(card['scryfall_set_uri'])
        except:
            self.scryfall_set_uri = ''
        try:
            self.rulings_uri = str(card['rulings_uri'])
        except:
            self.rulings_uri = ''
        try:
            self.prints_search_uri = str(card['prints_search_uri'])
        except:
            self.prints_search_uri = ''
        try:
            self.collector_number = str(card['collector_number'])
        except:
            self.collector_number = ''
        try:
            self.digital = str(card['digital'])
        except:
            self.digital = ''
        try:
            self.rarity = str(card['rarity'])
        except:
            self.rarity = ''
        try:
            self.flavor_text = str(card['flavor_text'])
        except:
            self.flavor_text = ''
        try:
            self.card_back_id = str(card['card_back_id'])
        except:
            self.card_back_id = ''
        try:
            self.artist = str(card['artist'])
        except:
            self.artist = ''
        try:
            self.artist_ids = str(card['artist_ids'])
        except:
            self.artist_ids = ''
        try:
            self.illustration_id = str(card['illustration_id'])
        except:
            self.illustration_id = ''
        try:
            self.border_color = str(card['border_color'])
        except:
            self.border_color = ''
        try:
            self.frame = str(card['frame'])
        except:
            self.frame = ''
        try:
            self.full_art = str(card['full_art'])
        except:
            self.full_art = ''
        try:
            self.textless = str(card['textless'])
        except:
            self.textless = ''
        try:
            self.booster = str(card['booster'])
        except:
            self.booster = ''
        try:
            self.story_spotlight = str(card['story_spotlight'])
        except:
            self.story_spotlight = ''
        try:
            self.edhrec_rank = str(card['edhrec_rank'])
        except:
            self.edhrec_rank = ''
        try:
            self.penny_rank = str(card['penny_rank'])
        except:
            self.penny_rank = ''
        try:
            self.prices = str(card['prices'])
        except:
            self.prices = ''
        try:
            self.related_uris = str(card['related_uris'])
        except:
            self.related_uris = ''
        try:
            self.purchase_uris = str(card['purchase_uris'])
        except:
            self.purchase_uris = ''
        try:
            self.all_parts = str(card['all_parts'])
        except:
            self.all_parts = ''
        try:
            self.promo_types = str(card['promo_types'])
        except:
            self.promo_types = ''
        try:
            self.arena_id = str(card['arena_id'])
        except:
            self.arena_id = ''
        try:
            self.security_stamp = str(card['security_stamp'])
        except:
            self.security_stamp = ''
        try:
            self.card_faces = str(card['card_faces'])
        except:
            self.card_faces = ''
        try:
            self.preview = str(card['preview'])
        except:
            self.preview = ''
        try:
            self.produced_mana = str(card['produced_mana'])
        except:
            self.produced_mana = ''
        try:
            self.watermark = str(card['watermark'])
        except:
            self.watermark = ''
        try:
            self.frame_effects = str(card['frame_effects'])
        except:
            self.frame_effects = ''
        try:
            self.loyalty = str(card['loyalty'])
        except:
            self.loyalty = ''
        try:
            self.printed_name = str(card['printed_name'])
        except:
            self.printed_name = ''        
        try:
            self.game_changer = str(card['game_changer'])
        except:
            self.game_changer = ''        
        try:
            self.printed_type_line = str(card['printed_type_line'])
        except:
            self.printed_type_line = ''                
        try:
            self.printed_text = str(card['printed_text'])
        except:
            self.printed_text = ''        
        try:
            self.color_indicator = str(card['color_indicator'])
        except:
            self.color_indicator = ''        
        try:
            self.tcgplayer_etched_id = str(card['tcgplayer_etched_id'])
        except:
            self.tcgplayer_etched_id = ''        
        try:
            self.content_warning = str(card['content_warning'])
        except:
            self.content_warning = ''        
        try:
            self.flavor_name = str(card['flavor_name'])
        except:
            self.flavor_name = ''        
        try:
            self.attraction_lights = str(card['attraction_lights'])
        except:
            self.attraction_lights = ''        
        try:
            self.variation_of = str(card['variation_of'])
        except:
            self.variation_of = ''        
        try:
            self.life_modifier = str(card['life_modifier'])
        except:
            self.life_modifier = ''        
        try:
            self.hand_modifier = str(card['hand_modifier'])
        except:
            self.hand_modifier = ''        
        try:
            self.defense = str(card['defense'])
        except:
            self.defense = ''

        
class priced_card():
    def __init__(self,args):
        try:
            reformatPrice = str.replace(args,"'",'"')
            reformatPrice = str.replace(reformatPrice,"None",'"None"')            
            cardprices = json.loads(reformatPrice)
            try:
                self.usd =  float(cardprices["usd"])
            except:
                self.usd = -1

            try:
                self.usd_foil = float(cardprices["usd_foil"])
            except:
                self.usd_foil = -1

            try:
                self.usd_etched = float(cardprices["usd_etched"])
            except:
                self.usd_etched = -1

            try:
                self.eur = float(cardprices["eur"])
            except:
                self.eur = -1

            try:
                self.eur_foil = float(cardprices["eur_foil"])
            except:
                self.eur_foil = -1

            try:
                self.eur_etched = float(cardprices["eur_etched"])
            except:
                self.eur_etched = -1

            try:
                self.tix = float(cardprices["tix"])
            except:
                self.tix = -1
        except Exception as e:
            if(debug):
                print(f"Error: {e}")
        pass

# Create the connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};'
count=0

# If authentication is required, add uid and pwd
if username and password:
    connection_string += f'UID={username};PWD={password};'

# Connect to the database
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    if skip == 0:
        clear_price_query = "DELETE FROM PriceHistory WHERE Age='Old'"
        cursor.execute(clear_price_query)
        shift_price_query = "UPDATE PriceHistory SET Age='Old'"
        cursor.execute(shift_price_query)
    print("Connection successful!")    
except Exception as e:
    print(f"Error: {e}")

def processCard(card):    
    try:        
        processed_card = formatted_card(card)        
        if(debug):
            print(processed_card.errors)
        newKeys = card.keys()
        for i in newKeys:
            if i in all_card_options:
                pass
            else:
                all_card_options.append(i)
    except Exception as e:
        print(f"Error: {e}")                
    
    return processed_card

def getPricing(prices):
    try:
        query_card = priced_card(prices)
        return query_card
    except:
        print("Could not get card prices")
    
def postUpdate():
    refreshQuery = "INSERT INTO UpdateLog(Update_Date,Update_Table) VALUES (GETDATE(),'Cards')"
    cursor.execute(refreshQuery)
    conn.commit()
    refreshQuery = "INSERT INTO UpdateLog(Update_Date,Update_Table) VALUES (GETDATE(),'Pricing')"
    cursor.execute(refreshQuery)
    conn.commit()
    print("Card roster update logged...")


def saveCardAttempt(card):
    try:
        #Check if the record exists
        #query_check = "SELECT COUNT(*) FROM Cards WHERE id = ?;"
        #cursor.execute(query_check, (card.id))
        #exists = cursor.fetchone()[0]
        exists = False

        data = (card.object,card.oracle_id,card.multiverse_ids,card.mtgo_id,card.mtgo_foil_id,card.tcgplayer_id,card.cardmarket_id,card.name,card.lang,card.released_at,card.uri,card.scryfall_uri,card.layout,card.highres_image,card.image_status,card.image_uris,card.mana_cost,card.cmc,card.type_line,card.oracle_text,card.power,card.toughness,card.colors,card.color_identity,card.keywords,card.legalities,card.games,card.reserved,card.foil,card.nonfoil,card.finishes,card.oversized,card.promo,card.reprint,card.variation,card.set_id,card.set,card.set_name,card.set_type,card.set_uri,card.set_search_uri,card.scryfall_set_uri,card.rulings_uri,card.prints_search_uri,card.collector_number,card.digital,card.rarity,card.flavor_text,card.card_back_id,card.artist,card.artist_ids,card.illustration_id,card.border_color,card.frame,card.full_art,card.textless,card.booster,card.story_spotlight,card.edhrec_rank,card.penny_rank,card.prices,card.related_uris,card.purchase_uris,card.all_parts,card.promo_types,card.arena_id,card.security_stamp,card.card_faces,card.preview,card.produced_mana,card.watermark,card.frame_effects,card.loyalty,card.printed_name,card.game_changer,
                card.printed_type_line,card.printed_text,card.color_indicator,card.tcgplayer_etched_id,card.content_warning,card.flavor_name,card.attraction_lights,card.variation_of,card.life_modifier,card.hand_modifier,card.defense,card.id)

        if exists:
            if(debug):
                print("Record exists. Updating...")            
            method = "updated"
            #Set Update Query
            update_query = """
            UPDATE Cards SET                
                [object]=?,
                [oracle_id]=?,
                [multiverse_ids]=?,
                [mtgo_id]=?,
                [mtgo_foil_id]=?,
                [tcgplayer_id]=?,
                [cardmarket_id]=?,
                [name]=?,
                [lang]=?,
                [released_at]=?,
                [uri]=?,
                [scryfall_uri]=?,
                [layout]=?,
                [highres_image]=?,
                [image_status]=?,
                [image_uris]=?,
                [mana_cost]=?,
                [cmc]=?,
                [type_line]=?,
                [oracle_text]=?,
                [power]=?,
                [toughness]=?,
                [colors]=?,
                [color_identity]=?,
                [keywords]=?,
                [legalities]=?,
                [games]=?,
                [reserved]=?,
                [foil]=?,
                [nonfoil]=?,
                [finishes]=?,
                [oversized]=?,
                [promo]=?,
                [reprint]=?,
                [variation]=?,
                [set_id]=?,
                [set]=?,
                [set_name]=?,
                [set_type]=?,
                [set_uri]=?,
                [set_search_uri]=?,
                [scryfall_set_uri]=?,
                [rulings_uri]=?,
                [prints_search_uri]=?,
                [collector_number]=?,
                [digital]=?,
                [rarity]=?,
                [flavor_text]=?,
                [card_back_id]=?,
                [artist]=?,
                [artist_ids]=?,
                [illustration_id]=?,
                [border_color]=?,
                [frame]=?,
                [full_art]=?,
                [textless]=?,
                [booster]=?,
                [story_spotlight]=?,
                [edhrec_rank]=?,
                [penny_rank]=?,
                [prices]=?,
                [related_uris]=?,
                [purchase_uris]=?,
                [all_parts]=?,
                [promo_types]=?,
                [arena_id]=?,
                [security_stamp]=?,
                [card_faces]=?,
                [preview]=?,
                [produced_mana]=?,
                [watermark]=?,
                [frame_effects]=?,
                [loyalty]=?,
                [printed_name]=?,
                [game_changer]=?,
                [printed_type_line]=?,
                [printed_text]=?,
                [color_indicator]=?,
                [tcgplayer_etched_id]=?,
                [content_warning]=?,
                [flavor_name]=?,
                [attraction_lights]=?,
                [variation_of]=?,
                [life_modifier]=?,
                [hand_modifier]=?,
                [defense]=?
            WHERE [id]=?
            """
            cursor.execute(update_query, data)
        else:
            if(debug):
                print("No record exists. Creating...")            
            method = "inserted"
            #Set Insert Query
            insert_query = """
            INSERT INTO Cards ([object],[oracle_id],[multiverse_ids],[mtgo_id],[mtgo_foil_id],[tcgplayer_id],[cardmarket_id],[name],[lang],[released_at],[uri],[scryfall_uri],[layout],[highres_image],[image_status],[image_uris],[mana_cost],[cmc],[type_line],[oracle_text],[power],[toughness],[colors],[color_identity],[keywords],[legalities],[games],[reserved],[foil],[nonfoil],[finishes],[oversized],[promo],[reprint],[variation],[set_id],[set],[set_name],[set_type],[set_uri],[set_search_uri],[scryfall_set_uri],[rulings_uri],[prints_search_uri],[collector_number],[digital],[rarity],[flavor_text],[card_back_id],[artist],[artist_ids],[illustration_id],[border_color],[frame],[full_art],[textless],[booster],[story_spotlight],[edhrec_rank],[penny_rank],[prices],[related_uris],[purchase_uris],[all_parts],[promo_types],[arena_id],[security_stamp],[card_faces],[preview],[produced_mana],[watermark],[frame_effects],[loyalty],[printed_name],[game_changer],[printed_type_line],[printed_text],[color_indicator],[tcgplayer_etched_id],[content_warning],[flavor_name],[attraction_lights],[variation_of],[life_modifier],[hand_modifier],[defense],[id]) 
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
            """
            # Execute the insert query
            cursor.execute(insert_query, data)
        
        cardp = getPricing(card.prices)                
        pricingQuery = """INSERT INTO PriceHistory ([CardId],[Age],[usd],[usd_foil],[usd_etched],[eur],[eur_foil],[eur_etched],[tix],[Update_Date]) VALUES (?,?,?,?,?,?,?,?,?,GETDATE())"""        
        pricingData = (card.id,'New',cardp.usd,cardp.usd_foil,cardp.usd_etched,cardp.eur,cardp.eur_foil,cardp.eur_etched,cardp.tix)
        cursor.execute(pricingQuery, pricingData)

        # Commit the changes
        conn.commit()
        if(debug):
            print("Data "+method+" successfully!")            

    except Exception as e:
        print(f"Ln 530 Error: {e}")
        
with open('cards.txt','r',encoding="utf8") as file2:    
    for line in file2:        
        if(count%100 == 0):
            print(count)
        try:
            if(line != "[" and line != "]" and count > skip):
                all_but_one = str(line[:-2])
                card = json.loads(all_but_one)
                processed_card = processCard(card)                
                saveCardAttempt(processed_card)
        except Exception as e:            
            print(f"An error ({e}) occured parsing line {str(count)}")            
        count = count + 1
        if(sample and count>sample_size):            
            #postUpdate()
            #print(all_card_options)
            cursor.close()
            conn.close()
            quit()
    postUpdate()
    cursor.close()
    conn.close()
    quit()
