import helper
import os
import sys

#def scrape_caller(url,page_state):
#    cont=2
#    url=url+"&o="+str(cont)
#    while page_state > 0:
#        page_state=helper.scrape(url)
#        cont+=1
#        url=url[:-1]+str(cont)


print("Subito helper v 0.2")
print("Vuoi controllare se viene inserito un nuovo prodotto su una certa ricerca su Subito, o vuoi monitorare il prezzo di un prodotto?")
mode=int(input("Inserisci 1 per creare un avviso di inserimento prodotto, 2 per creare un avviso di prezzo di un prodotto,3 per info dettagliate: "))
if(mode==3):
    print("Modalità 1: Utile se si vuole essere avvisati quando su subito viene inserito un nuovo oggetto di una ricerca che ci interessa.\nPer esempio, fornendo l'indirizzo di ricerca 'https://www.subito.it/annunci-italia/vendita/usato/?q=hifiman',il programma accederà alla pagina e controllerà la presenza di elementi nuovi rispetto all'ultima scansione")
    print("Modalità 2: Inserendo l'url di un oggetto in vendita,")
    sys.exit()
if(mode==1):
    new_items_url = input("Inserisci l'indirizzo della pagina subito di cui vuoi monitorare l'inserimento di un nuovo oggetto: ")
    new_items_filename = input("Inserisci un nome attinente per il file: ")
    new_items_filepath = os.path.join("new_items",new_items_filename+".json")
    f = open(new_items_filepath,"a")
    print("adesso sto scaricando la prima pagina dei risultati e la salvo nel file, potrebbe volerci un po' in base alle condizioni della rete")
    f.write(new_items_url+"\n")
    helper.scrape(new_items_url,f)
    f.close()
    print("finito!")
    sys.exit()

#mode 2 da fare, ignorare tutto quello che sta sotto questo commento

#print("vuoi creare un nuovo file o selezionarne uno esistente?")
#value=int(input("premere 1 per creare un nuovo file, premere 2 per scegliere un file esistente: "))
#if(value==1):
#    filename = input("Inserisci un nome per il file su cui verranno scritti tutti i prezzi. Il file verrà salvato nella sottocartella 'listings':")
#    filepath = os.path.join("listings",filename+".txt")
#    f = open(filepath,"a")


#url = "https://www.subito.it/annunci-italia/vendita/usato/?q=hifiman"
#page_state = helper.scrape(url)
#print(page_state,url)
#scrape_caller(url,page_state)