import requests
from bs4 import BeautifulSoup

# Struktūra spēļu datiem
class Spele:
    def __init__(self, komanda1, komanda2, datums, laiks, rezultats1, rezultats2, statuss):
        self.komanda1 = komanda1
        self.komanda2 = komanda2
        self.datums = datums
        self.laiks = laiks
        self.rezultats1 = rezultats1
        self.rezultats2 = rezultats2
        self.statuss = statuss

    #Spēļu datu struktūras izvadīšana
    def __str__(self):
        return f"{self.komanda1} vs {self.komanda2} - {self.datums} {self.laiks} ({self.rezultats1}:{self.rezultats2}) - {self.statuss}"

#Ir iespējams iegūt IIHF spēļus grafiku lapas saturu
adrese = "https://www.iihf.com/en/events/2025/wm/schedule"

lapa = requests.get(adrese)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    # print(lapas_saturs.prettify())
    atradu_card = lapas_saturs.find_all(class_="b-card-schedule")
    #print(len(atradu_card))
    # TODO: Iegūt valstis sarakstu

    speles_lapa = []
    lapa = []
    for card in atradu_card:
        spele = Spele("", "", "", "", "", "", "")
        list = []

        #Iegūstam komandas nosaukumus
        komandas = card.find(class_="s-countries")
        #print(komandas.prettify())
        komandas = komandas.find_all("span")
        komanda1 = komandas[0].get_text(strip=True)
        komanda2 = komandas[1].get_text(strip=True)
        #print(komanda1)
        #print(komanda2)
        spele.komanda1 = komanda1
        spele.komanda2 = komanda2
        list.append(komanda1)
        list.append(komanda2)

        #Iegūstam spēles datumu
        datums = card.find(class_="s-date")
        #print(datums.prettify())
        datums = datums.get_text(strip=True)
        spele.datums = datums
        list.append(datums)
        #print(datums)

        #Iegūstam spēles laiku
        laiks = card.find(class_="s-time")
        #print(laiks.prettify())
        laiks = laiks.get_text(strip=True)
        spele.laiks = laiks
        list.append(laiks)
        #print(laiks)

        #Iegūstam spēles rezultātu
        rezultats1 = card.find(class_="s-count js-homescore")
        rezultats2 = card.find(class_="s-count js-awayscore")
        #print(rezultats1.prettify())
        #print(rezultats2.prettify())
        rezultats1 = rezultats1.get_text(strip=True)
        rezultats2 = rezultats2.get_text(strip=True)
        spele.rezultats1 = rezultats1
        spele.rezultats2 = rezultats2
        list.append(rezultats1)
        list.append(rezultats2)
        #print(rezultats1)
        #print(rezultats2)

        #Iegūstam spēles statusu
        statuss = card.find(class_="s-text")
        #print(statuss.prettify())
        statuss = statuss.find("span").get_text(strip=True)
        spele.statuss = statuss
        list.append(statuss)
        #print(statuss)
        
        speles_lapa.append(spele)
        lapa.append(list)

    # print()
    # for spele in speles_lapa:
    #     print(spele)
    # print()
    # print(lapa)


    #Menu
    print("\nSpēļu grafiks")
    while True:
        print("\n1. Iegūt visu spēles grafiku")
        print("2. Iegūt iepriekšējās spēles grafiku")
        print("3. Iegūt tiešraidu spēles grafiku")
        print("4. Iegūt gaidāmās spēles grafiku")
        # print("5. Iegūt valsta datus") TODO: Sortēšana pēc valsti
        # print("6. Iegūt rezultātu tablo") TODO: Uzzimēt rezultātu tablo
        print("5. Iziet")
        izvēle = input("Izvēlieties opciju: ")
        print()
        if izvēle == "1":
            for spele in speles_lapa:
                print(spele)
        elif izvēle == "2":
            for spele in speles_lapa:
                if spele.statuss == "FINAL" or spele.statuss == "F(OT)" or spele.statuss == "F(SO)":
                    print(spele)
        elif izvēle == "3":
            for spele in speles_lapa:
                if spele.statuss == "LIVE":
                    print(spele)
        elif izvēle == "4":
            for spele in speles_lapa:
                if spele.statuss == "UPCOMING":
                    print(spele)
        elif izvēle == "5":
            break