import json
import xlsxwriter

workbook = xlsxwriter.Workbook("Cards.xlsx")
worksheet = workbook.add_worksheet()

count=0
row=1

def tryWrite(col,val):
    if val.startswith("https://"):
        formattedVal = val[8:]
    elif val.startswith("http://"):
        formattedVal = val[7:]
    else:
        worksheet.write(row,col,str(val))
        formattedVal = val

    try:        
        worksheet.write(row,col,str(formattedVal))
    except:
        print("Could not write value")

def saveCardAttempt(card):
    try:
        keys = card.keys()        
        for i in keys:
            try:            
                keyCol = getKeyCol(i)
                tryWrite(keyCol,card[i])    
            except:
                tryWrite(0,"")
    except:
        print("Could not parse card data")

def getKeyCol(keyId):
    if keyId=="object": 
        return 0
    if keyId=="id": 
        return 1
    if keyId=="oracle_id": 
        return 2
    if keyId=="multiverse_ids": 
        return 3
    if keyId=="mtgo_id": 
        return 4
    if keyId=="mtgo_foil_id": 
        return 5
    if keyId=="tcgplayer_id": 
        return 6
    if keyId=="cardmarket_id": 
        return 7
    if keyId=="name": 
        return 8
    if keyId=="lang": 
        return 9
    if keyId=="released_at": 
        return 10
    if keyId=="uri": 
        return 11
    if keyId=="scryfall_uri": 
        return 12
    if keyId=="layout": 
        return 13
    if keyId=="highres_image": 
        return 14
    if keyId=="image_status": 
        return 15
    if keyId=="image_uris": 
        return 16
    if keyId=="mana_cost": 
        return 17
    if keyId=="cmc": 
        return 18
    if keyId=="type_line": 
        return 19
    if keyId=="oracle_text": 
        return 20
    if keyId=="power": 
        return 21
    if keyId=="toughness": 
        return 22
    if keyId=="colors": 
        return 23
    if keyId=="color_identity": 
        return 24
    if keyId=="keywords": 
        return 25
    if keyId=="legalities": 
        return 26
    if keyId=="games": 
        return 27
    if keyId=="reserved": 
        return 28
    if keyId=="foil": 
        return 29
    if keyId=="nonfoil": 
        return 30
    if keyId=="finishes": 
        return 31
    if keyId=="oversized": 
        return 32
    if keyId=="promo": 
        return 33
    if keyId=="reprint": 
        return 34
    if keyId=="variation": 
        return 35
    if keyId=="set_id": 
        return 36
    if keyId=="set": 
        return 37
    if keyId=="set_name": 
        return 38
    if keyId=="set_type": 
        return 39
    if keyId=="set_uri": 
        return 40
    if keyId=="set_search_uri": 
        return 41
    if keyId=="scryfall_set_uri": 
        return 42
    if keyId=="rulings_uri": 
        return 43
    if keyId=="prints_search_uri": 
        return 44
    if keyId=="collector_number": 
        return 45
    if keyId=="digital": 
        return 46
    if keyId=="rarity": 
        return 47
    if keyId=="flavor_text": 
        return 48
    if keyId=="card_back_id": 
        return 49
    if keyId=="artist": 
        return 50
    if keyId=="artist_ids": 
        return 51
    if keyId=="illustration_id": 
        return 52
    if keyId=="border_color": 
        return 53
    if keyId=="frame": 
        return 54
    if keyId=="full_art": 
        return 55
    if keyId=="textless": 
        return 56
    if keyId=="booster": 
        return 57
    if keyId=="story_spotlight": 
        return 58
    if keyId=="edhrec_rank": 
        return 59
    if keyId=="penny_rank": 
        return 60
    if keyId=="prices": 
        return 61
    if keyId=="related_uris": 
        return 62
    if keyId=="purchase_uris": 
        return 63
    if keyId=="all_parts": 
        return 64
    if keyId=="promo_types": 
        return 65
    if keyId=="arena_id": 
        return 66
    if keyId=="security_stamp": 
        return 67
    if keyId=="card_faces": 
        return 68
    if keyId=="preview": 
        return 69
    if keyId=="produced_mana": 
        return 70
    if keyId=="watermark": 
        return 71
    if keyId=="frame_effects": 
        return 72
    if keyId=="loyalty": 
        return 73
    if keyId=="printed_name": 
        return 74


