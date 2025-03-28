"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU. Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022. Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt. Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
import datetime

def LueAutot():
    autot = {}
    while True:
        rekisterinumero = input("Syötä rekisterinumero (tai LOPPU lopettaaksesi): ")

        if rekisterinumero.upper() == "LOPPU":
            print()
            break

        while True:
            try:
                pvm_str = input("Syötä rekisteröintipäivämäärä (pp.kk.vvvv): ")
                rekisteripvm = datetime.datetime.strptime(pvm_str, "%d.%m.%Y").date()
                break
            except ValueError:
                print("Virheellinen päivämäärämuoto!")

        autot[rekisterinumero] = rekisteripvm

    return autot

def TalletaTiedostoon(autot):
    if not autot:
        print("Ei autoja!")
        return

    with open("autot.txt", "w") as tiedosto:
        for rekisterinumero, pvm in autot.items():
            tiedosto.write(f"{rekisterinumero}\t{pvm.strftime('%d.%m.%Y')}\n")

def LueTiedostosta():
    autot = {}
    try:
        with open("autot.txt", "r") as tiedosto:
            for rivi in tiedosto:
                rivi = rivi.strip()
                rekisterinumero, pvm_str = rivi.split('\t')
                pvm = datetime.datetime.strptime(pvm_str, "%d.%m.%Y").date()
                autot[rekisterinumero] = pvm
    except FileNotFoundError:
        print("Tiedostoa ei löydy!")

    return autot

def TulostaTiedot(autot):
    if not autot:
        print("Ei autoja!")
        return

    print("Rekisterinumero\tRekisteröintipäivä\n")

    for rekisterinumero, pvm in sorted(autot.items()):
        print(f"{rekisterinumero}\t\t{pvm.strftime('%d.%m.%Y')}")

if __name__ == "__main__":
    autot = LueAutot()
    TalletaTiedostoon(autot)
    luetut_autot = LueTiedostosta()
    TulostaTiedot(luetut_autot)


    


