# -*- coding: utf-8 -*-

"""
KT7

Toimeentulotukea maksetaan turvaamaan perustuslaissa tarkoitettu välttämätön toimeentuloa.
Tee ohjelma, joka laskee yksinäisen henkilön tai perheen saaman toimeentulotuen.
Ohjelma laskee tuen määrän käyttäjän syöttämälle määrälle päiviä ja tulostaa toimeentulotuen kokonaismäärän kahdella desimaalilla.
Ohjelma kysyy tuen laskemisessa tarvittavat tiedot yhdessä asumisesta ja lapsista.
Toimeentulotuen määrä lasketaan alla olevan taulukon mukaisesti kahden desimaalin tarkkuudella.
Toimeentulotuen laskemista voidaan toistaa niin monta kertaa kuin ohjelman käyttäjä haluaa. Alla on suuntaa antava esimerkki ohjelman toiminnasta.

Tuki lasketaan siis yhdelle henkilölle, ei esim avioparille


Tuen saaja

Euroa / päivä

Yksin asuva

16,18

Yksinhuoltaja

17,80

Avio- ja avopuolisot kumpikin

13,76

Jokainen 10-17-vuotias lapsi

11,33

Jokainen alle 10-vuotias lapsi

10,20



Tämä ohjelma laskee toimeentulotuen määrän. Alla esimerkkiajo ohjelmasta.

Koodin rakenteelle ei aseteta vaatimuksia muuten kuin, että syötteet annetaan esimerkin mukaisessa järjestyksessä ja ohjelma laskee (tulostaa) tuen määrän oikein. Esimerkkiajosta käy ilmi. että kysymyksiä luupataan eli ohjelma päättyy vasta kun  käyttäjä ei halua enää laskea toimeentulotukea uusilla tiedoilla.



Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): k

Asutko yksin (1) vai puolison kanssa (2) : 1

Onko sinulla/teillä alaikäisiä lapsia (k/e) : k

Kuinka monta alle 10-vuotiasta lasta : 1

Kuinka monta 10-17-vuotiasta lasta : 2

Kuinka monelle päivälle tuki lasketaan : 10



Saat toimeentulotukea 506.60 euroa

Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): e

"""
euroa = 0

while True:
    while True:
        try:
            saaty = int(input("Asutko yksin (1) vai puolison kanssa (2) : "))
            if saaty in [1, 2]:
                break
            else:
                print("Asutko yksin (1) vai puolison kanssa (2) : ")
        except ValueError:
            print("Asutko yksin (1) vai puolison kanssa (2) : ")

    if saaty == 1:
        euroa = 16.18
    else:
        euroa = 13.76

    while True:
        lapset = input("Onko sinulla/teillä alaikäisiä lapsia (k/e) : ").lower()
        if lapset in ['k', 'e']:
            break
        else:
            print("Onko sinulla/teillä alaikäisiä lapsia (k/e) : ")

    if lapset == 'k':
        if saaty == 1:
            euroa = 17.80
        allekymmenen = int(input("Kuinka monta alle 10-vuotiasta lasta : "))
        alapsista = allekymmenen * 10.20
        ylikymmenen = int(input("Kuinka monta 10-17-vuotiasta lasta : "))
        lapsista = ylikymmenen * 11.33 + alapsista
    else:
        lapsista = 0

    while True:
        try:
            paivat = int(input("Kuinka monelle päivälle tuki lasketaan : "))
            if paivat > 0:
                break
            else:
                print("Kuinka monelle päivälle tuki lasketaan : ")
        except ValueError:
            print("Kuinka monelle päivälle tuki lasketaan : ")

    tuki = (euroa + lapsista) * paivat

    print(f"Saat toimeentulotukea {tuki:.2f} euroa")
    print()
    uudelleen = input("Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ").lower()
    if uudelleen == 'k':
        continue
    else:
        break
