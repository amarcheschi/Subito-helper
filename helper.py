import requests
import sys
from bs4 import BeautifulSoup

r = requests.get('https://www.subito.it/annunci-toscana/vendita/usato/?q=sennheiser&o=4')
#print(r.text)
soup= BeautifulSoup(r.content,"html.parser")
#soup.prettify()
#print(soup.prettify())
# Trova il tag span con la classe "price_item" e l'attributo itemprop="price"
# Selezioniamo il tag span utilizzando i selettori CSS
# e usiamo tutti i classi per essere più specifici
# Cerca il tag div con la classe specificata
# Cerca il tag p con la classe specificata all'interno dell'elemento a
name_tags = soup.findAll('h2', class_='ItemTitle-module_item-title__VuKDo')
price_tags = soup.select('a.SmallCard-module_link__hOkzY p.index-module_price__N7M2x')
if(len(name_tags)!=len(price_tags)):
    print("Errore: nomi e prezzi di lunghezza diversa")
    sys.exit()
for i in range(len(name_tags)):
    print(name_tags[i].text.strip(),price_tags[i].text.strip())
# Se il tag viene trovato, stampa il suo contenuto testuale
#if price_tag:
#    print(price_tag.text.strip())
#else:
#    print("Il prezzo non è stato trovato.")