"""
KT1

Tee kaksi lambda-funktiota:
* summa saa parametrinaan kaksi lukua ja palauttaa niiden summan
* tulo saa parametrinaan kaksi lukua ja palauttaa niiden tulon

Tee laske-funktio, joka saa parametrinaan funktion ja listan lukuja. Funktio palauttaa listassa olevien lukujen tulon tai summan riippuen kumpaa em lambda-funktiota käytettiin funktion kutsussa. Jos luvut-lista on tyhjä, niin palautetaan 0 ja jos luvut sisältää vain yhden alkion, niin palautetaan tämä alkio.

VIHJE: Jos lista=[1, 2, 3], niin voit laskea alkioiden summan, s,  summa-funktion avulla näin:

s=summa(summa(1, 2), 3) .

Vastaava pätäee myös tuloon.


Pääohjelma on valmiina, älä muokkaa sitä.

Esimerkkitulostus:
1320
28
4
4
0
0

"""
#Write lambdas and laske here

summa = lambda a, b: a + b
tulo = lambda a, b: a * b

def laske(function, luvut):
    if not luvut:
        return 0
    if len(luvut) == 1:
        return luvut[0]

    tulos = luvut[0]
    for luku in luvut[1:]:
        tulos = function(tulos, luku)

    return tulos


# Don't touch lines below
if __name__ == "__main__":
    luvut = [1, 5, 8, 11, 3]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = [4]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = []
    print(laske(tulo, luvut))
    print(laske(summa, luvut))
