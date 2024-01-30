import requests
from bs4 import BeautifulSoup

def scrape(url,file):

    r = requests.get(url)
    soup= BeautifulSoup(r.content,"html.parser")
    name_tags = soup.findAll('h2', class_='ItemTitle-module_item-title__VuKDo')
    price_tags = soup.select('a.SmallCard-module_link__hOkzY p.index-module_price__N7M2x')
    if(len(name_tags)==0 & len(price_tags)==0):
        print("la pagina è vuota")
        return -1
    if(len(name_tags)!=len(price_tags)):
        print("Errore: nomi e prezzi di lunghezza diversa")
        return -2
    for i in range(len(name_tags)):
        file.write(name_tags[i].text.strip()+ " " + price_tags[i].text.strip()+"\n")
        #print(name_tags[i].text.strip(),price_tags[i].text.strip())

    return len(name_tags)