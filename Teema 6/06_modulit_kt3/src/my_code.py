"""
KT3

Tutustu omatoimisesti NymPy-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa. Esimerkkisovellus on vapaavalintainen.



"""

#ilmeisesti tarkoitettiin NumPy-kirjastoa?

#imports here
import numpy as np

if __name__ == "__main__":
    # Arvotaan 10 satunnaislukua 0-999 väliltä
    satunnaisluvut = np.random.randint(0, 1000, 10)

    # Jotta luvut saadaan tasaisesti printattua
    suurintasaus = ""
    pienintasaus = ""

    # Lasketaan keskiarvo
    keskiarvo = np.mean(satunnaisluvut)

    # Suurin luku ja indeksi
    suurin = np.max(satunnaisluvut)
    suurin_indeksi = np.argmax(satunnaisluvut) + 1
    if suurin < 10:
        suurintasaus = "  "
    elif suurin >= 10 and suurin < 100:
        suurintasaus = " "

    # Pienin luku ja indeksi
    pienin = np.min(satunnaisluvut)
    pienin_indeksi = np.argmin(satunnaisluvut) + 1
    if pienin < 10:
        pienintasaus = "  "
    elif pienin >= 10 and pienin < 100:
        pienintasaus = " "

    # Tulostetaan satunnaisluvut ja niiden keskiarvo
    print("Satunnaisluvut: " + ", ".join(map(str, satunnaisluvut)))
    print(f"Suurin luku:    {suurintasaus}{suurin}, tuli kierrokselta: {suurin_indeksi}")
    print(f"Pienin luku:    {pienintasaus}{pienin}, tuli kierrokselta: {pienin_indeksi}")
    print(f"Keskiarvo:      {keskiarvo}")