def initializeSheet():
    worksheet.write(0,0,"object")
    worksheet.write(0,1,"id")
    worksheet.write(0,2,"oracle_id")
    worksheet.write(0,3,"multiverse_ids")
    worksheet.write(0,4,"mtgo_id")
    worksheet.write(0,5,"mtgo_foil_id")
    worksheet.write(0,6,"tcgplayer_id")
    worksheet.write(0,7,"cardmarket_id")
    worksheet.write(0,8,"name")
    worksheet.write(0,9,"lang")
    worksheet.write(0,10,"released_at")
    worksheet.write(0,11,"uri")
    worksheet.write(0,12,"scryfall_uri")
    worksheet.write(0,13,"layout")
    worksheet.write(0,14,"highres_image")
    worksheet.write(0,15,"image_status")
    worksheet.write(0,16,"image_uris")
    worksheet.write(0,17,"mana_cost")
    worksheet.write(0,18,"cmc")
    worksheet.write(0,19,"type_line")
    worksheet.write(0,20,"oracle_text")
    worksheet.write(0,21,"power")
    worksheet.write(0,22,"toughness")
    worksheet.write(0,23,"colors")
    worksheet.write(0,24,"color_identity")
    worksheet.write(0,25,"keywords")
    worksheet.write(0,26,"legalities")
    worksheet.write(0,27,"games")
    worksheet.write(0,28,"reserved")
    worksheet.write(0,29,"foil")
    worksheet.write(0,30,"nonfoil")
    worksheet.write(0,31,"finishes")
    worksheet.write(0,32,"oversized")
    worksheet.write(0,33,"promo")
    worksheet.write(0,34,"reprint")
    worksheet.write(0,35,"variation")
    worksheet.write(0,36,"set_id")
    worksheet.write(0,37,"set")
    worksheet.write(0,38,"set_name")
    worksheet.write(0,39,"set_type")
    worksheet.write(0,40,"set_uri")
    worksheet.write(0,41,"set_search_uri")
    worksheet.write(0,42,"scryfall_set_uri")
    worksheet.write(0,43,"rulings_uri")
    worksheet.write(0,44,"prints_search_uri")
    worksheet.write(0,45,"collector_number")
    worksheet.write(0,46,"digital")
    worksheet.write(0,47,"rarity")
    worksheet.write(0,48,"flavor_text")
    worksheet.write(0,49,"card_back_id")
    worksheet.write(0,50,"artist")
    worksheet.write(0,51,"artist_ids")
    worksheet.write(0,52,"illustration_id")
    worksheet.write(0,53,"border_color")
    worksheet.write(0,54,"frame")
    worksheet.write(0,55,"full_art")
    worksheet.write(0,56,"textless")
    worksheet.write(0,57,"booster")
    worksheet.write(0,58,"story_spotlight")
    worksheet.write(0,59,"edhrec_rank")
    worksheet.write(0,60,"penny_rank")
    worksheet.write(0,61,"prices")
    worksheet.write(0,62,"related_uris")
    worksheet.write(0,63,"purchase_uris")
    worksheet.write(0,64,"all_parts")
    worksheet.write(0,65,"promo_types")
    worksheet.write(0,66,"arena_id")
    worksheet.write(0,67,"security_stamp")
    worksheet.write(0,68,"card_faces")
    worksheet.write(0,69,"preview")
    worksheet.write(0,70,"produced_mana")
    worksheet.write(0,71,"watermark")
    worksheet.write(0,72,"frame_effects")
    worksheet.write(0,73,"loyalty")
    worksheet.write(0,74,"printed_name")


with open('cards copy.json','r') as file:
    data = json.load(file)

initializeSheet()
with open('cards.txt','r',encoding="utf8") as file2:    
    for line in file2:        
        if(count%10000 == 0):
            print(count)
        try:
            if(line != "[" and line != "]"):
                all_but_one = str(line[:-2])
                card = json.loads(all_but_one)
                saveCardAttempt(card)                
                row = row+1
        except:
            print("An error occured parsing line "+str(count))            
        count = count + 1            
        # if(count>100):
        #     workbook.close()
        #     quit()

workbook.close()
        
        