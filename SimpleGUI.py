import flet as ft
import json

all_json_options = []

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

    def __getattribute__(self, name):
        pass

class jsonBlock:            
    def __init__(self,json):
        for key, value in json.items():
            setattr(self, key, value)
        
    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def Count(self):
        return len(self.__dict__)

class JsonVizApp(ft.Column):
    def __init__(self):
        super().__init__()                
        self.controls = [
            ft.Column([
                ft.Row([
                    ft.Text("")
                ])
            ])
        ]
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.height= 200
        self.width=400
    def QueryJson(self,searchArray):
        pass

    def findCard(self, set: str, cn: str):
        print("Searching...")
        self.controls = []
        self.update()
        with open('cards.txt','r',encoding="utf8") as file2:    
            count = 0
            for line in file2:        
                if(count%10000 == 0):
                    #print(count)
                    pass
                try:
                    all_but_one = str(line[:-2])
                    card = json.loads(all_but_one)
                    jblock = jsonBlock(card)                    
                    # processed_card = processCard(card)
                    if(jblock["set"] == set):
                        if(cn == ""):                        
                            print("Found match: " + jblock["name"])
                            for prop in jblock.__dict__.keys():
                                    text_head = ft.Text(prop+":")
                                    text_val = ft.Text(jblock[prop])

                                    prop_row = ft.Row([
                                        text_head,
                                        text_val
                                    ])
                                    self.controls.append(prop_row)
                        elif(hasattr(jblock,"collector_number")):
                            if(cn == jblock["collector_number"]):
                                print("Found match: " + jblock["name"])
                                for prop in jblock.__dict__.keys():
                                    text_head = ft.Text(prop)
                                    text_val = ft.Text(jblock[prop])

                                    prop_row = ft.Row([
                                        text_head,
                                        text_val
                                    ])
                                    self.controls.append(prop_row)                                                            
                            else:
                                pass
                        
                except Exception as e:            
                    print(f"An error ({e}) occured parsing line {str(count)}")            
                count = count + 1
        self.update()                     
        return                            

class JsonVizParser(ft.Column):              
    def __init__(self,jviz: JsonVizApp):
        super().__init__()
        self.scroll = ft.ScrollMode.ADAPTIVE
        self.height= 800
        self.width=500          
        self.FileLookup = ft.TextField(value = "cards.txt", text_align=ft.TextAlign.RIGHT,width=300)                     
        self.QueryButton = ft.IconButton(
                    icon=ft.Icons.CHECK_CIRCLE,
                    icon_color=ft.Colors.GREEN_300,
                    icon_size=25,
                    tooltip="Query JSON file",
                    #on_click=lambda e: jviz.findCard(jviz.set_number.value,jviz.txt_number.value),
                    on_click= lambda e: self.buildSearchQuery(jviz),
                    alignment=ft.alignment.center,                    
                )   

        self.controls = [
            ft.Column([
                ft.Row([
                    ft.Text("Please provide the link to the text/json file"),
                ]),
                ft.Row([
                    self.FileLookup,
                    ft.IconButton(
                        icon=ft.Icons.CHECK_CIRCLE,
                        icon_color=ft.Colors.GREEN_300,
                        icon_size=25,
                        tooltip="Load JSON Keys",
                        on_click= lambda e: self.getSearchKeys(self.FileLookup.value),
                        alignment=ft.alignment.center,                
                    )
                ])
            ])
        ]
    
    def buildSearchQuery(self, jviz):
        searchQ = jsonBlock({})        
        
        for col in all_json_options:
            colVal = ft.TextField(ref=col).value
            searchQ.__setattr__(col,colVal)
            
        jviz.QueryJson(searchQ)

    def getSearchKeys(self,fileValue):
        try:                        
            block = populate_all_options(fileValue)            
            if(block.Count() > 0):
                self.controls = []
                newCol = ft.Column(
                    controls=[]
                )
                for attr in block.__dict__:
                    try:                        
                        varthis = block[attr]
                        colRow = ft.Row(visible=False)
                        colLabel = ft.Text(f"{varthis}",width=175)
                        colRow.controls.append(colLabel)
                        colfeild = ft.TextField(text_align=ft.TextAlign.RIGHT, width=225)
                        colRow.controls.append(colfeild)
                        colCheck = ft.Checkbox(label=f"Include {varthis} on display?", on_change= lambda e: self.toggleRow(colRow))
                        #colRow.controls.append(colCheck)
                        newCol.controls.append(colRow)                        
                        newCol.controls.append(colCheck)                        
                    except Exception as e:
                        print(f"Error in JsonVizParser.getSearchKeys for {block[attr]}: {e}")
                self.controls.append(newCol)
            self.update()
        except Exception as e:
            print(f"Error in JsonVizParser.getSearchKeys: {e}")
            pass

    def toggleRow(self,row):              
        try:
            if(row.visible):
                print("Changing row visibility to false")
                row.visible = False
            else:
                print("Changing row visibility to true")
                row.visible = True        
            row.update()
            self.page.update()
            self.update()        
        except Exception as e:
            print(f"Cannot toggle row: {e}")
        


def populate_all_options(fileValue:str):
    thisCount = 0
    newBlock = jsonBlock({})
    print(f"Processing file '{fileValue}'")
    with open(fileValue,'r',encoding="utf8") as file:                
        for line in file:            
            try:
                if(thisCount%25000 == 0):
                    print(str(int((thisCount/107301)*1000)/10) + "% Complete")
                all_but_one = str(line[:-2])
                jObj = json.loads(all_but_one)
                newKeys = jObj.keys()        
                for i in newKeys:
                    if hasattr(newBlock,i):
                        pass
                    else:
                        newBlock.__setattr__(i,i)
                thisCount = thisCount+1
            except Exception as e:
                print(e)
        print("100% Complete")
    return newBlock

def processCard(card):    
    try:        
        processed_card = formatted_card(card)
        newKeys = card.keys()        
        for i in newKeys:
            if i in all_json_options:
                pass
            else:
                all_json_options.append(i)
        return processed_card
    except Exception as e:
        print(f"Error: {e}")

                 
def main(page: ft.Page):
    page.title = "JSON Visualizer"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    
    jviz = JsonVizApp()
    jParser = JsonVizParser(jviz)
    #Create Inputs
    set_number = ft.TextField(value="rex",text_align=ft.TextAlign.RIGHT, width=100)
    txt_number = ft.TextField(value="1", text_align=ft.TextAlign.RIGHT, width=100)        

    #Create Buttons
    # searchbutton = ft.IconButton(
    #                 icon=ft.Icons.CHECK_CIRCLE,
    #                 icon_color=ft.Colors.GREEN_300,
    #                 icon_size=25,
    #                 tooltip="Yep",
    #                 on_click= jviz.findCard(set_number.value,txt_number.value),
    #                 alignment=ft.alignment.center
    #             )     

    # create application instance
    # page.add(ft.Row([ft.Column(
    #                     [                   
    #                         ft.Row([ft.Text("Set",width=100),set_number]),                
    #                         ft.Row([ft.Text("Collector Number",width=100),txt_number]),
    #                         ft.Row([ft.Text("Search",width=100),searchbutton]),
    #                         # ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),                                
    #                         # ft.IconButton(ft.Icons.ADD, on_click=plus_click),                
    #                     ],
    #                     alignment=ft.MainAxisAlignment.CENTER,
    #                     width=400
    #                 ),
    #                 jviz
    #                 ],alignment=ft.MainAxisAlignment.CENTER
    #                 ))    
    # add application's root control to the page
    page.add(jParser)
    page.add(jviz)
    page.update()

ft.app(main)