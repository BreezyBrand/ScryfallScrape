# ScryfallScrape
Using the bulk files from Scryfall, generate a spreadsheet or populate a local database.

1) Open your desired server and run "Intiialize.sql" to create the database and tables on your local machine

2) Within this repo on your local repo, go to scryfall and download the "all_cards_<timestamp>.json" file and rename it to "cards.txt". For ease, remove the leading "[" and tailing "]" lines

3) Run "write to db.py"
