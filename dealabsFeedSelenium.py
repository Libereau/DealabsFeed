import feedparser
import json
import os
import re
import getpass
from bs4 import BeautifulSoup
from selenium import webdriver

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
            browser = webdriver.Firefox(executable_path="geckodriver.exe")
            browser.get(lienArticle)
            pageHtml = browser.page_source
            soup = BeautifulSoup(pageHtml, 'html.parser')
            classe = soup.find('div', class_='threadItem-headerMeta')
            temp = classe.text.replace("\t","")
            temp = temp.replace(" ","")
            temp = temp.replace("\n","")
            print("      . Température - "+temp)
            #print("      . Température - "+str(temp))
            browser.close()
