import feedparser
import json
import os
import re
import getpass
from bs4 import BeautifulSoup
import requests
import time

os.system('cls')
print("\n[#] Dealabs RSS feed parser.")
url = "https://www.dealabs.com/rssx/keyword-alarm/nIXuN_M_dZMkHo96vKMt0q9rHkiuc7M5EI_JFfKNYVk."
feed = feedparser.parse(url)

if feed.bozo == 1:
    exit("\n    [!] Erreur réseau ou Url non spécifiée")

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
            lienArticle
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(lienArticle, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            classe = soup.find('div', class_='threadItem-headerMeta')
            temp = classe.text.replace("\t","")
            temp = temp.replace(" ","")
            temp = temp.replace("\n","")
            print("      . Température - "+temp)
