"""
KT4

Tutustu omatoimisesti Pandas-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa.  Esimerkkisovellus on vapaavalintainen.


"""
#imports here
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Arvotaan 10 satunnaislukua 0-999 väliltä
    df = pd.DataFrame({"Luvut": np.random.randint(0, 1000, 10)})

    # Jotta luvut saadaan tasaisesti printattua
    suurintasaus = ""
    pienintasaus = ""

    # Lasketaan keskiarvo
    keskiarvo = df["Luvut"].mean()

    # Suurin luku ja indeksi
    suurin = df["Luvut"].max()
    suurin_indeksi = df["Luvut"].idxmax() + 1
    if suurin < 10:
        suurintasaus = "  "
    elif suurin >= 10 and suurin < 100:
        suurintasaus = " "

    # Pienin luku ja indeksi
    pienin = df["Luvut"].min()
    pienin_indeksi = df["Luvut"].idxmin() + 1
    if pienin < 10:
        pienintasaus = "  "
    elif pienin >= 10 and pienin < 100:
        pienintasaus = " "

    # Tulostetaan DataFrame ja analyysin tulokset
    print("Satunnaisluvut: " + ", ".join(map(str, df["Luvut"].tolist())))
    print(f"Suurin luku:    {suurintasaus}{suurin}, tuli kierrokselta: {suurin_indeksi}")
    print(f"Pienin luku:    {pienintasaus}{pienin}, tuli kierrokselta: {pienin_indeksi}")
    print(f"Keskiarvo:      {keskiarvo:.2f}")





