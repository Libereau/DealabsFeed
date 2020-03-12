import feedparser
import json
import os
import re

os.system('cls') # or 'clear' for linux
print("\n[#] Dealabs RSS feed parser.")
url = "<Your Url Here>"
feed = feedparser.parse(url)

if feed.bozo == 1:
    exit("\n    [!] Erreur réseau")

print("\n ############################################### \n")

print("Liste des produits : ")

if feed.status != 200:
    exit("[!] RSS feed not reachable!")
else:
    if feed.entries != "":
        entries = feed.entries

        for i in range(0, len(feed.entries)):
            print("\n  [!] Nouveau produit : ")
            print("      . "+feed.entries[i].title)
            summary = feed.entries[i].summary
            price = re.findall("<strong>(.*?)</strong",summary)
            print("      . Prix - "+price[0].split(" ")[0])
            dateOfPublishing = feed.entries[i].published
            print("      . Date de publication - "+dateOfPublishing)
            lienArticle = feed.entries[i].id
            print("      . Lien - "+lienArticle)
