"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU. 

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

"""

def LuoNimetJaArvosanat():
    henkilot = {}
    while True:
        nimi = input("Nimi: ")
        if nimi.lower() == "loppu":
            break

        if nimi in henkilot:
            print("Henkilö on jo listassa.")
            continue

        try:
            arvosana = int(input("Arvosana: "))
            if arvosana < 0:
                arvosana = 0
            elif arvosana > 5:
                arvosana = 5
        except ValueError:
            print("Virheellinen syöte, arvosanaksi asetetaan 0.")
            arvosana = 0

        henkilot[nimi] = arvosana

    return henkilot

def TulostaHylatyt(henkilot):
    hylatyt = [nimi for nimi, arvosana in henkilot.items() if arvosana == 0]
    for nimi in hylatyt:
        print(nimi)

def PalautaHylattyjenMaara(henkilot):
    hylattyjen_maara = sum(1 for arvosana in henkilot.values() if arvosana == 0)
    print(hylattyjen_maara)

def TulostaKaikki(henkilot):
    for nimi, arvosana in henkilot.items():
        print(f"{nimi}: {arvosana}")

if __name__ == "__main__":
    tiedot = LuoNimetJaArvosanat()
    hylattyjen_maara = sum(1 for arvosana in tiedot.values() if arvosana == 0)

    if hylattyjen_maara > 0:
        print(f"Hylättyjen määrä: {hylattyjen_maara}")
        TulostaHylatyt(tiedot)
    else:
        TulostaKaikki(tiedot)



        
