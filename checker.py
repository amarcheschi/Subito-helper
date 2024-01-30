import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

#controlla se esistono nuovi elementi online non nel foglio offline

p = Path('new_items')
directories = [x for x in p.iterdir()]

for file_path in directories:
    with open(file_path,"r") as file:
        url=file.readline().strip()
        print(url)
        for line in file:
            print(line.strip())
        print("######################################\n")
        r = requests.get(url)
        soup= BeautifulSoup(r.content,"html.parser")
        name_tags = soup.findAll('h2', class_='ItemTitle-module_item-title__VuKDo')
        price_tags = soup.select('a.SmallCard-module_link__hOkzY p.index-module_price__N7M2x')
        new_count=0
        for i in range(len(name_tags)):
            online_item=name_tags[i].text.strip()+ " " + price_tags[i].text.strip()
            file.seek(0)
            flag=0
            print("elemento da cercare: "+online_item)
            for line in file:
                offline_item = line.strip()
                print(offline_item)
                if(offline_item == online_item):
                    flag=1
                    print("elemento trovato! ")
                    break
            if(flag==0):
                print("elemento online nuovo: "+online_item)
                new_count+=1
        print("\ntrovati "+str(new_count)+" elementi nuovi")
            
   