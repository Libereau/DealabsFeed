import feedparser
import json
import os
import re
import getpass
from bs4 import BeautifulSoup
import requests
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

os.system('clear')
f = open("produitsDealabs.txt", 'w')
print("\n[#] Dealabs RSS feed parser.")
f.write("[#] Dealabs RSS feed parser.\n")

url = "https://www.dealabs.com/rssx/keyword-alarm/nIXuN_M_dZMkHo96vKMt0q9rHkiuc7M5EI_JFfKNYVk."
feed = feedparser.parse(url)

if feed.bozo == 1:
    exit("\n    [!] Erreur réseau ou Url non spécifiée")

if feed.status != 200:
    exit("[!] RSS feed not reachable!")
else:
    if feed.entries != "":
        entries = feed.entries

        for i in range(0, len(feed.entries)):
            summary = feed.entries[i].summary
            price = re.findall("<strong>(.*?)</strong",summary)
            dateOfPublishing = feed.entries[i].published
            lienArticle = feed.entries[i].id
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            r = requests.get(lienArticle, headers=headers)
            soup = BeautifulSoup(r.text, 'html.parser')
            classe = soup.find('div', class_='threadItem-headerMeta')
            temp = classe.text.replace("\t","")
            temp = temp.replace(" ","")
            temp = temp.replace("\n","")

            if temp[0] != "-" and temp != "Nouveau":
                if int(temp.split("°")[0]) > 50:
                    print("\n  [!] Nouveau produit : ")
                    f.write("\n  [!] Nouveau produit : ")
                    print("      . "+feed.entries[i].title)
                    f.write("\n      . "+feed.entries[i].title)
                    print("      . Prix - "+price[0].split(" ")[0])
                    f.write("\n      . Prix - "+price[0].split(" ")[0])
                    print("      . Date de publication - "+dateOfPublishing)
                    f.write("\n      . Date de publication - "+dateOfPublishing)
                    print("      . Lien - "+lienArticle)
                    f.write("\n      . Lien - "+lienArticle)
                    print("      . Température - "+temp)
                    f.write("\n      . Température - "+temp)
                    f.write("\n")


print("\n")
port = 465
adresse = "your address"
password = "your pass"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(adresse, password)

    message = MIMEMultipart()
    message["From"] = adresse
    message["To"] = adresse
    message["Subject"] = "Nouveaux deals !"
    text = "Nouveaux deals, regarde la piece jointe !"

    message.attach(MIMEText(open("/home/libero/Documents/programmes/DealabsFeed/produitsDealabs.txt").read()))

    server.sendmail(adresse, adresse, text)
